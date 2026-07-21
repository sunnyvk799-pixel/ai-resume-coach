from sentence_transformers import SentenceTransformer

# Load the model once when the application starts
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_text(text: str) -> list[float]:
    """Generate an embedding for a single text."""
    return model.encode(text).tolist()


def embed_chunks(chunks: list[str]) -> list[list[float]]:
    """Generate embeddings for multiple chunks."""
    return model.encode(chunks).tolist()