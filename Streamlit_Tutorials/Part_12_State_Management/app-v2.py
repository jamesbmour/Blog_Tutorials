import streamlit as st

st.title("Streamlit Session State Management Tutorial")

st.header("1. Initialize Values in Session State")

# Initialize session state variables
if "counter" not in st.session_state:
    st.session_state.counter = 0  # Using attribute syntax

if "input_text" not in st.session_state:
    st.session_state["input_text"] = ""  # Using dictionary syntax

st.write("Counter:", st.session_state.counter)
st.write("Input Text:", st.session_state.input_text)

st.subheader("Increment Counter Example")

# Button to increment the counter
if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.write("Counter incremented!")

st.write("Updated Counter:", st.session_state.counter)

st.header("2. Update Session State with Callbacks")


# Callback function to update input_text in session state
def update_input():
    st.session_state.input_text = st.session_state.text_input


# Text input with callback
st.text_input("Enter some text:", key="text_input", on_change=update_input)

st.write("Updated Input Text:", st.session_state.input_text)

st.header("3. Delete Items from Session State")

if st.button("Reset Counter and Input Text"):
    # Delete specific items from session state
    del st.session_state.counter
    del st.session_state["input_text"]
    st.write("Session state variables 'counter' and 'input_text' have been deleted.")

st.header("4. Serializable Session State")

st.write(
    """
By default, Streamlit's session state allows you to store any Python object.
However, if you enable `enforceSerializableSessionState`, only pickle-serializable objects are allowed.
"""
)

if st.button("Store Unserializable Object"):
    try:
        # Attempt to store an unserializable object (lambda function)
        st.session_state.unserializable = lambda x: x
        st.write("Stored an unserializable object in session state.")
    except Exception as e:
        st.write(f"Error: {e}")

st.header("5. Session State and Widget Association")

# Widgets with a key automatically sync with session state
st.text_input("Your name:", key="name")
st.write("Session State 'name':", st.session_state.name)

st.header("6. Forms and Callbacks")


# Callback function for form submission
def form_callback():
    st.write("Slider Value:", st.session_state.my_slider)
    st.write("Checkbox Value:", st.session_state.my_checkbox)


with st.form(key="my_form"):
    st.slider("My slider", 0, 10, 5, key="my_slider")
    st.checkbox("Check me", key="my_checkbox")
    st.form_submit_button("Submit", on_click=form_callback)

st.header("7. Caveats and Limitations")

st.write(
    """
- Only `st.form_submit_button` supports callbacks within forms.
- Modifying the value of a widget via session state after it's instantiated will raise an exception.
"""
)

st.subheader("Attempting to Modify Widget Value After Instantiation")

# Instantiate a slider widget
st.slider("Immutable Slider", 0, 100, 50, key="immutable_slider")

try:
    # Attempt to modify the widget's value via session state
    st.session_state.immutable_slider = 75
except Exception as e:
    st.write(f"Error: {e}")

st.write("Session State 'immutable_slider':", st.session_state.immutable_slider)

st.subheader("Setting State of Button-like Widgets")

try:
    if "my_button" not in st.session_state:
        # Attempt to set the state of a button-like widget (not allowed)
        st.session_state.my_button = True
    st.button("My Button", key="my_button")
except Exception as e:
    st.write(f"Error: {e}")
