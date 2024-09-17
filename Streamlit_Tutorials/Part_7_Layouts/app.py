import streamlit as st
import time

# Set the page configuration
st.set_page_config(
    page_title="Streamlit Layouts Tutorial",
    page_icon=":art:",
    initial_sidebar_state="collapsed",
)

st.title("Streamlit Layouts Tutorial")

# 1. Columns
st.header("Columns")
st.write("Using `st.columns()` to create columns.")

# 2. Container
st.header("Container")
st.write("Using `st.container()` to group elements together.")

# 3. Empty
st.header("Empty")
st.write("Using `st.empty()` as a placeholder for updating content.")


# 4. Expander
st.header("Expander")
st.write("Using `st.expander()` to hide/show content.")


# 5. Form
st.header("Form")
st.write("Using `st.form()` to group input widgets with a submit button.")

# 6. Sidebar
st.header("Sidebar")
st.write("Using `st.sidebar` to add content to the sidebar.")


# 7. Tabs
st.header("Tabs")
st.write("Using `st.tabs()` to create tabbed sections.")
