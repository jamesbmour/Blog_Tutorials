###############################################################################
# SECTION 0: IMPORTS AND SETUP
# - Import required libraries (streamlit, time, pandas, numpy)
# - Essential packages for data manipulation and UI
###############################################################################
import streamlit as st
import time
import pandas as pd
import numpy as np

st.title("Streamlit Caching and State Tutorial")

###############################################################################
# SECTION 1: CACHING DATA WITH ST.CACHE_DATA
# - Introduction to data caching
# - Demonstration of caching DataFrame operations
# - Performance improvement example
###############################################################################
st.header("1. st.cache_data")
st.write("st.cache_data is used for caching functions that return data.")


@st.cache_data
def load_data(nrows):
    time.sleep(2)  # Simulate a 2-second delay
    df = pd.DataFrame(np.random.randn(nrows, 3), columns=["A", "B", "C"])
    return df


if st.button("Load Data"):
    data = load_data(1000)
    st.write(data)

st.write("Notice how the data loads quickly after the first time.")

###############################################################################
# SECTION 2: RESOURCE CACHING WITH ST.CACHE_RESOURCE
# - Caching for global resources
# - Use cases for ML models and database connections
# - Shared resource demonstration
###############################################################################
st.header("2. st.cache_resource")
st.write(
    "st.cache_resource is used for caching global resources like ML models or database connections."
)


@st.cache_resource
def load_model():
    time.sleep(3)  # Simulate a 3-second delay for model loading
    return "Pretend this is a large ML model"


if st.button("Load Model"):
    model = load_model()
    st.write("Model loaded:", model)

st.write(
    "The model loads quickly after the first time, and it's shared across all users."
)

###############################################################################
# SECTION 3: CACHE MANAGEMENT
# - Methods to clear specific caches
# - Clearing all cached items
# - When to clear cache
###############################################################################
st.header("3. Clearing Cache")

if st.button("Clear Data Cache"):
    load_data.clear()
    st.write("Data cache cleared!")

if st.button("Clear All Caches"):
    st.cache_data.clear()
    st.cache_resource.clear()
    st.write("All caches cleared!")

###############################################################################
# SECTION 4: INTRODUCTION TO SESSION STATE
# - Basic session state concepts
# - State persistence across reruns
# - Counter example implementation
###############################################################################
st.header("4. Session State")
st.write("Session State allows you to store and persist state for each user session.")

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.write(f"Counter: {st.session_state.counter}")

if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.rerun()

st.text_input("Enter your name", key="name")
st.write(f"Hello, {st.session_state.name}")

###############################################################################
# SECTION 5: ADVANCED SESSION STATE WITH CALLBACKS
# - Using callback functions
# - Event handling with session state
# - Best practices for callbacks
###############################################################################
st.header("5. Callbacks with Session State")


def increment_counter():
    st.session_state.counter += 1


st.button("Increment (with callback)", on_click=increment_counter)

###############################################################################
# SECTION 6: FORMS AND SESSION STATE INTEGRATION
# - Creating forms with multiple inputs
# - Handling form submissions
# - Accessing form data through session state
###############################################################################
st.header("6. Forms and Session State")

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider", 0, 10, 5, key="form_slider")
    checkbox_val = st.checkbox("Form checkbox", key="form_checkbox")
    submitted = st.form_submit_button("Submit")

if submitted:
    st.write("Slider value:", st.session_state.form_slider)
    st.write("Checkbox value:", st.session_state.form_checkbox)
