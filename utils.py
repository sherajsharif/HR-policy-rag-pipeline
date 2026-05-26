import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_pdfs(data_path):
    """Loads all PDFs from the specified directory and attaches metadata."""
    documents = []
    for file in os.listdir(data_path):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(data_path, file))
            docs = loader.load()
            
            # Extract policy name from filename (e.g. 'leavepolicy.pdf' -> 'Leavepolicy')
            policy_name = os.path.splitext(file)[0].replace('_', ' ').title()
            
            # Attach custom metadata to each page/document chunk
            for doc in docs:
                doc.metadata['policy_name'] = policy_name
                doc.metadata['document_type'] = 'HR Policy'
                
            documents.extend(docs)
    return documents

def split_text(documents):
    """Splits loaded documents into smaller chunks for vectorization."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=100,
        length_function=len
    )
    return text_splitter.split_documents(documents)
