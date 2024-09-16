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

# using st.container
st.write("### This is outside the container")

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


# using st.expander
st.write("### This is outside the expander")

st.write("### This is outside the form")

# using st.popover
st.write("### Adding popover")


# using st.sidebar
st.write("### This is outside the sidebar")

# using st.tabs
st.write("### Adding tabs")
