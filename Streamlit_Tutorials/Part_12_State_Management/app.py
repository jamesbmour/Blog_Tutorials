# Part 12: Streamlit Session State Management Tutorial
# app.py
import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Streamlit Session State Management Tutorial",
    layout="wide",
)

# Title of the app
st.title("Streamlit Session State Management Tutorial")

with st.sidebar:
    # Display current state
    st.header("Current State")
    st.write(st.session_state)


# 1. Initialize Values in Session State
st.header("1. Initialize Values in Session State")


st.markdown("---")

# 2. Update Session State with Callbacks
st.header("2. Update Session State with Callbacks")


st.markdown("---")

# 3. Delete Items from Session State
st.header("3. Delete Items from Session State")


st.markdown("---")

# 4. Serializable Session State
st.header("4. Serializable Session State")


st.markdown("---")

# 5. Session State and Widget Association
st.header("5. Session State and Widget Association")


st.markdown("---")

# 6. Forms and Callbacks
st.header("6. Forms and Callbacks")
