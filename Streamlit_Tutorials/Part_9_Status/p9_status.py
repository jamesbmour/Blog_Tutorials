import streamlit as st
import time

# Set the page configuration for Streamlit app
st.set_page_config(
    page_title="Streamlit Part 9: Status",  # Title of the page
    page_icon="random",  # Random icon for the page
    layout="wide",  # Layout of the page
    initial_sidebar_state="collapsed",  # Initial state of the sidebar
)

# Set the title of the app
st.title("Streamlit Part 9: Status Elements")

# Demonstrate st.progress
st.write("### st.progress")
progress_text = (
    "Operation in progress. Please wait."  # Text to display with the progress bar
)
my_bar = st.progress(0, text=progress_text)  # Initialize the progress bar

# Simulate a long-running operation
for percent_complete in range(100):
    time.sleep(0.01)  # Simulate time delay
    my_bar.progress(percent_complete + 1, text=progress_text)  # Update the progress bar

time.sleep(1)  # Wait for a second before clearing the progress bar
my_bar.empty()  # Clear the progress bar

# Add a button to rerun the app
st.button("Rerun")

# Demonstrate st.status
st.write("### st.status")
st.success(
    "This is a success message!", icon="✅"
)  # Display a success message with an icon

# Demonstrate st.spinner
st.write("### st.spinner")
with st.spinner(
    "In progress..."
):  # Display a spinner while the operation is in progress
    time.sleep(5)  # Simulate a long-running operation
st.success("Done!")  # Display a success message after the operation completes

# Demonstrate st.success
st.write("### st.success")
st.success("This is a success message!")  # Display a success message

# Demonstrate st.error
st.write("### st.error")
st.error("This is an error message!")  # Display an error message

# Demonstrate st.warning
st.write("### st.warning")
st.warning("This is a warning message!")  # Display a warning message

# Demonstrate st.info
st.write("### st.info")
st.info("This is an info message!")  # Display an info message

# Demonstrate st.exception
st.write("### st.exception")
try:
    raise Exception(
        "This is an exception!"
    )  # Raise an exception to demonstrate st.exception
except Exception as e:
    st.exception(e)  # Display the exception message

# Demonstrate st.balloons
st.write("### st.balloons")
st.balloons()  # Display balloons for a fun effect

# Demonstrate st.snow
st.write("### st.snow")
st.snow()  # Display snow for a festive effect
