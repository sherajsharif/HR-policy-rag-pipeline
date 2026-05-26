import os
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

def get_embeddings():
    """Initializes and returns HuggingFace endpoint embeddings (runs in the cloud, bypasses local OS issues)."""
    huggingface_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    if not huggingface_token:
        raise ValueError("HUGGINGFACEHUB_API_TOKEN not found in .env file.")
        
    return HuggingFaceEndpointEmbeddings(
        model="sentence-transformers/all-MiniLM-L6-v2",
        huggingfacehub_api_token=huggingface_token
    )
