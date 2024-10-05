import streamlit as st
from streamlit_chat import message
import os
import dotenv
from langchain_groq import ChatGroq

# Load environment variables for API key
dotenv.load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize ChatGroq model
llm = ChatGroq(model_name="llama-3.1-70b-versatile", temperature=0)

# Initialize chat history if not set
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Simple CSS styling for UI
st.markdown("""
<style>
    .stApp { background-color: #1e1e1e; color: #fff; }
    .stTextInput > div > div > input { background-color: #333; color: #fff; }
    .stButton > button { background-color: #e50914; color: #fff; }
    .chat-message { padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem; }
    .chat-message.user { background-color: #444; }
    .chat-message.bot { background-color: #222; }
</style>
""", unsafe_allow_html=True)

# Display title
st.title("🗨️ Simple AI Chatbot")

# Display previous chat messages
for msg in st.session_state.messages:
    message(msg['content'], is_user=msg['is_user'])

# Capture user input
user_input = st.text_input("Type your message here...")

# Send message button
if st.button("Send") and user_input:
    # Add user message
    st.session_state.messages.append({"content": user_input, "is_user": True})

    # Get bot response
    response = llm.invoke(user_input)
    
    
    # Add bot response
    st.session_state.messages.append({"content": response.content, "is_user": False})

    # Refresh UI
    st.experimental_rerun()