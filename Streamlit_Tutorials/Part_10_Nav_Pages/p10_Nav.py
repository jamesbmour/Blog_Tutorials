# Streamlit Part 10: Navigation and Pages
import streamlit as st

st.title("Navigation and Pages")
st.divider()
st.write("### st.navigation")


# st.navigation
def page1():
    st.write(st.session_state.foo)


def page2():
    st.write(st.session_state.bar)


# Widgets shared by all the pages
st.selectbox("Foo", ["A", "B", "C"], key="foo")
st.checkbox("Bar", key="bar")

pg = st.navigation([st.Page(page1), st.Page(page2)])
pg.run()

st.divider()
st.write("### st.page")


# def page2():
#     st.title("Second page")
#

pg = st.navigation(
    [
        st.Page("./pages/page_1.py", title="First page", icon="🔥"),
        st.Page(page2, title="Second page", icon=":material/favorite:"),
    ]
)
pg.run()


st.divider()
st.write("### st.page_link")
# st.page_link
# st.page_link("p10_Nav.py", label="Home", icon="🏠")
# st.page_link("./pages/page_1.py", label="Page 1", icon="1️⃣")
# st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")

st.divider()
st.write("### st.switch_page")
# st.switch_page
if st.button("Home"):
    st.switch_page("p10_Nav.py")
if st.button("Page 1"):
    st.switch_page("pages/page_1.py")
if st.button("Page 2"):
    st.switch_page("pages/page_2.py")
