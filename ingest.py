import os
from utils import load_pdfs, split_text
from rag_pipeline import build_vector_store

def main():
    print("Loading documents from 'Data/' folder...")
    docs = load_pdfs("Data")
    if not docs:
        print("Error: No PDFs found in 'Data/' folder.")
        return
        
    print(f"Loaded {len(docs)} document pages.")
    
    print("Splitting text into chunks...")
    chunks = split_text(docs)
    print(f"Created {len(chunks)} text chunks.")
    
    print("Building vector store (this may take a moment)...")
    build_vector_store(chunks)
    print("Success! Vector store built and saved to 'vectorstore/' folder.")

if __name__ == "__main__":
    main()
