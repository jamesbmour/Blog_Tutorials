import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Streamlit Part 8: Chat Elements",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Title of the app
st.title("Streamlit Part 8: Chat Elements")

# Introduction section
st.write("## Exploring Streamlit's Chat Elements")
st.write(
    """
    In this part of the Streamlit series, we'll explore how to use chat elements to create a 
    conversation-like interface within your Streamlit app. This is particularly useful for 
    creating interactive assistants, chatbots, or even simple user feedback systems.
    """
)

# Example chat messages
st.write("### Chat Messages")

st.write("#### User's Message")
with st.chat_message("user"):
    st.write("Hi there! How can I help you today?")

st.write("#### Bot's Response")
with st.chat_message("bot"):
    st.write("Sure! I can assist you with any questions you have about Streamlit.")

# Interactive chat input
st.write("### Chat Input")
st.write(
    """
    Below is a simple example of a chat input where you can enter a message, 
    and the app will respond with a generic reply. Try it out!
    """
)

# Chat input box
prompt = st.chat_input("Type your message here...")
if prompt:
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("bot"):
        st.write("I'm a bot! Here's a generic reply to your message.")

# Simulate a more complex interaction
st.write("### Simulating a Chatbot Conversation")
st.write(
    """
    Let's simulate a more complex interaction where the bot provides a different response 
    based on the user's input.
    """
)

# A simple logic to respond differently based on user input
if prompt:
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("bot"):
        if "help" in prompt.lower():
            st.write(
                "It looks like you need help. What specifically can I assist you with?"
            )
        elif "streamlit" in prompt.lower():
            st.write(
                "Streamlit is an awesome tool for building interactive web apps with Python!"
            )
        else:
            st.write("I'm not sure how to respond to that, but I'm here to help!")
