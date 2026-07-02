from backend.retriever import search_index
from backend.generator import build_prompt, generate_answer
from config import (
    TOP_K,
    SEARCH_POOL,
    TEMPERATURE,
    MAX_TOKENS
)

# ---------------------------
# 5. RAG Function
# ---------------------------
# Retrieve top-k relevant chunks using embeddings and pass to LLM


def answer_with_rag(
    query,
    embedder,
    index,
    mini_docs,
    k=TOP_K,
    pool=SEARCH_POOL,
    temp=TEMPERATURE,
    max_tokens=MAX_TOKENS
):

    # Step 1: Search relevant chunks
    indices = search_index(
        index=index,
        embedder=embedder,
        query=query,
        pool=pool
    )

    # Step 2: Select top k chunks
    hits = []

    for idx in indices[0]:
        doc = mini_docs[int(idx)]

        if len(doc["text"].split()) >= 20:
            hits.append(doc)

        if len(hits) >= k:
            break

    if not hits:
        return "Sorry, no relevant info found.", []

    # Step 3: Build context
    context = "\n\n".join(
        [
            f"[Doc {i+1}] (rid={h['rid']}, chunk={h['chunk_id']})\n{h['text']}"
            for i, h in enumerate(hits)
        ]
    )

    # Step 4: Build prompt
    prompt = build_prompt(context, query)

    # Step 5: Generate answer
    answer = generate_answer(
        prompt=prompt,
        temp=temp,
        max_tokens=max_tokens
    )

    return answer, hits