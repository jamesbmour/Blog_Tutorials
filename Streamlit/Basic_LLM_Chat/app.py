# Import necessary libraries
import streamlit as st
import ollama
from typing import Dict, Generator

# add page config
st.set_page_config(
    page_title="Ollama Chat App",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("Ollama with Streamlit Chat App")
