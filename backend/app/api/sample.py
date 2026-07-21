from app.rag.embeddings import embed_chunks
from app.rag.vector_store import vector_store

chunks = [
    "Python Flask Docker",
    "Machine Learning using Scikit-learn",
    "React Frontend"
]

embeddings = embed_chunks(chunks)

vector_store.add_documents(
    ids=["1", "2", "3"],
    documents=chunks,
    embeddings=embeddings,
    metadatas=[
        {"type": "resume"},
        {"type": "resume"},
        {"type": "resume"},
    ]
)

print("Stored successfully!")