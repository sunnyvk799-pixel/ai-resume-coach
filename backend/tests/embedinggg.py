from app.rag.embeddings import embed_text
from app.rag.vector_store import vector_store

question = "Python backend"

embedding = embed_text(question)

results = vector_store.search(
    embedding=embedding,
    k=2
)

print(results["documents"])