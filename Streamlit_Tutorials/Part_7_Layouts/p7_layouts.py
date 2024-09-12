import streamlit as st

st.set_page_config(
    page_title="Streamlit Part 7: Layouts",
    page_icon="random",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("Streamlit Part 7: Layouts")


# using st.columns
st.write("### This is outside the columns")
col1, col2 = st.columns(2)

with col1:
    st.write("This is column 1")
    st.button("Press me")


with col2:
    st.write("This is column 2")
    st.button("Press me 2")

# using st.container
st.write("### This is outside the container")
container = st.container()
with container:
    st.write("This is inside the container")
    st.button("Container 1")

# using st.dialog
st.write("### This is outside the dialog")


# with st.dialog("This is a dialog"):
#     st.write("This is inside the dialog")
#     st.button("Container 2")
@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()


if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"

# using st.empty
st.write("### This is outside the empty")

empty = st.empty()
empty.write("This is inside the empty")
empty.button("Empty")

# using st.expander
st.write("### This is outside the expander")
with st.expander("This is an expander"):
    st.write("This is inside the expander")
    st.button("Expander")

# using st.form
st.write("### This is outside the form")
with st.form("This is a form"):
    st.write("This is inside the form")
    name = st.text_input("Name")
    st.form_submit_button("Form")
    st.write(f"Name: {name}")


# using st.popover
st.write("### This is outside the popover")
with st.popover("This is a popover"):
    st.write("This is inside the popover")
    st.button("Popover")

# using st.sidebar
st.write("### This is outside the sidebar")
with st.sidebar:
    st.write("This is inside the sidebar")
    st.button("Sidebar")

# using st.tabs
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.write("This is the cat tab")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with tab2:
    st.write("This is the dog tab")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with tab3:
    st.write("This is the owl tab")
    st.image("https://static.streamlit.io/examples/owl.jpg")
