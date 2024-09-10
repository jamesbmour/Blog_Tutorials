# Streamlit Part 3: Data Elements
import streamlit as st
import pandas as pd

# config for auto rerun
st.set_page_config(initial_sidebar_state="auto")

st.title("Streamlit Part 3: Data Elements")

# Example DataFrame
df = pd.DataFrame({
    "Column 1": [1, 2, 3, 4],
    "Column 2": [10, 20, 30, 40],
    "Column 3": [100, 200, 300, 400]
})

# st.dataframe
st.header("st.dataframe")

# st.table
st.header("st.table")

# st.json
st.header("st.json")

# st.column_config
st.header("st.column_config")

# st.pandas_profiling
st.header("st.pandas_profiling")

# st.data_editor
st.header("st.data_editor")

# st.metric
st.header("st.metric")
