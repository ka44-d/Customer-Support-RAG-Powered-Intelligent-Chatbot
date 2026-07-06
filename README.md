# 🤖 RAG-Powered Customer Support Chatbot

A Retrieval-Augmented Generation (RAG) chatbot for customer support using FastAPI, Streamlit, FAISS, Sentence Transformers, Docker, and Azure Container Apps.

---

## Features

- AI-powered customer support chatbot
- Retrieval-Augmented Generation (RAG)
- Semantic search using FAISS
- Sentence Transformers embeddings
- Groq LLM integration
- FastAPI REST API
- Streamlit Web Interface
- Dockerized deployment
- Azure Container Apps deployment

---

## Tech Stack

- Python 3.12
- FastAPI
- Streamlit
- FAISS
- Sentence Transformers
- Groq API
- Docker
- Azure Container Apps

---

## Project Structure

```text
backend/
frontend/
config/
data/
models/
tests/
Dockerfile.backend
Dockerfile.frontend
docker-compose.yml
```

---

## Architecture

```
User
   │
   ▼
Streamlit Frontend
   │
POST /chat
   ▼
FastAPI Backend
   │
Retriever (FAISS)
   │
Top-k Context
   ▼
Groq LLM
   │
Generated Answer
   ▼
User
```

---

## Running with Docker

### Backend

```bash
docker build -t backend -f Dockerfile.backend .
docker run -p 8000:8000 backend
```

### Frontend

```bash
docker build -t frontend -f Dockerfile.frontend .
docker run -p 8501:8501 frontend
```

---

## API Endpoints

### Home

```
GET /
```

### Chat

```
POST /chat
```

Example:

```json
{
  "question": "How to reset password?"
}
```

---

## Deployment

- Backend deployed on Azure Container Apps
- Frontend deployed on Azure Container Apps
- Docker images stored in Azure Container Registry

---

## Author

Kamal Ayman Khedr
Faculty of Computer Science and Artificial Intelligence
Menoufia National University