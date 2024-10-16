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



# Call st.navigation in your entrypoint file with one or more pages defined by st.Page. st.navigation returns the current page, which can be executed using .run() method.

# When using st.navigation, your entrypoint file (the file passed to streamlit run) acts like a router or frame of common elements around each of your pages. Streamlit executes the entrypoint file with every app rerun. To execute the current page, you must call the .run() method on the StreamlitPage object returned by st.navigation.

# The set of available pages can be updated with each rerun for dynamic navigation. By default, st.navigation draws the available pages in the side navigation if there is more than one page. This behavior can be changed using the position keyword argument.

# As soon as any session of your app executes the st.navigation command, your app will ignore the pages/ directory (across all sessions).