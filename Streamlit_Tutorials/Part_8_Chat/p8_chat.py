import streamlit as st

st.set_page_config(
    page_title="Streamlit Part 8: Chat Elements",
    page_icon="random",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("Streamlit Part 8: Chat Elements")

st.write("### chat messages")
with st.chat_message("user"):
    st.write("### chat message")

with st.chat_message("bot"):
    st.write("### chat message")

st.write("### chat input")
prompt = st.chat_input("Hello this is a chat input")
if prompt:
    st.write(f"User input: {prompt}")
