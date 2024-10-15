# pages/navigation_intro.py
import streamlit as st


def main():
    st.title("Introduction to st.navigation")
    st.write(
        "The `st.navigation` function is used to configure pages in a multi-page Streamlit app."
    )
    st.code(
        """
import streamlit as st

pages = [
    st.Page("pages/intro.py", title="Introduction", icon="👋"),
    st.Page("pages/page1.py", title="Page 1", icon="1️⃣"),
    st.Page("pages/page2.py", title="Page 2", icon="2️⃣"),
]

pg = st.navigation(pages)
pg.run()
    """,
        language="python",
    )
    st.write("This creates a sidebar navigation menu with three pages.")


if __name__ == "__page__":
    main()
