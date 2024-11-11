from langchain.schema import HumanMessage, AIMessage, SystemMessage
import streamlit as st
from dotenv import load_dotenv
from os import getenv
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
import os

load_dotenv()


# Function to configure the Streamlit page
def configure_page():
    st.set_page_config(
        page_title="Ollama Chat App",
        page_icon="🤖",
        layout="centered",
        initial_sidebar_state="expanded",
    )
    st.title("💬 Ollama with Streamlit Chat App")
    with st.expander("Check State"):
        st.write(st.session_state)


# Function to display and handle sidebar
def handle_sidebar():
    selected_model = st.sidebar.selectbox(
        "Select Model", ("llama3.2", "llama3.2:1b", "qwen2.5:0.5b", "gpt-3.5-turbo")
    )
    st.sidebar.divider()
    if st.sidebar.button("Clear Chat"):
        st.session_state.messages = [
            SystemMessage(content="You are a helpful AI assistant.")
        ]
        st.rerun()
    if st.sidebar.button("Clear Cache"):
        st.cache_data.clear()
        st.cache_resource.clear()
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Model Information")
    st.sidebar.write(f"Current Model: {selected_model}")
    return selected_model


@st.cache_resource
def get_chat_model(model_name):
    if model_name == "gpt-3.5-turbo":
        return ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            model="gpt-3.5-turbo",
            streaming=True,
        )
    return ChatOllama(model=model_name, streaming=True)


# Function to display chat messages
def display_chat_messages():
    for message in st.session_state.messages[1:]:
        if isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.write(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("assistant"):
                st.write(message.content)


# Function to handle new user input
def handle_user_input(chat_model):
    if prompt := st.chat_input("What would you like to know?"):
        st.session_state.messages.append(HumanMessage(content=prompt))
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for chunk in chat_model.stream(st.session_state.messages):
                if chunk.content:
                    full_response += chunk.content
                    message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
            st.session_state.messages.append(AIMessage(content=full_response))


####################################################################################################
#########################  Main execution flow  ####################################################
####################################################################################################
configure_page()

selected_model = handle_sidebar()

chat_model = get_chat_model(selected_model)

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpful AI assistant.")
    ]

display_chat_messages()

handle_user_input(chat_model)
