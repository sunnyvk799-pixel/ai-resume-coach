import chromadb


class VectorStore:

    def __init__(self):
        self.client = chromadb.PersistentClient(path="chroma_db")

        self.collection = self.client.get_or_create_collection(
            name="resume_coach"
        )

    def add_documents(
        self,
        ids,
        documents,
        embeddings,
        metadatas
    ):
        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(
        self,
        embedding,
        document_id,
        k=3
    ):
        return self.collection.query(
            query_embeddings=[embedding],
            n_results=k,
            where={
                "document_id": document_id
            }
        )

vector_store = VectorStore()