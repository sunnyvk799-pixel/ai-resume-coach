from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.rag.qa import ask

router = APIRouter(tags=["Chat"])


class ChatRequest(BaseModel):
    question: str
    document_id: str 


class ChatResponse(BaseModel):
    answer: str
    sources: list[str]


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        result = ask(request.question,
                     request.document_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))