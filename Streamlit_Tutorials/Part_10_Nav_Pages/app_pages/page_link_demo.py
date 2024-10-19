# app_pages/page_link_demo.py
import streamlit as st


def page_link():
    st.title("Using st.page_link")
    st.page_link("app_pages/intro.py", label="Go to Intro", icon="🏠")
    st.page_link("app_pages/page_link_demo.py", label="Refresh This Page", icon="🔄")
    st.page_link("https://www.streamlit.io/", label="Visit Streamlit", icon="🚀")


if __name__ == "__page__":
    page_link()
