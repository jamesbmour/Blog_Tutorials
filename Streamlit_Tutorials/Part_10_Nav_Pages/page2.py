import streamlit as st

st.title("Page 2")

st.write("This is Page 2.")

# Sidebar navigation
with st.sidebar:
    st.write("## Sidebar Navigation")
    page = st.radio("Go to", ["Main Page", "Page 1", "Page 2"])

    if page != "Page 2":
        st.switch_page(page)
# Buttons to switch pages
if st.button("Go back to Main Page"):
    st.switch_page("Main Page")

if st.button("Go to Page 1"):
    st.switch_page("Page 1")
