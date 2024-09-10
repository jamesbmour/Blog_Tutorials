# Streamlit Part 4: Inputs in Streamlit
import streamlit as st

# set config for wide mode and auto rerun
st.set_page_config(layout="wide")

# Set the title of the app
st.title("Streamlit Part 4: Inputs in Streamlit")

# Create columns for better UI
col1, col2 = st.columns(2)

# Column 1
with col1:
    st.subheader("Col 1")


# Column 2
with col2:
    st.subheader("Col 2")