# pages/page_link_demo.py
import streamlit as st


def page():
    st.title("Using st.page_link")
    st.write(
        "`st.page_link` allows you to create custom navigation links within your app."
    )
    st.code(
        """
st.page_link("pages/intro.py", label="Go to Intro", icon="🏠")
st.page_link("pages/page1.py", label="Visit Page 1", icon="1️⃣")
    """,
        language="python",
    )
    st.write("Let's try it out:")
    st.page_link("pages/intro.py", label="Go to Intro", icon="🏠")
    st.page_link("pages/page_link_demo.py", label="Refresh This Page", icon="🔄")


if __name__ == "__page__":
    page()