from langchain.schema import HumanMessage, AIMessage, SystemMessage
import streamlit as st
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from os import getenv
from langchain_openai import ChatOpenAI

load_dotenv()

# add page config
st.set_page_config(
    page_title="Ollama Chat App",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("💬 Ollama with Streamlit Chat App")

# Initialize model selection
with st.sidebar:
    model_option = st.selectbox(
        "Select Model", ("llama3.2", "llama3.2:1b", "qwen2.5:0.5b")
    )

    # Add a clear chat button
    if st.button("Clear Chat"):
        st.session_state.messages = [
            SystemMessage(content="You are a helpful AI assistant.")
        ]
        st.rerun()

    if st.button("Clear Cache"):
        st.cache_data.clear()
        st.cache_resource.clear()


# Initialize the chat model
def get_chat_model():
    return ChatOllama(model=model_option, streaming=True)


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
        message_placeholder = st.empty()
        full_response = ""

        # Stream the response
        for chunk in chat_model.stream(st.session_state.messages):
            if chunk.content:
                full_response += chunk.content
                message_placeholder.markdown(full_response + "▌")

        # Final response without cursor
        message_placeholder.markdown(full_response)

        # Add the full response to session state
        st.session_state.messages.append(AIMessage(content=full_response))

# Display model information
st.sidebar.markdown("---")
st.sidebar.markdown("### Model Information")
st.sidebar.write(f"Current Model: {model_option}")
