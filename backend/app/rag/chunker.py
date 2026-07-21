from langchain_text_splitters import RecursiveCharacterTextSplitter


splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
)


def chunk_text(text: str) -> list[str]:
    """
    Split text into overlapping chunks suitable for embeddings.
    """
    return splitter.split_text(text)