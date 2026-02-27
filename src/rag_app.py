import os
from pathlib import Path

# Disable Chroma telemetry noise
os.environ["ANONYMIZED_TELEMETRY"] = "False"

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from llama_cpp import Llama

from prompts import SYSTEM_PROMPT, USER_TEMPLATE

CHROMA_DIR = Path("chroma_db")
EMBED_MODEL = "BAAI/bge-small-en-v1.5"
MODEL_PATH = "models/qwen2.5-3b-instruct.Q4_K_M.gguf"


def load_db():
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    db = Chroma(
        persist_directory=str(CHROMA_DIR),
        embedding_function=embeddings,
        collection_name="incident_kb",
    )
    return db

def load_llm():
    if not Path(MODEL_PATH).exists():
        raise FileNotFoundError(f"Missing model at {MODEL_PATH}. Download GGUF and place it there.")

    # Tune for Mac CPU/Metal
    llm = Llama(
        model_path=MODEL_PATH,
        n_ctx=4096,
        n_threads=8,
        n_gpu_layers=10,  # uses Metal if available; lower if it errors
        verbose=False,
    )
    return llm

def build_context(docs):
    blocks = []
    for i, d in enumerate(docs, start=1):
        src = d.metadata.get("source", "unknown")
        text = d.page_content.strip()
        blocks.append(f"[{i}] SOURCE: {src}\n{text}\n")
    return "\n".join(blocks)

def generate_answer(llm: Llama, prompt: str) -> str:
    # Qwen instruct is chatty; we keep it simple with a single completion call
    out = llm(
        prompt,
        max_tokens=800,
        temperature=0.1,
        top_p=0.9,
        repeat_penalty=1.1
    )

    return out["choices"][0]["text"].strip()

def ask(user_input: str, k: int = 6):
    db = load_db()
    llm = load_llm()

    docs = db.similarity_search(user_input, k=k)
    context = build_context(docs)

    prompt = f"{SYSTEM_PROMPT}\n\n" + USER_TEMPLATE.format(context=context, user_input=user_input)
    answer = generate_answer(llm, prompt)

    return answer, docs

if __name__ == "__main__":
    sample_query = """We are seeing login failures in production after a config change.
Users get 401 Unauthorized. Possible token validation issue.
What info is missing and what should we check next?"""

    response, docs = ask(sample_query, k=6)
    print("\n" + "="*90)
    print(response)
    print("\n" + "="*90)
    print("Retrieved sources:")
    for i, d in enumerate(docs, start=1):
        print(f"[{i}] {d.metadata.get('source','unknown')}")