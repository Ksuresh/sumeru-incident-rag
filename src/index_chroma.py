import os
from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

DATA_DIR = Path("data/kb_md")
CHROMA_DIR = Path("chroma_db")

EMBED_MODEL = "BAAI/bge-small-en-v1.5"  # CPU-friendly, high quality
CHUNK_SIZE = 1200
CHUNK_OVERLAP = 200

def main():
    if not DATA_DIR.exists():
        raise FileNotFoundError(f"Missing {DATA_DIR}. Unzip incident_kb_md.zip into data/kb_md/")

    print(f"Loading markdown files from: {DATA_DIR}")
    loader = DirectoryLoader(
        str(DATA_DIR),
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
        show_progress=True,
    )
    docs = loader.load()
    print(f"Loaded documents: {len(docs)}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", " ", ""],
    )
    chunks = splitter.split_documents(docs)
    print(f"Created chunks: {len(chunks)}")

    print(f"Creating embeddings with: {EMBED_MODEL}")
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_DIR),
        collection_name="incident_kb",
    )
    db.persist()

    print(f"✅ Chroma index created at: {CHROMA_DIR.resolve()}")

if __name__ == "__main__":
    main()