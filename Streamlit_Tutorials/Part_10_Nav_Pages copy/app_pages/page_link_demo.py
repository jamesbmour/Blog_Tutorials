# pages/page_link_demo.py
import streamlit as st

# Display a link to another page in a multipage app or to an external page.
# If another page in a multipage app is specified, clicking st.page_link stops the current page execution and runs the specified page as if the user clicked on it in the sidebar navigation.
# If an external page is specified, clicking st.page_link opens a new tab to the specified page. The current script run will continue if not complete.
def page_link():
    st.title("Using st.page_link")
    st.write(
        "`st.page_link` allows you to create custom navigation links within your app."
    )
    st.code(
        """
st.page_link("app_pages/intro.py", label="Go to Intro", icon="🏠")
st.page_link("app_pages/page1.py", label="Visit Page 1", icon="1️⃣")
    """,
        language="python",
    )
    st.write("Let's try it out:")
    st.page_link("app_pages/intro.py", label="Go to Intro", icon="🏠")
    st.page_link("app_pages/page_link_demo.py", label="Refresh This Page", icon="🔄")
    st.page_link("https://www.streamlit.io/", label="Visit Streamlit", icon="🚀")


if __name__ == "__page__":
    page_link()