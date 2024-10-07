# Streamlit Part 8 Chat Elements
import streamlit as st

st.set_page_config(
    page_title="Streamlit Part 8: Chat Elements",
    page_icon="random",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("Streamlit Part 8: Chat Elements")

st.write("""1. st.chat_message`st.chat_message` Inserts a chat message container.""")

st.write("""2. st.chat_input`st.chat_input` Inserts a chat input box.""")
prompt = st.chat_input("Type your message here...")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("bot"):
        st.write("I am a bot")
