import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")

    CHROMA_PATH: str = os.getenv(
        "CHROMA_PATH",
        "chroma_db"
    )

    FRONTEND_URL: str = os.getenv(
        "FRONTEND_URL",
        "http://localhost:5174"
    )


settings = Settings()