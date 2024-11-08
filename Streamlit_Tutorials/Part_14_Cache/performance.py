import time
import pandas as pd
import streamlit as st


# Function to simulate a slow loading process
def slow_load_data():
    time.sleep(3)  # Simulate delay
    data = {
        "A": list(range(1, 11)),
        "B": [x**2 for x in range(1, 11)],
        "C": [x**3 for x in range(1, 11)],
    }
    df = pd.DataFrame(data)
    return df


# Create two columns
col1, col2 = st.columns(2)

# Without Caching Column
with col1:
    st.header("Without Caching")
    st.write("Loading data without caching... this will take some time.")
    start_time = time.time()
    data_without_cache = slow_load_data()
    end_time = time.time()
    st.dataframe(data_without_cache)
    st.write(f"Time taken: {end_time - start_time:.2f} seconds")


# Load data with caching using st.cache_data
@st.cache_data
def cached_load_data():
    return slow_load_data()


# With Caching Column
with col2:
    st.header("With Caching")
    st.write(
        "Loading data with caching... first load will take some time, but subsequent loads will be faster."
    )
    start_time = time.time()
    data_with_cache = cached_load_data()
    end_time = time.time()
    st.dataframe(data_with_cache)
    st.write(f"Time taken: {end_time - start_time:.2f} seconds")
    # Button to reload data and demonstrate caching effect
    if st.button("Reload Data with Caching"):
        start_time = time.time()
        data_with_cache = cached_load_data()
        end_time = time.time()
        st.dataframe(data_with_cache)
        st.write(f"Time taken: {end_time - start_time:.2f} seconds")
