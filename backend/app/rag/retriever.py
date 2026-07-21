from app.rag.embeddings import embed_text
from app.rag.vector_store import vector_store


def retrieve(
    question: str,
    document_id: str,
    k: int = 3
):
    question_embedding = embed_text(question)

    results = vector_store.search(
        embedding=question_embedding,
        document_id=document_id,
        k=k
    )

    return results