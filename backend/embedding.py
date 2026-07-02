import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
from config import EMBEDDINGS_PATH, EMBEDDING_MODEL

# Load sentence-transformer model and compute normalized embeddings

def get_embeddings(chunk_texts):
    model = SentenceTransformer(EMBEDDING_MODEL)

  
    embedding_file = EMBEDDINGS_PATH


    if embedding_file.exists():
        embeddings = np.load(embedding_file)    
    else:
        embeddings = model.encode(
            chunk_texts,
            batch_size=64,
            normalize_embeddings=True,
            show_progress_bar=True
        ).astype("float32")
        np.save(embedding_file, embeddings)

    return model, embeddings