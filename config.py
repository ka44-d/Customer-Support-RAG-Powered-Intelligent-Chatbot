from pathlib import Path
from dotenv import load_dotenv
import os


# ==========================
# Project Paths
# ==========================

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

DATA_DIR = BASE_DIR / "data"
CONFIG_DIR = BASE_DIR / "config"
MODELS_DIR = BASE_DIR / "models"

DATASET_PATH = DATA_DIR / "Customer_Support_Training_Dataset.csv"
EMBEDDINGS_PATH = MODELS_DIR / "embeddings.npy"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ==========================
# Model Configuration
# ==========================

EMBEDDING_MODEL = "all-MiniLM-L6-v2"
LLM_MODEL = "llama-3.1-8b-instant"

# ==========================
# RAG Configuration
# ==========================

CHUNK_SIZE = 100
CHUNK_OVERLAP = 30

TOP_K = 3
SEARCH_POOL = 70

TEMPERATURE = 0.7
MAX_TOKENS = 500