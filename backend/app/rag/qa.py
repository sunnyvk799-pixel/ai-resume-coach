from app.rag.retriever import retrieve
from app.llm.gemini import generate


def ask(question: str, document_id: str):

    results = retrieve(
        question=question,
        document_id=document_id
    )

    context = "\n\n".join(results["documents"][0])

    prompt = f"""
You are an AI Resume Coach.

Answer ONLY from the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    answer = generate(prompt)

    return {
        "answer": answer,
        "sources": results["documents"][0]
    }