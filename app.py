import streamlit as st
from langchain.chat_models import ChatOllama
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

# Load .env config if needed
load_dotenv()

# Streamlit UI
st.set_page_config(page_title="Local AI Chat", layout="centered")
st.title("💬 Ollama Chat (Local LLM)")

# Session state to hold chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input field
user_input = st.chat_input("Type your message...")

# Chat model setup
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        llm = ChatOllama(model=os.getenv("OLLAMA_MODEL", "mistral"))
        response = llm([HumanMessage(content=user_input)])
        reply = response.content
    except Exception as e:
        reply = f"❌ Error: {str(e)}"

    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
