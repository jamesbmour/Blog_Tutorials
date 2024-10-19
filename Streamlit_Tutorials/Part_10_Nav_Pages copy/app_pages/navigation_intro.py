# pages/navigation_intro.py
import streamlit as st

# Call st.navigation in your entrypoint file with one or more pages defined by st.Page. st.navigation returns the current page, which can be executed using .run() method.

# When using st.navigation, your entrypoint file (the file passed to streamlit run) acts like a router or frame of common elements around each of your pages. Streamlit executes the entrypoint file with every app rerun. To execute the current page, you must call the .run() method on the StreamlitPage object returned by st.navigation.

# The set of available pages can be updated with each rerun for dynamic navigation. By default, st.navigation draws the available pages in the side navigation if there is more than one page. This behavior can be changed using the position keyword argument.

# As soon as any session of your app executes the st.navigation command, your app will ignore the pages/ directory (across all sessions).
def navigation_intro():
    st.title("Introduction to st.navigation")
    st.write(
        "The `st.navigation` function is used to configure pages in a multi-page Streamlit app."
    )
    st.code(
        """
import streamlit as st

pages = [
    st.Page("app_pages/intro.py", title="Introduction", icon="👋"),
    st.Page("app_pages/page1.py", title="Page 1", icon="1️⃣"),
    st.Page("app_pages/page2.py", title="Page 2", icon="2️⃣"),
]

pg = st.navigation(pages)
pg.run()
    """,
        language="python",
    )
    st.write("This creates a sidebar navigation menu with three pages.")
    
    


if __name__ == "__page__":
    navigation_intro()
