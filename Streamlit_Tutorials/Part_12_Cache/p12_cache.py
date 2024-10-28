import streamlit as st
import time
import pandas as pd
import numpy as np

st.title("Streamlit Caching and State Tutorial")

# Section 1: st.cache_data
st.header("1. st.cache_data")
st.write("st.cache_data is used for caching functions that return data.")


# Define a function to simulate a time-consuming data operation
@st.cache_data
def load_data(nrows):
    time.sleep(2)  # Simulate a 2-second delay
    df = pd.DataFrame(np.random.randn(nrows, 3), columns=["A", "B", "C"])
    return df


# Video Narration: "Let's demonstrate how st.cache_data works. We'll use it to cache a function that loads data."

if st.button("Load Data"):
    data = load_data(1000)
    st.write(data)

st.write("Notice how the data loads quickly after the first time.")

# Section 2: st.cache_resource
st.header("2. st.cache_resource")
st.write(
    "st.cache_resource is used for caching global resources like ML models or database connections."
)


# Define a function to simulate loading a large ML model
@st.cache_resource
def load_model():
    time.sleep(3)  # Simulate a 3-second delay for model loading
    return "Pretend this is a large ML model"


# Video Narration: "Now, let's see how st.cache_resource works. We'll use it to cache a simulated ML model."

if st.button("Load Model"):
    model = load_model()
    st.write("Model loaded:", model)

st.write(
    "The model loads quickly after the first time, and it's shared across all users."
)

# Section 3: Clearing Cache
st.header("3. Clearing Cache")

# Video Narration: "We can clear the cache for specific functions or all cached items."

if st.button("Clear Data Cache"):
    load_data.clear()
    st.write("Data cache cleared!")

if st.button("Clear All Caches"):
    st.cache_data.clear()
    st.cache_resource.clear()
    st.write("All caches cleared!")

# Section 4: Session State
st.header("4. Session State")
st.write("Session State allows you to store and persist state for each user session.")

# Video Narration: "Let's explore how to use Session State to maintain state across reruns."

# Initialize counter in session state
if "counter" not in st.session_state:
    st.session_state.counter = 0

# Display current counter value
st.write(f"Counter: {st.session_state.counter}")

# Button to increment counter
if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.rerun()

# Text input with session state
st.text_input("Enter your name", key="name")
st.write(f"Hello, {st.session_state.name}")

# Section 5: Callbacks with Session State
st.header("5. Callbacks with Session State")

# Video Narration: "We can use callbacks to update Session State when widget values change."


def increment_counter():
    st.session_state.counter += 1


st.button("Increment (with callback)", on_click=increment_counter)

# Section 6: Forms and Session State
st.header("6. Forms and Session State")

# Video Narration: "Forms can be used with Session State to batch inputs together."

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider", 0, 10, 5, key="form_slider")
    checkbox_val = st.checkbox("Form checkbox", key="form_checkbox")
    submitted = st.form_submit_button("Submit")

if submitted:
    st.write("Slider value:", st.session_state.form_slider)
    st.write("Checkbox value:", st.session_state.form_checkbox)

# Conclusion
st.header("Conclusion")
st.write(
    "This tutorial demonstrated Streamlit's caching mechanisms and session state management."
)
st.write(
    "Experiment with these features to create efficient and interactive Streamlit apps!"
)
