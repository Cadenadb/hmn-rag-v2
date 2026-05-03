"""RAG query endpoints."""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter()


class QueryRequest(BaseModel):
    question: str
    collection: str = "default"
    top_k: int = 5
    stream: bool = False


class Source(BaseModel):
    doc_id: str
    chunk: str
    score: float


class QueryResponse(BaseModel):
    answer: str
    sources: List[Source]
    model: str
    latency_ms: int


@router.post("/", response_model=QueryResponse)
async def query(req: QueryRequest):
    """Run a RAG query against the vector store."""
    # TODO: connect to RAG engine
    return QueryResponse(
        answer="RAG engine initializing — connect your API keys in .env",
        sources=[],
        model="gpt-4o-mini",
        latency_ms=0,
    )
