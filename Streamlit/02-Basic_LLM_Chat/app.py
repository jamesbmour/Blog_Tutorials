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
