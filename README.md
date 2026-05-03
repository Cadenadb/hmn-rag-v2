# 🚀 HMN RAG v2.0 — Advanced RAG Engine

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Python](https://img.shields.io/badge/python-3.11+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Docker](https://img.shields.io/badge/docker-ready-blue)

Enterprise-grade Retrieval-Augmented Generation engine with multi-modal support,
security hardening, hybrid search, and full observability.

## ✨ Features

| Category | Capabilities |
|---|---|
| 🔒 **Security** | PDF sandboxing, input validation, rate limiting, audit logging |
| 🚀 **Performance** | Hybrid search, Redis cache, async processing, batch embeddings |
| 📊 **Multi-Modal** | PDF, DOCX, TXT, Markdown, images (OCR) |
| 🔍 **Retrieval** | Vector + keyword + cross-encoder re-ranking |
| 📈 **Observability** | Prometheus metrics, structured logging, health checks |
| 🐳 **Infra** | Docker, docker-compose, GitHub Actions CI/CD |

## 🏗️ Architecture

```
┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│  Telegram Bot    │   │   REST API       │   │  WebSocket       │
│  (python-telegram│   │  (FastAPI)       │   │  (streaming)     │
└────────┬─────────┘   └────────┬─────────┘   └────────┬─────────┘
         └────────────────────┬─┘                       │
                              ▼                         │
                    ┌─────────────────┐                 │
                    │   RAG Engine    │◀────────────────┘
                    │  (LangChain)    │
                    └────────┬────────┘
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
     ┌────────────┐ ┌──────────────┐ ┌────────────┐
     │  ChromaDB  │ │  Redis Cache │ │ PDF/Doc    │
     │  (vectors) │ │              │ │ Processor  │
     └────────────┘ └──────────────┘ └────────────┘
```

## 🚀 Quick Start

```bash
git clone https://github.com/Cadenadb/hmn-rag-v2.git
cd hmn-rag-v2
cp .env.example .env        # fill in your API keys
docker-compose up -d
```

The API is now available at `http://localhost:8000/docs`.

## 📁 Project Structure

```
hmn-rag-v2/
├── src/
│   ├── api/            # FastAPI app + routers + middleware
│   ├── core/           # RAG engine, LLM adapters, retrieval logic
│   ├── services/       # PDF processor, vector store, cache
│   └── utils/          # Security, config, monitoring helpers
├── docker/             # Dockerfiles per service
├── .github/workflows/  # CI/CD pipelines
├── configs/            # Environment-specific config YAML
├── pyproject.toml      # Python project metadata & deps
└── docker-compose.yml  # Full stack orchestration
```

## ⚙️ Configuration

Copy `.env.example` to `.env` and set:

```env
OPENAI_API_KEY=sk-...
TELEGRAM_BOT_TOKEN=...
REDIS_URL=redis://redis:6379
CHROMA_HOST=chromadb
```

## 📄 License

MIT © 2026 Cadenadb
