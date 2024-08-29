# Streamlit Part 3: Data Elements
import streamlit as st
import pandas as pd
st.title("Streamlit Tutorials")


# st.dataframe
st.header("st.dataframe")
st.write("Dataframe using st.dataframe()")

df = pd.DataFrame({
    "Column 1": [1, 2, 3, 4],
    "Column 2": [10, 20, 30, 40]
})
st.dataframe(df)

# st.table
st.header("st.table")
st.write("Table using st.table()")
st.table(df)

# st.json
st.header("st.json")
st.write("JSON using st.json()")
st.json({
    "Column 1": [1, 2, 3, 4],
    "Column 2": [10, 20, 30, 40]
})

# st.column_config
st.header("st.column_config")
st.write("Column Configuration using st.column_config()")
st.write("This is a wide column")
st.write("This is a narrow column")
st.column_config = {"wideMode": True}


# st.pandas_profiling
st.header("st.pandas_profiling")
st.write("Pandas Profiling using st.pandas_profiling()")
from pandas_profiling import ProfileReport
profile = ProfileReport(df, title="Pandas Profiling Report")
st.write(profile)

#st.data_editor
st.header("st.data_editor")
st.write("Data Editor using st.data_editor()")
st.data_editor(df)

# st.metric
st.header("st.metric")
st.write("Metric using st.metric()")
st.metric("Metric 1", 100)
st.metric("Metric 2", 200)






