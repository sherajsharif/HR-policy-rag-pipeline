# 🏢 HR Policy Query Resolution System using RAG Pipeline

An enterprise-grade AI-powered HR assistant built using **Retrieval-Augmented Generation (RAG)** architecture to provide accurate, context-aware, and conversational responses from HR policy documents.

The application combines **Groq LLMs**, **LangChain**, **FAISS Vector Search**, and **HuggingFace Embeddings** to create a scalable and production-ready conversational AI solution.

---

# 🌐 Live Demo

🚀 **Deployed Application:**  
https://hr-policy-query-resolution-system-using-rag-pipeline.streamlit.app/

---

# 📸 Application Preview

## Main Interface

![HR Policy RAG Assistant](./assets/hr_rag_ui.png)

---

# 🚀 Key Features

- ✅ Conversational HR Policy Assistant
- ✅ Retrieval-Augmented Generation (RAG)
- ✅ Context-Aware Question Answering
- ✅ Multi-turn Conversation Memory
- ✅ Semantic Search using FAISS
- ✅ Groq Llama 3.1 Integration
- ✅ MMR-based Intelligent Retrieval
- ✅ Multi-PDF Support
- ✅ Streamlit Interactive UI
- ✅ Modular & Scalable Architecture
- ✅ Production-Ready Deployment

---

# 🧠 System Architecture

```text
User Query
    ↓
Question Contextualization
    ↓
Semantic Vector Retrieval
    ↓
MMR-Based Relevant Chunk Selection
    ↓
Groq LLM Generation
    ↓
Context-Aware HR Response
```

---

# ⚙️ Technology Stack

| Category | Technology |
|---|---|
| LLM | Groq - Llama 3.1 8B Instant |
| Embeddings | HuggingFace Endpoint Embeddings |
| Vector Database | FAISS |
| Framework | LangChain (LCEL) |
| Frontend | Streamlit |
| Programming Language | Python |
| Document Loader | PyPDFLoader |
| Text Splitter | RecursiveCharacterTextSplitter |

---

# 📂 Project Structure

```bash
HR-policy-rag-pipeline/
│
├── app.py
├── ingest.py
├── rag_pipeline.py
├── embeddings.py
├── utils.py
├── requirements.txt
├── README.md
│
├── Data/
│   └── HR policy PDFs
│
├── vectorstore/
│   ├── index.faiss
│   └── index.pkl
│
└── assets/
    └── hr_rag_ui.png
```

---

# 🔄 Workflow

## Phase 1 — Data Ingestion

1. Load HR policy PDF documents
2. Extract and preprocess text
3. Split text into optimized chunks
4. Generate semantic embeddings
5. Store vectors in FAISS database

---

## Phase 2 — Conversational Query Pipeline

1. User submits HR-related question
2. Chat history is analyzed
3. Question contextualization occurs
4. Relevant chunks are retrieved
5. Groq LLM generates grounded response
6. Response displayed in Streamlit UI

---

# 🧩 Module Overview

## `app.py`
Handles:
- Streamlit frontend UI
- Chat interaction
- Session state management
- Suggested queries
- Chat history rendering

---

## `ingest.py`
Responsible for:
- PDF ingestion
- Document preprocessing
- Text chunking
- FAISS vector database creation

---

## `rag_pipeline.py`
Contains:
- Conversational RAG chain
- Prompt engineering
- Contextual question reformulation
- MMR retrieval logic
- LLM orchestration

---

## `embeddings.py`
Manages:
- HuggingFace embedding generation
- Secure API token handling
- Cloud embedding inference

---

## `utils.py`
Provides:
- PDF loading utilities
- Metadata attachment
- Recursive text splitting

---

# 💬 Example Queries

- What is the annual leave policy?
- What is the resignation notice period?
- What are the office timings?
- What is the travel reimbursement policy?
- What is the medical reimbursement limit?
- What is the travel per diem for Sweden?

---

# 🚀 Local Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/sherajsharif/HR-policy-rag-pipeline.git
cd HR-policy-rag-pipeline
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

---

## 4️⃣ Build Vector Database

```bash
python ingest.py
```

---

## 5️⃣ Launch Streamlit App

```bash
streamlit run app.py
```

---

# 🌐 Deployment

The application is deployed using Streamlit Cloud.

🔗 Live Application:  
https://hr-policy-query-resolution-system-using-rag-pipeline.streamlit.app/

---

# 🔐 Security Practices

- API keys securely managed using Streamlit Secrets
- `.env` excluded using `.gitignore`
- No hardcoded credentials in source code
- Context-grounded response generation reduces hallucinations

---

# 📈 Future Enhancements

- Hybrid Search (BM25 + Dense Retrieval)
- PDF Upload Support
- Source Citation Responses
- Docker Deployment
- AWS/GCP/Azure Hosting
- Authentication System
- Real-time Streaming Responses
- Conversation Export Feature

---

# 👨‍💻 Author

## Sheraj Sharif

### Connect With Me

- GitHub: https://github.com/sherajsharif
- LinkedIn: https://www.linkedin.com/in/sheraj-sharif-652723250/
- Portfolio: https://sherajsharif.github.io/

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
