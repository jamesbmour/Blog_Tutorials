# app.py
import streamlit as st

pages = [
    st.Page("app_pages/intro.py", title="Introduction", icon="👋"),
    st.Page("app_pages/navigation_intro.py", title="st.navigation", icon="🧭"),
    st.Page("app_pages/page_link_demo.py", title="st.page_link", icon="🔗"),
    st.Page("app_pages/switch_page_demo.py", title="st.switch_page", icon="🔀"),
]

pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()
