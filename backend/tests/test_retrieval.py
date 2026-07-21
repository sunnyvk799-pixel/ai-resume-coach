from app.rag.retriever import retrieve

results = retrieve(
    "What backend technologies do I know?"
)

print(results["documents"])