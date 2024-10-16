# pages/switch_page_demo.py
import streamlit as st

# When st.switch_page is called, the current page execution stops and the specified page runs as if the user clicked on it in the sidebar navigation. The specified page must be recognized by Streamlit's multipage architecture (your main Python file or a Python file in a pages/ folder). Arbitrary Python scripts cannot be passed to st.switch_page.
def switch_page():
    st.title("Using st.switch_page")
    st.write("`st.switch_page` allows you to programmatically switch pages.")
    st.code(
        """
if st.button("Go to Intro"):
    st.switch_page("app_pages/intro.py")
    """,
        language="python",
    )
    st.write("Let's try it out:")
    if st.button("Go to Intro"):
        st.switch_page("app_pages/intro.py")


if __name__ == "__page__":
    switch_page()
