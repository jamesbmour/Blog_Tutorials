# Streamlit Part 3: Data Elements
import streamlit as st
import pandas as pd

st.title("Streamlit Part 3: Data Elements")

# Creating a simple DataFrame for demonstration.
df = pd.DataFrame({
    "Column 1": [1, 2, 3, 4],
    "Column 2": [10, 20, 30, 40],
    "Column 3": [100, 200, 300, 400],
    "Column 4": [1000, 2000, 3000, 4000]

})

# st.dataframe
st.header("st.dataframe")
# Displays interactive dataframe in table form.
st.dataframe(df, width=500, height=200, hide_index=False)

# st.table
st.header("st.table")
# Differs from st.dataframe in that the table is static: its entire contents are laid out directly on the page.
st.table(df)

# st.json
st.header("st.json")
# Display an object or string as a pretty-printed, interactive JSON string.
st.json(
    df.to_json(orient="records")
    , expanded=True)

# st.data_editor
st.header("st.data_editor")
# Users can edit the data directly from the Streamlit interface.
st.data_editor(df)

# st.metric
st.header("st.metric")
# Displaying metrics with st.metric(). It can show the value and optionally a comparison to another value.
st.metric("Metric 1", 100, 5)
st.metric("Metric 2", 200, -3)
