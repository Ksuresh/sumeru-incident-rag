from pathlib import Path

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

CHROMA_DIR = Path("chroma_db")
EMBED_MODEL = "BAAI/bge-small-en-v1.5"

def main():
    if not CHROMA_DIR.exists():
        raise FileNotFoundError("Missing chroma_db/. Run src/index_chroma.py first.")

    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    db = Chroma(
        persist_directory=str(CHROMA_DIR),
        embedding_function=embeddings,
        collection_name="incident_kb",
    )

    queries = [
        "SSLHandshakeException certificate expired during deployment",
        "login failure 401 unauthorized token validation mismatch",
        "HikariPool connection is not available timed out after 30000ms",
        "DNS NXDOMAIN load balancer 504 gateway timeout",
    ]

    for q in queries:
        print("\n" + "="*80)
        print("QUERY:", q)
        results = db.similarity_search(q, k=4)

        for i, r in enumerate(results, start=1):
            src = r.metadata.get("source", "unknown")
            snippet = r.page_content[:280].replace("\n", " ")
            print(f"\n[{i}] SOURCE: {src}")
            print("    ", snippet, "...")

if __name__ == "__main__":
    main()