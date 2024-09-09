import streamlit as st

st.title("Streamlit Part 7: Layouts")
# st.sidebar

# using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# using 'with' notation
with st.sidebar:
    st.write("This is a sidebar")
    st.button("Press me")

# using st.columns
col1, col2 = st.columns(2)

with col1:
    st.write("This is column 1")
    st.button("Press me")


with col2:
    st.write("This is column 2")
    st.button("Press me")


# using st.tabs
tabs = st.tabs()
with tabs:
    with st.tab("First"):
        st.write("This is the first tab")
    with st.tab("Second"):
        st.write("This is the second tab")
    with st.tab("Third"):
        st.write("This is the third tab")

# using st.expander
expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")
expander.write("...and even more details...")
expander.write("...and even more details...")

# using st.empty
empty = st.empty()
empty.text("This is some text")
empty.markdown("This is some markdown")


# using st.container
container = st.container()
container.write("This is inside the container")
container.write("This is also inside the container")

