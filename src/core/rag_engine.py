"""Core RAG engine — orchestrates retrieval + generation."""
from __future__ import annotations
from typing import List
from dataclasses import dataclass


@dataclass
class RetrievedChunk:
    text: str
    doc_id: str
    score: float
    metadata: dict


class RAGEngine:
    """
    Hybrid retrieval + LLM generation pipeline.

    Steps:
      1. Embed query (OpenAI text-embedding-3-small)
      2. Vector search (ChromaDB)
      3. Keyword re-rank (BM25)
      4. Cross-encoder re-rank (top-K)
      5. Prompt assembly + LLM call
      6. Return answer + sources
    """

    def __init__(self, llm, embedder, vector_store, cache=None):
        self.llm = llm
        self.embedder = embedder
        self.vector_store = vector_store
        self.cache = cache

    async def query(self, question: str, collection: str = "default", top_k: int = 5) -> dict:
        # 1. Cache check
        if self.cache:
            cached = await self.cache.get(question)
            if cached:
                return cached

        # 2. Embed
        embedding = await self.embedder.embed(question)

        # 3. Vector search
        chunks: List[RetrievedChunk] = await self.vector_store.search(
            embedding, collection=collection, top_k=top_k * 2
        )

        # 4. Re-rank (placeholder — swap in cross-encoder)
        chunks = sorted(chunks, key=lambda c: c.score, reverse=True)[:top_k]

        # 5. Build context
        context = "\n\n".join(f"[{c.doc_id}] {c.text}" for c in chunks)

        # 6. LLM call
        prompt = (
            f"Answer the question using ONLY the context below.\n"
            f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
        )
        answer = await self.llm.complete(prompt)

        result = {
            "answer": answer,
            "sources": [{"doc_id": c.doc_id, "chunk": c.text[:200], "score": c.score} for c in chunks],
        }

        if self.cache:
            await self.cache.set(question, result)

        return result
