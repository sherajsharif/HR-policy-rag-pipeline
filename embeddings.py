import streamlit as st
from langchain_huggingface import HuggingFaceEndpointEmbeddings

def get_embeddings():
    """Initializes and returns HuggingFace endpoint embeddings."""

    huggingface_token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

    return HuggingFaceEndpointEmbeddings(
        model="sentence-transformers/all-MiniLM-L6-v2",
        huggingfacehub_api_token=huggingface_token
    )
