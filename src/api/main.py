"""HMN RAG v2.0 — FastAPI entrypoint."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import structlog

from src.api.routers import documents, queries, health

log = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info("hmn_rag_startup", version="2.0.0")
    yield
    log.info("hmn_rag_shutdown")


app = FastAPI(
    title="HMN RAG v2.0",
    description="Advanced Retrieval-Augmented Generation API",
    version="2.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, tags=["Health"])
app.include_router(documents.router, prefix="/documents", tags=["Documents"])
app.include_router(queries.router, prefix="/query", tags=["Query"])
