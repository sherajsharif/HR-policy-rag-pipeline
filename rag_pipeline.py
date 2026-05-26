import os
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from embeddings import get_embeddings
import streamlit as st
VECTOR_STORE_PATH = "vectorstore"

def build_vector_store(chunks):
    """Builds and saves a FAISS vector store from text chunks."""
    embeddings = get_embeddings()
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local(VECTOR_STORE_PATH)
    return vector_store

def load_vector_store():
    """Loads the FAISS vector store from local storage."""
    embeddings = get_embeddings()
    if os.path.exists(VECTOR_STORE_PATH):
        return FAISS.load_local(VECTOR_STORE_PATH, embeddings, allow_dangerous_deserialization=True)
    return None

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def format_docs(docs):
    formatted = []
    seen_content = set()
    for doc in docs:
        if doc.page_content not in seen_content:
            policy = doc.metadata.get('policy_name', 'Unknown Policy')
            content = f"--- Source: {policy} ---\n{doc.page_content}"
            formatted.append(content)
            seen_content.add(doc.page_content)
    return "\n\n".join(formatted)

def get_rag_chain(vector_store):
    """Creates a conversational RAG chain with memory using LCEL."""

    llm = ChatGroq(
        groq_api_key=st.secrets["GROQ_API_KEY"],
        model_name="llama-3.1-8b-instant",
        temperature=0.1
    )
    
    # 1. Contextualize Question Prompt
    # This rephrases the user's follow-up question into a standalone question
    contextualize_q_system_prompt = """Given a chat history and the latest user question which might reference context in the chat history, formulate a standalone question which can be understood without the chat history. Do NOT answer the question, just reformulate it if needed and otherwise return it as is."""
    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )
    contextualize_q_chain = contextualize_q_prompt | llm | StrOutputParser()

    # 2. Main QA Prompt
    system_prompt = """You are a helpful HR assistant for Celebal Technologies. Your goal is to answer HR queries using the provided policy context. 

Table Intelligence Instructions:
- IMPORTANT: Codes like M01-M11, E01-E11, and D01-D11 ALWAYS refer to employee Job Grades/Seniority Levels.
- Higher numbers (e.g., M11) represent more senior levels than lower numbers (e.g., M06).
- Location names (like Stockholm, Mumbai, Class A) refer to cities or regions.
- Numerical values in tables (like Rs. 1900 or SEK 400) refer to reimbursement limits or allowances.

General Guidelines:
1. Provide a clear, detailed, and professional answer based on the context.
2. If the context contains relevant information but doesn't have an exact answer, summarize what is available.
3. If the answer is completely missing from the context, only then say: "Not available in HR policies."

Context:
{context}"""
    
    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 10, "fetch_k": 20}
    )

    def contextualized_question(input):
        if input.get("chat_history"):
            return contextualize_q_chain
        return RunnablePassthrough()

    rag_chain = (
        RunnablePassthrough.assign(
            context=contextualize_q_chain | retriever | format_docs
        )
        | qa_prompt
        | llm
        | StrOutputParser()
    )
    
    return rag_chain
