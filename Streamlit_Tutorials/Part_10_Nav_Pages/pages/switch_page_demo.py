# pages/switch_page_demo.py
import streamlit as st


def main():
    st.title("Using st.switch_page")
    st.write("`st.switch_page` allows you to programmatically switch pages.")
    st.code(
        """
if st.button("Go to Intro"):
    st.switch_page("pages/intro.py")
    """,
        language="python",
    )
    st.write("Let's try it out:")
    if st.button("Go to Intro"):
        st.switch_page("pages/intro.py")


if __name__ == "__page__":
    main()
