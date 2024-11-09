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
###############################################################################
st.header("1. st.cache_data")
# clear cache button
if st.button("Clear Cache"):
    st.cache_data.clear()
    st.write("Cache cleared!")


@st.cache_data
def load_data(nrows):
    time.sleep(2)  # Simulate a 2-second delay to represent an expensive computation.
    df = pd.DataFrame(np.random.randn(nrows, 3), columns=["A", "B", "C"])
    return df


if st.button("Load Data with Timer"):
    start_time = time.time()
    data = load_data(1000)
    end_time = time.time()
    st.write(data)
    st.write(f"Data loaded in {end_time - start_time:.2f} seconds.")


###############################################################################
# SECTION 2: RESOURCE CACHING WITH ST.CACHE_RESOURCE
###############################################################################
st.header("2. st.cache_resource")


@st.cache_resource(ttl=2)
def load_model():
    time.sleep(3)  # Simulate a 3-second delay for model loading
    return "Pretend this is a large ML model"


if st.button("Load Model with Timer"):
    start_time = time.time()
    model = load_model()
    end_time = time.time()
    st.write("Model loaded:", model)
    st.write(f"Model loaded in {end_time - start_time:.2f} seconds.")

###############################################################################
# SECTION 3: CACHE MANAGEMENT
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
# SECTION 5: ADVANCED SESSION STATE WITH CALLBACKS
###############################################################################
st.subheader("Advance Usage:")


@st.cache_data(ttl=3600)  # 👈 Cache data for 1 hour (=3600 seconds)
def get_api_data():
    data = load_data(1000)
    return data


@st.cache_data(max_entries=1000)  # 👈 Maximum 1000 entries in the cache
def get_large_array(seed):
    np.random.seed(seed)
    arr = np.random.rand(100000)
    return arr
