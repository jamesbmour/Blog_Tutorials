import streamlit as st

st.title("Streamlit Session State Management Tutorial")

st.header("1. Add Statefulness to Apps")

st.write(
    """
Streamlit creates a new session for each browser tab that connects to the app.
By default, Streamlit reruns your script from top to bottom every time you interact with your app.
Each rerun is a blank slate: no variables are shared between runs.

**Session State** allows you to share variables between reruns for each user session.
In addition to storing and persisting state, Streamlit also allows you to manipulate state using callbacks.
Session state also persists across apps inside a multipage app.
"""
)

st.subheader("Build a Counter")

# Initialize 'count' in session state
if "count" not in st.session_state:
    st.session_state.count = 0

st.write("Count:", st.session_state.count)

# Button to increment the counter
if st.button("Increment"):
    st.session_state.count += 1
    st.write("Counter incremented!")

st.write("Updated Count:", st.session_state.count)

st.header("2. Initialize Values in Session State")

# Initialize session state variables
if "counter" not in st.session_state:
    st.session_state.counter = 0

if "input_text" not in st.session_state:
    st.session_state["input_text"] = ""

st.write("Counter:", st.session_state.counter)
st.write("Input Text:", st.session_state.input_text)

st.header("3. Reads and Updates")

st.subheader("Read Session State")

st.write("Counter:", st.session_state.counter)
st.write("Input Text:", st.session_state.input_text)

st.subheader("Update Session State")

# Button to increment the counter
if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.write("Counter incremented!")

st.write("Updated Counter:", st.session_state.counter)

st.header("4. Update Session State with Callbacks")


# Callback function to update input_text in session state
def update_input():
    st.session_state.input_text = st.session_state.text_input


# Text input with callback
st.text_input("Enter some text:", key="text_input", on_change=update_input)

st.write("Updated Input Text:", st.session_state.input_text)

st.header("5. Advanced Concepts")

st.subheader("Session State and Widget State Association")

st.write(
    """
Session State provides the functionality to store variables across reruns.
Widget state (i.e., the value of a widget) is also stored in a session.
For simplicity, Streamlit unifies this information in one place—the Session State.
This convenience feature makes it super easy to read or write to the widget's state anywhere in the app's code.
Session State variables mirror the widget value using the `key` argument.
"""
)

st.write("Example with Temperature Slider:")

if "celsius" not in st.session_state:
    # Set the initial default value of the slider widget
    st.session_state.celsius = 50.0

# Slider widget associated with session state
st.slider("Temperature in Celsius", min_value=-100.0, max_value=100.0, key="celsius")

# Accessing the value from session state
st.write("Current Temperature in Celsius:", st.session_state.celsius)

st.header("6. Delete Items from Session State")

if st.button("Reset All Session State Variables"):
    # Clear all items from session state
    st.session_state.clear()
    st.write("All session state variables have been reset.")

st.header("7. Serializable Session State")

st.write(
    """
By default, Streamlit's session state allows you to persist any Python object for the duration of the session,
irrespective of the object's pickle-serializability. However, some execution environments may require serializing
all data in session state. To enforce serializability, you can enable `enforceSerializableSessionState` in the
Streamlit configuration.

**Note:** When this option is enabled, attempting to store an unserializable object (like a lambda function) in
session state will raise an exception.
"""
)

if st.button("Store Unserializable Object"):
    try:
        # Attempt to store an unserializable object (lambda function)
        st.session_state.unserializable = lambda x: x
        st.write("Stored an unserializable object in session state.")
    except Exception as e:
        st.write(f"Error: {e}")

st.header("8. Forms and Callbacks")


# Callback function for form submission
def form_callback():
    st.write("Slider Value:", st.session_state.my_slider)
    st.write("Checkbox Value:", st.session_state.my_checkbox)


with st.form(key="my_form"):
    st.slider("My slider", 0, 10, 5, key="my_slider")
    st.checkbox("Check me", key="my_checkbox")
    st.form_submit_button("Submit", on_click=form_callback)

st.header("9. Caveats and Limitations")

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
