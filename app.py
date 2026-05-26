import streamlit as st
import os
from rag_pipeline import load_vector_store, get_rag_chain, HumanMessage, AIMessage

# Page Config
st.set_page_config(page_title="HR Policy Assistant", page_icon="🏢", layout="wide")

# Custom CSS for Premium Look
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏢 HR Policy Query Assistant")
st.markdown("Ask any question regarding company policies (Leave, Travel, Health Check, etc.)")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for Quick Actions
with st.sidebar:
    st.header("💡 Suggested Questions")
    st.caption("Click a question to ask the bot instantly:")
    
    suggestions = [
        "What is the annual leave policy?",
        "What are the general office timings?",
        "How much is the health checkup limit?",
        "What is the notice period for resignation?",
        "What is the travel per diem for Sweden?"
    ]
    
    for suggestion in suggestions:
        if st.button(suggestion, use_container_width=True):
            # We'll set a trigger in session state to handle the button click
            st.session_state.active_query = suggestion

# Initialize Vector Store
if "vector_store" not in st.session_state:
    st.session_state.vector_store = load_vector_store()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Main Query Area
if st.session_state.vector_store:
    # Check if a suggestion was clicked, otherwise wait for chat input
    query = st.chat_input("Enter your question: (e.g., What is the annual leave policy?)")
    
    if "active_query" in st.session_state:
        query = st.session_state.active_query
        del st.session_state.active_query # Clear it so it doesn't repeat

    if query:
        # Display user message in chat message container
        st.chat_message("user").markdown(query)
        
        # Prepare chat history for the chain
        chat_history = []
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                chat_history.append(HumanMessage(content=msg["content"]))
            else:
                chat_history.append(AIMessage(content=msg["content"]))
        
        # Add user message to chat history state
        st.session_state.messages.append({"role": "user", "content": query})

        with st.spinner("Searching for answers..."):
            qa_chain = get_rag_chain(st.session_state.vector_store)
            # Pass both the input and the chat history
            answer = qa_chain.invoke({"input": query, "chat_history": chat_history})

            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                st.markdown(answer)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": answer})
else:
    st.warning("No vector database found. Please run 'python ingest.py' in your terminal first to build the knowledge base.")

# Status Indicator
st.divider()
st.caption("Powered by Groq, Sentence-Transformers & LangChain")
