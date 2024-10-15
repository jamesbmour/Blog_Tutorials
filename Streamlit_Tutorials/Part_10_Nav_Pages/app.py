# app.py
import streamlit as st

pages = [
    st.Page("pages/intro.py", title="Introduction", icon="👋"),
    st.Page("pages/navigation_intro.py", title="st.navigation", icon="🧭"),
    st.Page("pages/page_link_demo.py", title="st.page_link", icon="🔗"),
    st.Page("pages/switch_page_demo.py", title="st.switch_page", icon="🔀"),
]

pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()

# Common elements (footer)
st.sidebar.markdown("---")
st.sidebar.info("This is a tutorial on Streamlit page navigation.")
