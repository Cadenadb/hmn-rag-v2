"""PDF processing service — extract, chunk, and embed documents."""
from __future__ import annotations
import io
from typing import List


def extract_text_from_pdf(data: bytes) -> str:
    """Extract raw text from PDF bytes using pypdf."""
    try:
        from pypdf import PdfReader
        reader = PdfReader(io.BytesIO(data))
        pages = [page.extract_text() or "" for page in reader.pages]
        return "\n".join(pages)
    except Exception as e:
        raise ValueError(f"PDF extraction failed: {e}") from e


def chunk_text(text: str, size: int = 512, overlap: int = 64) -> List[str]:
    """Split text into overlapping chunks by word count."""
    words = text.split()
    chunks, start = [], 0
    while start < len(words):
        end = min(start + size, len(words))
        chunks.append(" ".join(words[start:end]))
        start += size - overlap
    return chunks
