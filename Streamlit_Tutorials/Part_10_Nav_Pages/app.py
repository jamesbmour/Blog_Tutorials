# app.py
import streamlit as st

# Page Navigation
# Page Definitions for the Navigation Demo App
pages = [
    st.Page("pages/intro.py", title="Introduction", icon="👋"),
    st.Page("pages/navigation_intro.py", title="st.navigation", icon="🧭"),
    st.Page("pages/page_link_demo.py", title="st.page_link", icon="🔗"),
    st.Page("pages/switch_page_demo.py", title="st.switch_page", icon="🔀"),
]

# Adding pages to the sidebar navigation using st.navigation
pg = st.navigation(pages, position="sidebar", expanded=True)

# Running the app
pg.run()
