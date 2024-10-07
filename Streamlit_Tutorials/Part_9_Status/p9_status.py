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
st.write("### st.progress")
# Text to display with the progress bar
progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)  # Initialize the progress bar

# Simulate a long-running operation
for percent_complete in range(100):
    time.sleep(0.001)  # Simulate time delay
    my_bar.progress(percent_complete + 1, text=progress_text)  # Update the progress bar

# Wait for a second before clearing the progress bar
time.sleep(0.7)
# Clear the progress bar
my_bar.empty()

# Add a button to rerun the app to display the progress bar again
st.button("Rerun")

# st.status
st.write("### st.status")
# Display a success message with an icon
st.success("This is a success message!", icon="✅")

#  st.spinner
# Display a spinner while the operation is in progress
st.write("### st.spinner")
with st.spinner(
    "In progress..."
):  # Display a spinner while the operation is in progress
    time.sleep(2)  # Simulate a long-running operation
# Display a success message after the operation complete
st.success("Done!")

#  st.success
st.write("### st.success")
# Display a success message
st.success("This is a success message!")

#  st.error
st.write("### st.error")
# Display an error message
st.error("This is an error message!")

#  st.warning
st.write("### st.warning")
# Display a warning message
st.warning("This is a warning message!")

#  st.info
st.write("### st.info")
# Display an info message
st.info("This is an info message!")

#  st.exception
st.write("### st.exception")
try:
    raise Exception(
        "This is an exception!"
    )  # Raise an exception to demonstrate st.exception
except Exception as e:
    st.exception(e)  # Display the exception message

#  st.balloons
st.write("### st.balloons")
# Display balloons for a fun effect
st.balloons()

#  st.snow
st.write("### st.snow")
# Display snow for a festive effect
st.snow()
