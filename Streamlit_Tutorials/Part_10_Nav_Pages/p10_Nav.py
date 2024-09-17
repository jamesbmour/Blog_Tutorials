import streamlit as st

st.set_page_config(
    page_title="Streamlit Part 10: Navigation Pages",
    page_icon="🌟",
)

st.title("Streamlit Part 10: Navigation and Pages")

st.write("### Navigation")

st.write("Use the sidebar or buttons below to navigate between pages.")

# Sidebar navigation
with st.sidebar:
    st.write("## Sidebar Navigation")
    page = st.radio("Go to", ["Main Page", "Page 1", "Page 2"])

    if page == "Main Page":
        st.experimental_set_query_params()  # Stay on the main page
    else:
        st.switch_page(page)

# Buttons to switch pages
st.write("### st.switch_page")

if st.button("Go to Page 1"):
    st.switch_page("Page 1")

if st.button("Go to Page 2"):
    st.switch_page("Page 2")

# Links to other pages
st.write("### st.set_page_link")

st.markdown("[Go to Page 1](./Page%201)")
st.markdown("[Go to Page 2](./Page%202)")
