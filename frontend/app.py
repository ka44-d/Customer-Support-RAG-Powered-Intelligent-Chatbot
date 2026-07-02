import sys
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

import streamlit as st
import requests


# ---------------------------
# Page Setup
# ---------------------------
st.set_page_config(page_title="RAG Chatbot ", page_icon="🤖")
st.title("🤖 RAG-Powered Customer Support Chatbot")


# ---------------------------
# Chat History
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------------------
# Chat Input
# ---------------------------
query = st.chat_input("Ask a support question...")

if query:

    st.session_state.messages.append(
        {"role": "user", "content": query}
    )

    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
        with st.spinner("Searching..."):
            response = requests.post(
                f"{BACKEND_URL}/chat",
                json={
                    "question": query
                }
            )

            data = response.json()

            answer = data["answer"]
            
            hits = data["hits"]
            
            st.markdown(answer)

    
        with st.expander("Context Chunks Used"):

            for i, h in enumerate(hits, start=1):

                st.markdown(
                    f"**[Doc {i}] rid={h['rid']} | chunk={h['chunk_id']}**"
                )

                st.markdown(h["text"])

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )