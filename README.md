# 🏢 Celebal HR Policy RAG Assistant

A production-grade Retrieval-Augmented Generation (RAG) system built to provide intelligent, context-aware answers to HR policy queries using open-source tools and high-performance APIs.

---

## 🛠️ Technical Stack
*   **LLM**: Groq (Llama-3.1-8b-instant) - Chosen for sub-second response times and high reasoning quality.
*   **Embeddings**: Hugging Face Inference API (`all-MiniLM-L6-v2`) - Cloud-based to ensure 100% compatibility across Windows/Linux without local dependency issues.
*   **Vector Database**: FAISS (Facebook AI Similarity Search) - A high-performance local vector database for efficient semantic search.
*   **Orchestration**: LangChain (LCEL) - Used for building modular, conversational chains with memory.
*   **Frontend**: Streamlit - A premium, interactive web interface for the chatbot.

---

## 📁 File Architecture & Purpose

### 1. `app.py` (The Interface)
*   **Purpose**: The main entry point for the user. It manages the web UI, chat history, and the interaction between the user and the RAG pipeline.
*   **Key Features**: Sidebar suggested questions, session-state memory, and markdown-based chat styling.

### 2. `ingest.py` (The Knowledge Builder)
*   **Purpose**: A standalone script used to process PDFs and build the vector database.
*   **Workflow**: Reads PDFs from `Data/` -> Splits text -> Generates Embeddings -> Saves FAISS index to `vectorstore/`.
*   **Note**: Run this whenever you add or update your PDF documents.

### 3. `rag_pipeline.py` (The Brain)
*   **Purpose**: Contains the core logic for the RAG system.
*   **Key Features**:
    *   **MMR Retrieval**: Ensures a diverse set of document chunks are found to avoid repetitive context.
    *   **Contextualizer**: Re-phrases follow-up questions (e.g., "What about *this*?") into standalone queries.
    *   **Table Intelligence**: Hardcoded logic to help the AI correctly interpret HR grade tables (M01-M11).

### 4. `utils.py` (The Data Processor)
*   **Purpose**: Utility functions for document loading and text splitting.
*   **Key Features**: Automatically attaches metadata (Policy Name) to every text chunk so the AI knows which document it is reading.

### 5. `embeddings.py` (The Connector)
*   **Purpose**: Configures the connection to the Hugging Face API.
*   **Benefit**: By moving embeddings to the cloud, it bypasses the `WinError 126` (DLL missing) common on Windows machines running PyTorch.

### 6. `.env` (The Safe)
*   **Purpose**: Stores sensitive API keys (`GROQ_API_KEY`, `HUGGINGFACEHUB_API_TOKEN`) securely.

---

## 🔄 The System Workflow

### Phase A: Data Ingestion (One-time or on update)
1.  **PDF Loading**: `utils.py` reads PDFs and converts them into text.
2.  **Metadata Tagging**: Each chunk is tagged with its source file name.
3.  **Embedding Generation**: Text is sent to Hugging Face Cloud to be converted into 384-dimensional vectors.
4.  **Vector Storage**: The vectors and text are saved locally in the `vectorstore/` folder.

### Phase B: Conversational Query (User interaction)
1.  **Input**: User asks a question in `app.py`.
2.  **Contextualization**: The AI looks at previous chat history and the new question to create a "Standalone Question."
3.  **MMR Retrieval**: The system searches the FAISS index for the 10 most relevant and diverse chunks of policy text.
4.  **Generation**: The text chunks + standalone question are sent to **Groq**. 
5.  **Output**: The AI provides a detailed answer based *only* on the retrieved context.

---

## 🚀 How to Run
1.  **Activate Environment**: `venv\Scripts\activate`
2.  **Install Deps**: `pip install -r requirements.txt`
3.  **Index Data**: `python ingest.py`
4.  **Launch App**: `streamlit run app.py`
