import faiss

# Build FAISS index for fast similarity search (dot-product based)

def build_index(embeddings):

    index = faiss.IndexFlatIP(embeddings.shape[1])

    index.add(embeddings)

    return index



def search_index(index, embedder, query, pool=70):

    query_embedding = embedder.encode(
        [query],
        normalize_embeddings=True
    ).astype("float32")

    _, indices = index.search(query_embedding, pool)

    return indices