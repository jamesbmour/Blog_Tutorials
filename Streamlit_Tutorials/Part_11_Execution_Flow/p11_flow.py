import streamlit as st
import time

# -------------------------------
# Streamlit Execution Flow Elements Tutorial
# -------------------------------

# Set the title of the app
st.title("Streamlit Execution Flow Elements Tutorial")

# -------------------------------
# 1. Using `st.dialog`
# -------------------------------
st.header("1. st.dialog")
st.write("`st.dialog` creates a modal dialog that can be triggered by user actions.")


# Define a dialog function using the @st.dialog decorator
@st.dialog("Example Dialog")
def show_dialog():
    """
    This function creates a modal dialog with a text input and a submit button.
    When the user submits, it saves the input to Session State and reruns the app to close the dialog.
    """
    st.write("This is a modal dialog.")
    name = st.text_input("Enter your name")
    if st.button("Submit"):
        # Store the entered name in Session State
        st.session_state.dialog_name = name
        # Rerun the app to close the dialog
        st.rerun()


# Button to open the dialog
if st.button("Open Dialog"):
    show_dialog()

# Display a greeting if the user has submitted their name
if "dialog_name" in st.session_state:
    st.write(f"Hello, {st.session_state.dialog_name}!")

# -------------------------------
# 2. Using `st.fragment`
# -------------------------------
st.header("2. st.fragment")
st.write("`st.fragment` allows a part of your app to rerun independently.")


@st.fragment
def update_counter():
    """
    This fragment maintains its own counter in Session State.
    It increments the counter and displays it.
    The button within the fragment triggers a rerun of the fragment only.
    """
    if "counter" not in st.session_state:
        st.session_state.counter = 0

    st.write(f"Counter: {st.session_state.counter}")

    if st.button("Increment (Fragment Rerun)"):
        st.session_state.counter += 1
        # Rerun only the fragment
        st.rerun(scope="fragment")


# Execute the fragment
update_counter()

# Button to trigger a full app rerun
if st.button("Full App Rerun"):
    st.rerun()

# Execute the fragment
update_counter()


# -------------------------------
# 3. Using `st.rerun`
# -------------------------------
st.header("3. st.rerun")
st.write("`st.rerun` allows you to rerun the entire app or just a fragment.")

# Display the current counter value
st.write("Current counter value:", st.session_state.get("counter", 0))

# Button to increment the counter and rerun the app
if st.button("Increment and Rerun"):
    st.session_state.counter = st.session_state.get("counter", 0) + 1
    st.rerun()

st.write("This message appears after rerun.")

# -------------------------------
# 4. Using `st.stop`
# -------------------------------
st.header("4. st.stop")
st.write("`st.stop` halts the execution of the script at that point.")

# Checkbox to trigger stopping the script
if st.checkbox("Stop execution"):
    st.warning("Execution will stop here.")
    st.stop()  # Stop execution if checkbox is selected

# This part only executes if the script wasn't stopped
st.success("This will only show if execution wasn't stopped.")

# -------------------------------
# 5. Using `st.form` and `st.form_submit_button`
# -------------------------------
st.header("5. st.form and st.form_submit_button")
st.write(
    "`st.form` groups inputs together, and `st.form_submit_button` submits the form."
)

# Create a form using with notation
with st.form("example_form"):
    st.write("Inside the form:")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120)
    # Submit button for the form
    submitted = st.form_submit_button("Submit Form")
    if submitted:
        # Store form data in Session State
        st.session_state.form_data = {"name": name, "age": age}
        st.success("Form submitted successfully!")

# Display submitted form data if available
if "form_data" in st.session_state:
    st.write("### Submitted Data:")
    st.write(f"**Name:** {st.session_state.form_data['name']}")
    st.write(f"**Age:** {st.session_state.form_data['age']}")

# -------------------------------
# Bonus: Combining Elements
# -------------------------------
st.header("Bonus: Combining Elements")
st.write("Let's combine some of these elements in a more complex example.")


# Define a complex dialog that includes a form
@st.dialog("Complex Dialog")
def complex_dialog():
    """
    This dialog contains a form with name and age inputs.
    Upon submission, it saves the data to Session State and reruns the app to close the dialog.
    """
    with st.form("dialog_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, max_value=120)
        submitted = st.form_submit_button("Submit")

    if submitted:
        # Store dialog results in Session State
        st.session_state.dialog_result = {"name": name, "age": age}
        # Rerun the app to close the dialog
        st.rerun()


# Button to open the complex dialog
if st.button("Open Complex Dialog"):
    complex_dialog()

# Display the dialog result if available
if "dialog_result" in st.session_state:
    st.write("### Dialog Result:")
    st.write(f"**Name:** {st.session_state.dialog_result['name']}")
    st.write(f"**Age:** {st.session_state.dialog_result['age']}")
    # Button to clear the result and reset the state
    if st.button("Clear Result"):
        del st.session_state.dialog_result
        st.rerun()
