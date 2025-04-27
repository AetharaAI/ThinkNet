# 🧠 Brain Collective - The First "Hive Mind" AI System

Brain Collective is a Python 3.10+ project that combines 6-8 specialized local LLMs into a unified cognitive system.
It orchestrates distributed consensus, dynamic memory sharing, and a fully operational web API for interaction.

## 🛠️ Stack
- **FastAPI** (Web API)
- **SQLAlchemy** (Persistence)
- **httpx** (Async LLM calls)
- **Jinja2** (Minimal web frontend)
- **Loguru** (Logging)
- **Pydantic** (Validation)
- **YAML** (Configuration)
- **Sentence Transformers** (Semantic embeddings for memory)

## 📦 Setup

```bash
pip install -r requirements.txt
uvicorn run_brain_collective:app --reload
