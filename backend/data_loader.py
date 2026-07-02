from config import DATASET_PATH, CHUNK_SIZE, CHUNK_OVERLAP
import pandas as pd
import re

# ---------------------------
# 2. Load & Clean Dataset
# ---------------------------
# Function to clean text by removing placeholders like {{...}} and
# extra whitespace, and converting to lowercase

def clean(s):
    s = re.sub(r"\{\{.*?\}\}", "", str(s))            # Remove placeholders
    return re.sub(r"\s+", " ", s).strip().lower()        # Normalize spacing & case


# Load and cache dataset after cleaning instruction & response
def load_data():
    df = pd.read_csv(DATASET_PATH)
    df["instruction_clean"] = df["instruction"].apply(clean)
    df["response_clean"] = df["response"].apply(clean)
    return df


# ---------------------------
# 3. Chunk & Embed
# ---------------------------
# Splits rows into smaller overlapping word chunks for better retrieval

def chunk_words(text, n=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    words = text.split()
    step = n - overlap
    return [" ".join(words[i:i+n]) for i in range(0, len(words), step)]




# Build and cache list of mini documents (chunks) with ID metadata

def build_chunks(df):
    docs = []
    for rid, row in df.iterrows():
        text = f"instruction: {row['instruction_clean']} | response: {row['response_clean']}"
        for i, ch in enumerate(chunk_words(text)):
            docs.append({"rid": rid, "chunk_id": i, "text": ch})
    return docs
