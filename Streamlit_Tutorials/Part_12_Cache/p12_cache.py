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


# Explain caching to the audience:
# - `st.cache_data` stores the result of a function so that the next time you call
#   it with the same inputs, it doesn't need to rerun the function—it just returns
#   the stored result. This greatly reduces computation time and improves performance.
# - Ideal for functions like data loading where the input doesn't frequently change.
@st.cache_data
def load_data(nrows):
    time.sleep(2)  # Simulate a 2-second delay to represent an expensive computation.
    df = pd.DataFrame(np.random.randn(nrows, 3), columns=["A", "B", "C"])
    return df


# Demonstrate caching benefits:
# - When the "Load Data" button is pressed, it takes 2 seconds initially but then
#   loads instantly on subsequent clicks since the result is cached.
if st.button("Load Data"):
    data = load_data(1000)
    st.write(data)

st.write("Notice how the data loads quickly after the first time.")

# Example showing performance improvement
# - Use Streamlit's time tracking to demonstrate the benefit of caching.
import time

if st.button("Load Data with Timer"):
    start_time = time.time()
    data = load_data(1000)
    end_time = time.time()
    st.write(data)
    st.write(f"Data loaded in {end_time - start_time:.2f} seconds.")
    # On first run, it will take approximately 2 seconds. On subsequent runs, it should be almost instant.

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


# Explain the difference between `st.cache_data` and `st.cache_resource`:
# - `st.cache_resource` is better suited for objects that are shared across sessions
#   (e.g., ML models, database connections) as it ensures that the resource is only
#   loaded once, saving both time and memory.
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

# Example showing performance improvement for resource caching
if st.button("Load Model with Timer"):
    start_time = time.time()
    model = load_model()
    end_time = time.time()
    st.write("Model loaded:", model)
    st.write(f"Model loaded in {end_time - start_time:.2f} seconds.")
    # Initially takes around 3 seconds, subsequent calls should be almost instant.

###############################################################################
# SECTION 3: CACHE MANAGEMENT
# - Methods to clear specific caches
# - Clearing all cached items
# - When to clear cache
###############################################################################
st.header("3. Clearing Cache")

# Important notes for your audience:
# - Cache management is critical when data changes frequently or to troubleshoot.
# - Clearing cache helps ensure the most up-to-date data is used.

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

# Explain what Session State is:
# - It keeps data in memory for a particular user's session, allowing for persistence
#   of variables between reruns (e.g., counter, user input).
# - This is especially helpful for creating interactive web applications.
if "counter" not in st.session_state:
    st.session_state.counter = 0

st.write(f"Counter: {st.session_state.counter}")

# Demonstrate state persistence:
# - Every time the "Increment Counter" button is clicked, the counter value is increased
#   and kept across reruns.
if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.rerun()

# Using input widgets with Session State:
# - Session State can also store user inputs for future use.
st.text_input("Enter your name", key="name")
st.write(f"Hello, {st.session_state.name}")

###############################################################################
# SECTION 5: ADVANCED SESSION STATE WITH CALLBACKS
# - Using callback functions
# - Event handling with session state
# - Best practices for callbacks
###############################################################################
st.header("5. Callbacks with Session State")


# Callback explanation:
# - Callback functions are executed after an event (e.g., clicking a button).
# - Useful to modify session state variables or trigger specific actions.
def increment_counter():
    st.session_state.counter += 1


# Demonstrate using callbacks:
# - The "Increment (with callback)" button uses a callback function to increment
#   the counter value without a full rerun.
st.button("Increment (with callback)", on_click=increment_counter)

###############################################################################
# SECTION 6: FORMS AND SESSION STATE INTEGRATION
# - Creating forms with multiple inputs
# - Handling form submissions
# - Accessing form data through session state
###############################################################################
st.header("6. Forms and Session State")

# Forms explanation:
# - Forms in Streamlit help bundle multiple widgets together for a cleaner user experience.
# - Submission of forms can trigger data processing, and inputs are accessible via Session State.
with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider", 0, 10, 5, key="form_slider")
    checkbox_val = st.checkbox("Form checkbox", key="form_checkbox")
    submitted = st.form_submit_button("Submit")

if submitted:
    # After form submission, the state of the widgets is saved in `st.session_state`.
    st.write("Slider value:", st.session_state.form_slider)
    st.write("Checkbox value:", st.session_state.form_checkbox)


# Example 1: Hashing a custom class
st.subheader("Advance Usage:")

st.write("#### The ttl (time-to-live) parameter")


@st.cache_data(ttl=3600)  # 👈 Cache data for 1 hour (=3600 seconds)
def get_api_data():
    data = load_data(1000)
    return data


st.write("The max_entries parameter")


@st.cache_data(max_entries=1000)  # 👈 Maximum 1000 entries in the cache
def get_large_array(seed):
    np.random.seed(seed)
    arr = np.random.rand(100000)
    return arr


# Excluding input parameters

st.write("#### Excluding input parameters")


@st.cache_data(ignore_hash=True)
def get_random_number(lower, upper):
    return np.random.randint(lower, upper)
