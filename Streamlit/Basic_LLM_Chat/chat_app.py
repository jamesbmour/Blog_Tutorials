# Import necessary libraries
import streamlit as st
from typing import Dict, Generator
from langchain_community.chat_models import ChatOllama
from langchain.schema import HumanMessage, AIMessage, SystemMessage
import requests
from langchain_openai import ChatOpenAI
from os import getenv
from dotenv import load_dotenv
import ollama

load_dotenv()

# add page config
st.set_page_config(
    page_title="Ollama Chat App",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("Ollama with Streamlit Chat App")

with st.expander("State and Models Info"):
    st.write(
        "Ollama is a conversational AI model developed by Langchain. It is designed to generate human-like responses to user input."
    )
    st.write("State: ")
    st.json(st.session_state, expanded=True)
    st.write("Models: ")
    st.json(ollama.list()["models"][1], expanded=True)

# Initialize session state variables if they don't exist
if "selected_model" not in st.session_state:
    st.session_state.selected_model = ""
if "messages" not in st.session_state:
    st.session_state.messages = []


# Function to get available models from Ollama
def get_available_models():
    try:
        response = requests.get("http://localhost:11434/api/tags")
        if response.status_code == 200:
            models = response.json()
            return [model["name"] for model in models["models"]]
        return []
    except:
        return []


# Define a function that generates responses from the Ollama model
def chat_generator(model_name: str, messages: list) -> Generator:
    """
    Creates a generator that streams responses from the Ollama model
    Args:
        model_name: The name of the Ollama model to use
        messages: Chat history in LangChain message format
    Returns:
        Generator yielding chunks of the model's response
    """
    # chat_model = ChatOllama(model=model_name)

    chat_model = ChatOpenAI(
        model="meta-llama/llama-3.2-3b-instruct:free",
        openai_api_key=getenv("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1",
        temperature=0.5,
    )

    # Convert messages to LangChain format
    langchain_messages = []
    for msg in messages:
        if msg["role"] == "user":
            langchain_messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            langchain_messages.append(AIMessage(content=msg["content"]))
        elif msg["role"] == "system":
            langchain_messages.append(SystemMessage(content=msg["content"]))

    # Stream the response
    for chunk in chat_model.stream(langchain_messages):
        yield chunk.content


# Create a dropdown to select the AI model
st.session_state.selected_model = st.selectbox(
    "Please select the model:",
    available_models if available_models else ["No models found"],
)

# Display all previous messages in the chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input through the chat interface
if prompt := st.chat_input("How could I help you?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and display AI response
    with st.chat_message("assistant"):
        # Stream the AI response using our generator function
        response = st.write_stream(
            chat_generator(st.session_state.selected_model, st.session_state.messages)
        )

    # Add AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
