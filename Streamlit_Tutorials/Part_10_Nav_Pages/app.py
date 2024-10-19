# app.py
import streamlit as st

# Page Navigation
# Page Definitions for the Navigation Demo App
pages = [
    st.Page("app_pages/intro.py", title="Introduction", icon="👋"),
    st.Page("app_pages/navigation_intro.py", title="st.navigation", icon="🧭"),
    st.Page("app_pages/page_link_demo.py", title="st.page_link", icon="🔗"),
    st.Page("app_pages/switch_page_demo.py", title="st.switch_page", icon="🔀"),
]

# Adding pages to the sidebar navigation using st.navigation
pg = st.navigation(pages, position="sidebar", expanded=True)
# Running the app
pg.run()
