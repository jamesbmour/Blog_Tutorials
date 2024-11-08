###############################################################################
# SECTION 14: Cache
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

# clear cache button
if st.button("Clear Cache"):
    st.cache_data.clear()
    st.write("Cache cleared!")


# - `st.cache_data` stores the result of a function so that the next time you call
#   it with the same inputs, it doesn't need to rerun the function—it just returns
#   the stored result. This greatly reduces computation time and improves performance.
# - Ideal for functions like data loading where the input doesn't frequently change.
@st.cache_data
def load_data(nrows):
    time.sleep(2)  # Simulate a 2-second delay to represent an expensive computation.
    df = pd.DataFrame(np.random.randn(nrows, 3), columns=["A", "B", "C"])
    return df


# - When the "Load Data" button is pressed, it takes 2 seconds initially but then
#   loads instantly on subsequent clicks since the result is cached.
if st.button("Load Data"):
    data = load_data(1000)
    st.write(data)

st.write("Notice how the data loads quickly after the first time.")

# - Use Streamlit's time tracking to demonstrate the benefit of caching.
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
# SECTION 5: ADVANCED SESSION STATE WITH CALLBACKS
# - Using callback functions
# - Event handling with session state
# - Best practices for callbacks
###############################################################################
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
