import streamlit as st
import pandas as pd

# config for wide mode and auto rerun
st.set_page_config(layout="wide", initial_sidebar_state="auto")

# Set the title of the app using st.title(). This serves as the main heading of your Streamlit application.
st.title("Streamlit Part 3: Data Elements")

# st.dataframe: This element allows you to display a pandas DataFrame with features like sorting and scrolling.
# It's interactive, so users can explore the data within the app.
st.header("st.dataframe")

# Creating a simple DataFrame for demonstration.
df = pd.DataFrame({
    "Column 1": [1, 2, 3, 4],
    "Column 2": [10, 20, 30, 40],
    "Column 3": [100, 200, 300, 400]
})

# Displays interactive dataframe in table form.
st.dataframe(df, width=500, height=200, hide_index=False)

# st.table: This function displays a static table with no interactive features.
# It's great for showing a snapshot of your data in a simple and clean format.
st.header("st.table")

# Differs from st.dataframe in that the table is static: its entire contents are laid out directly on the page.
st.table(df)

# st.json: This element allows you to display JSON data in a formatted and readable manner.
# It's useful for working with APIs or when you want to show raw data in JSON format.
st.header("st.json")

# Display an object or string as a pretty-printed, interactive JSON string.
st.json({
    "Column 1": [1, 2, 3, 4],
    "Column 2": [10, 20, 30, 40],
    "Column 3": [100, 200, 300, 400]
}, expanded=True)

# st.column_config: This element allows you to configure the layout of your app's columns.
# It's useful when you want to customize the width or alignment of columns.
st.header("st.column_config")

# Example: This would be where you configure column width or other properties.
# Note that Streamlit's layout options are typically handled with st.columns(), but
# this placeholder shows how to introduce such a concept.
st.write("This is a wide column")
st.write("This is a narrow column")
st.column_config = {"wideMode": True}  # This line is a placeholder as Streamlit doesn't directly support this yet.

# st.pandas_profiling: This is an external tool integrated with Streamlit to create an in-depth report of a DataFrame.
# It generates statistics, visualizations, and summaries automatically.
# st.header("st.pandas_profiling")
# st.write("Pandas Profiling using st.pandas_profiling()")
# from pandas_profiling import ProfileReport
# profile = ProfileReport(df, title="Pandas Profiling Report")
# Displaying the profile report using st.write(). Note that the display of ProfileReport in Streamlit requires using
# st.components.v1 or exporting as HTML.
# st.write(profile)

# st.data_editor: This function creates an interactive data editor within the app.
st.header("st.data_editor")
# Users can edit the data directly from the Streamlit interface.
st.data_editor(df)

# st.metric: This element is used to display a single number along with optional
# delta values, making it ideal for showing KPIs or summary statistics.
st.header("st.metric")

# Displaying metrics with st.metric(). It can show the value and optionally a comparison to another value.
st.metric("Metric 1", 100, 5)
st.metric("Metric 2", 200, -3)
