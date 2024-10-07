import streamlit as st
import time

# =========================
# Streamlit App Configuration
# =========================

# Configure the Streamlit page settings
st.set_page_config(
    page_title="Streamlit Part 8: Chat Elements",  # Title of the web page
    layout="wide",  # Layout set to wide for better use of screen space
    initial_sidebar_state="collapsed",  # Sidebar is collapsed by default
)

# =========================
# App Title and Introduction
# =========================

# Display the main title of the app
st.title("Streamlit Part 8: Chat Elements")

# =========================
# Session State Initialization
# =========================

# Initialize session state to store chat messages
# This ensures that messages persist across user interactions
if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================
# Display Existing Chat Messages
# =========================

# Section header for chat messages
st.write("### Chat Messages")

# Iterate through each message stored in session state
for msg in st.session_state.messages:
    # Determine the role of the message sender ('user' or 'bot')
    with st.chat_message(msg["role"]):
        # Display the content of the message
        st.write(msg["content"])

# =========================
# Chat Input Section
# =========================

# Section header for chat input
st.write("### Chat Input")

# Capture user input from the chat input box
# The placeholder text prompts the user to type their message
prompt = st.chat_input("Type your message here...")

# Check if the user has entered any input
if prompt:
    # =========================
    # Display User's Message
    # =========================

    # Append the user's message to the session state
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display the user's message in the chat interface
    with st.chat_message("user"):
        st.write(prompt)

    # =========================
    # Simulate Bot Response Delay
    # =========================

    # Introduce a 1-second delay to simulate the bot 'thinking'
    time.sleep(1)

    # =========================
    # Generate and Display Bot's Response
    # =========================

    # Create the bot's response by echoing the user's input
    bot_response = f"You said: {prompt}"

    # Append the bot's response to the session state
    st.session_state.messages.append({"role": "bot", "content": bot_response})

    # Display the bot's response in the chat interface
    with st.chat_message("bot"):
        st.write(bot_response)
