# Import necessary libraries
import streamlit as st
import ollama
from typing import Dict, Generator

st.set_page_config(
    page_title="Ollama Chat App",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)
st.title("Ollama with Streamlit demo")
# add page config

# Initialize session state variables if they don't exist
# Session state persists data between reruns of the app
if "selected_model" not in st.session_state:
    st.session_state.selected_model = ""
if "messages" not in st.session_state:
    # Store chat history
    st.session_state.messages = []

# Sidebar to display the current state and available models
with st.sidebar:
    st.write("State: ")
    st.json(st.session_state, expanded=True)
    st.write("Models: ")
    st.json(ollama.list()["models"], expanded=True)


# Define a function that generates responses from the Ollama model
def ollama_generator(model_name: str, messages: Dict) -> Generator:
    """
    Creates a generator that streams responses from the Ollama model
    Args:
        model_name: The name of the Ollama model to use
        messages: Chat history in the format Ollama expects
    Returns:
        Generator yielding chunks of the model's response
    """
    stream = ollama.chat(model=model_name, messages=messages, stream=True)
    for chunk in stream:
        yield chunk["message"]["content"]


# Create a dropdown to select the AI model
# Gets list of available models from Ollama and displays them
st.session_state.selected_model = st.selectbox(
    "Please select the model:", [model["name"] for model in ollama.list()["models"]]
)

# Display all previous messages in the chat history
for message in st.session_state.messages:
    # Creates chat bubble UI
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
            ollama_generator(st.session_state.selected_model, st.session_state.messages)
        )

    # Add AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
