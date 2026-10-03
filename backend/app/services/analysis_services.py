import uuid

from app.ats.analyzer import analyze
from app.rag.chunker import chunk_text
from app.rag.embeddings import embed_chunks
from app.rag.vector_store import vector_store

class AnalysisService:

    def analyze(self, resume_text: str, jd_text: str):
        document_id = str(uuid.uuid4())

        # ATS Analysis
        ats_result = analyze(resume_text, jd_text)

        ids = []
        documents = []
        embeddings = []
        metadatas = []

        # Resume
        resume_chunks = chunk_text(resume_text)
        resume_embeddings = embed_chunks(resume_chunks)

        for chunk, embedding in zip(resume_chunks, resume_embeddings):
            ids.append(str(uuid.uuid4()))
            documents.append(chunk)
            embeddings.append(embedding)
            metadatas.append({
                "document_id": document_id,
                "document_type": "resume"
            })  

        # Job Description
        jd_chunks = chunk_text(jd_text)
        jd_embeddings = embed_chunks(jd_chunks)

        for chunk, embedding in zip(jd_chunks, jd_embeddings):
            ids.append(str(uuid.uuid4()))
            documents.append(chunk)
            embeddings.append(embedding)
            metadatas.append({
                "document_id": document_id,
                "document_type": "job_description"
            })

        vector_store.add_documents(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

        return {
            **ats_result,
            "document_id": document_id
        }


analysis_service = AnalysisService()
