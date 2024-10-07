# Streamlit Part 9: Status Elements
import streamlit as st
import time

# Set the page configuration for Streamlit app
st.set_page_config(
    page_title="Streamlit Part 9: Status",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("Streamlit Part 9: Status Elements")
#  st.progress
st.write("### status.progress")

# Initialize the progress bar
st.write("### st.status")

# Display a success message with an icon
st.write("### st.spinner")


# Display a spinner while the operation is in progress
st.write("### st.success")


# Display a success message after the operation completes
st.write("### st.error")

# Display an error message
st.write("### st.warning")

# Display a warning message
st.write("### st.info")

# Display an info message
st.write("### st.exception")


# Display an exception message
st.write("### st.snow")
