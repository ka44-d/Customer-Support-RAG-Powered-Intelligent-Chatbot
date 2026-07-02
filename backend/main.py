from fastapi import FastAPI
from pydantic import BaseModel

from backend.data_loader import load_data, build_chunks
from backend.embedding import get_embeddings
from backend.retriever import build_index
from backend.rag import answer_with_rag
from backend.logger import logger


app = FastAPI()

embedder = None
index = None
mini_docs = None


@app.on_event("startup")
def startup():

    global embedder
    global index
    global mini_docs

    df = load_data()

    mini_docs = build_chunks(df)

    chunk_texts = [doc["text"] for doc in mini_docs]

    embedder, embeddings = get_embeddings(chunk_texts)

    index = build_index(embeddings)

    logger.info("RAG loaded successfully!")

class ChatRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {
        "message": "RAG Customer Support API is running successfully!"
    }

@app.post("/chat")
def chat(request: ChatRequest):


    answer, hits = answer_with_rag(
        query=request.question,
        embedder=embedder,
        index=index,
        mini_docs=mini_docs
    )


    return {
        "question": request.question,
        "answer": answer,
        "hits": hits
    }