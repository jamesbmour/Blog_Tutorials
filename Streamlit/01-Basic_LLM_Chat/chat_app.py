from langchain.schema import HumanMessage, AIMessage, SystemMessage
from os import getenv
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
import streamlit as st

load_dotenv()

# add page config
st.set_page_config(
    page_title="Ollama Chat App",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("Ollama with Streamlit Chat App")

# Initialize model selection
model_option = st.sidebar.selectbox(
    "Select Model", ("llama3.2", "llama3.2:1b", "qwen2.5:0.5b")
)


# Initialize the chat model
# @st.cache_resource
def get_chat_model():
    return ChatOllama(model=model_option)


chat_model = get_chat_model()

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpful AI assistant.")
    ]

# Display chat messages
for message in st.session_state.messages[1:]:  # Skip the system message
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to state and display
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.write(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_model.invoke(st.session_state.messages)
            st.write(response.content)
            st.session_state.messages.append(AIMessage(content=response.content))

# Add a clear chat button
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = [
        SystemMessage(content="You are a helpful AI assistant.")
    ]
    st.rerun()

# Display model information
st.sidebar.markdown("---")
st.sidebar.markdown("### Model Information")
st.sidebar.write(f"Current Model: {model_option}")
