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
    st.session_state.counter = 0  # Using attribute syntax

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


def update_input():
    st.session_state.input_text = st.session_state.text_input
    st.info(f"Input Text Updated: {st.session_state.input_text}")


st.text_input("Enter some text:", key="text_input", on_change=update_input)

st.markdown("---")

# 3. Delete Items from Session State
st.header("3. Delete Items from Session State")

# Button to reset 'counter' and 'input_text'
if st.button("Reset Counter and Input Text"):
    if "counter" in st.session_state:
        del st.session_state.counter
    if "input_text" in st.session_state:
        del st.session_state["input_text"]
    st.success("Session state variables 'counter' and 'input_text' have been deleted.")

st.markdown("---")

# 4. Serializable Session State
st.header("4. Serializable Session State")

if st.button("Store Unserializable Object"):
    try:
        st.session_state.unserializable = lambda x: x
        st.success("Stored an unserializable object in session state.")
    except Exception as e:
        st.error(f"Error: {e}")

# Display the unserializable object if it exists
if "unserializable" in st.session_state:
    st.write("Session state contains an unserializable object.")
else:
    st.write("No unserializable object stored in session state.")

st.markdown("---")

# 5. Session State and Widget Association
st.header("5. Session State and Widget Association")

st.text_input("Your name:", key="name")
st.write("Session State 'name':", st.session_state.get("name", ""))

st.markdown("---")

# 6. Forms and Callbacks
st.header("6. Forms and Callbacks")


def form_callback():
    st.success("Form Submitted!")
    st.write("Slider Value:", st.session_state.my_slider)
    st.write("Checkbox Value:", st.session_state.my_checkbox)


with st.form(key="my_form"):
    st.slider("My slider", 0, 10, 5, key="my_slider")
    st.checkbox("Check me", key="my_checkbox")
    st.form_submit_button("Submit", on_click=form_callback)

st.markdown("---")

# 7. Caveats and Limitations
st.header("7. Caveats and Limitations")

st.subheader("Attempting to Modify Widget Value After Instantiation")

st.slider("Immutable Slider", 0, 100, 50, key="immutable_slider")

try:
    # Attempt to modify the slider value programmatically
    st.session_state.immutable_slider = 75
    st.success("Immutable slider value set to 75.")
except Exception as e:
    st.error(f"Error: {e}")

st.subheader("Setting State of Button-like Widgets")

try:
    if "my_button" not in st.session_state:
        st.session_state.my_button = False  # Initialize if not present
    # Button state cannot be set directly; this will raise an error if attempted improperly
    button_clicked = st.button("My Button", key="my_button")
    if button_clicked:
        st.session_state.my_button = True
        st.info("Button was clicked!")
except Exception as e:
    st.error(f"Error: {e}")
