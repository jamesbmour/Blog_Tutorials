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
# Initialize 'counter' if not present
if "counter" not in st.session_state:
    st.session_state.counter = 1  # Using attribute syntax

# Initialize 'input_text' if not present
if "input_text" not in st.session_state:
    st.session_state["input_text"] = ""  # Using dictionary syntax

st.subheader("Increment Counter Example")
# Display current counter
st.write(f"Current Counter: {st.session_state.counter}")

# Button to increment the counter
if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.success("Counter incremented!")


st.markdown("---")
# 2. Update Session State with Callbacks
st.header("2. Update Session State with Callbacks")


# 3. Delete Items from Session State
st.markdown("---")
st.header("3. Delete Items from Session State")


st.markdown("---")
# 4. Session State and Widget Association
st.header("4. Session State and Widget Association")


st.markdown("---")
# 5. Forms and Callbacks
st.header("5. Forms and Callbacks")
