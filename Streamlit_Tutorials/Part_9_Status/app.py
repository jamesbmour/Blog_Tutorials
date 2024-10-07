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
# Text to display with the progress bar
progress_text = "Operation in progress. Please wait."
# Initialize the progress bar
my_bar = st.progress(value=0, text=progress_text)

# Simulate a long-running operation
for percent_complete in range(100):
    # Simulate time delay
    time.sleep(0.001)
    # Update the progress bar
    my_bar.progress(percent_complete + 1, text=progress_text)

# Wait for a second before clearing the progress bar
time.sleep(0.5)
# Clear the progress bar
my_bar.empty()

# Add a button to rerun the app to display the progress bar again
st.button("Rerun")

# Initialize the progress bar
st.write("### st.success")
st.success("This is a status message!", icon="✅")

# Display a success message with an icon
st.write("### st.spinner")
with st.spinner(
    "In progress..."
):  # Display a spinner while the operation is in progress
    time.sleep(1.5)  # Simulate a long-running operation
# Display a success message after the operation complete
st.success("Done!")

# Display a success message after the operation completes
st.write("### st.error")
# Display an error message
st.error("This is an error message!")

# Display an error message
st.write("### st.warning")
# Display a warning message
st.warning("This is a warning message!")

# Display a warning message
st.write("### st.info")
# Display an info message
st.info("This is an info message!")

# Display an info message
st.write("### st.exception")
try:
    raise Exception(
        "This is an exception!"
    )  # Raise an exception to demonstrate st.exception
except Exception as e:
    # Display the exception message
    st.exception(e)
#  st.balloons
st.write("### st.balloons")
bbtn = st.button("Click me to display balloons")
if bbtn:
    # Display balloons for a fun effect
    st.balloons()


# Display an exception message
st.write("### st.snow")

snow_btn = st.button("Click me to display snow")
if snow_btn:
    # Display snow for a festive effect
    st.snow()
