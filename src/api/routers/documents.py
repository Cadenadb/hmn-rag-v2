"""Document upload and management endpoints."""
from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter()


class IngestResponse(BaseModel):
    doc_id: str
    chunks: int
    status: str


@router.post("/ingest", response_model=IngestResponse)
async def ingest_document(file: UploadFile = File(...), collection: Optional[str] = "default"):
    """Upload and process a document (PDF, DOCX, TXT) into the vector store."""
    allowed = {"application/pdf", "text/plain",
               "application/vnd.openxmlformats-officedocument.wordprocessingml.document"}
    if file.content_type not in allowed:
        raise HTTPException(status_code=415, detail=f"Unsupported type: {file.content_type}")
    # TODO: route to PDFProcessor service
    return IngestResponse(doc_id="placeholder", chunks=0, status="queued")


@router.get("/list")
async def list_documents(collection: str = "default"):
    """List all ingested documents in a collection."""
    return {"collection": collection, "documents": []}
