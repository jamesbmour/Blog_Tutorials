import time

import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Streamlit Layouts Tutorial",
    page_icon=":art:",
    initial_sidebar_state="collapsed",
)

st.title("Streamlit Layouts Tutorial")

# 1. Columns
st.header("Columns")
st.write("Using `st.columns()` to create columns.")

col1, col2 = st.columns(2)

col1.write("This is column 1")

with col1:
    st.write("This is column 1")
    if st.button("Button in Column 1"):
        st.write("btn 1 pressed")
with col2:
    st.write("This is column 2")
    if st.button("Button in Column 2"):
        st.write("Button 2 Pressed")

# 2. Container
st.header("Container")
st.write("Using `st.container()` to group elements together.")

with st.container():
    st.write("This is inside a container")
    st.button("Button inside container")

    # Nested container
    with st.container():
        st.write("This is a nested container")
        st.button("Button inside nested container")

# 3. Empty
st.header("Empty")
st.write("Using `st.empty()` as a placeholder for updating content.")
placeholder = st.empty()

# Update the placeholder content dynamically
for i in range(5):
    placeholder.write(f"Updating... {i}")
    time.sleep(1)

placeholder.write("Done!")

# 4. Expander
st.header("Expander")
st.write("Using `st.expander()` to hide/show content.")
with st.expander("Click to expand"):
    st.write("This is inside the expander")
    st.button("Button inside expander")
    ecol1, ecol2 = st.columns(2)
    with ecol1:
        st.write("This is column 1")
    with ecol2:
        st.write("This is column 2")


# 5. Form
st.header("Form")
st.write("Using `st.form()` to group input widgets with a submit button.")

with st.form("my_form"):
    st.write("Inside the form")
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=0, max_value=120, step=1)
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(f"Hello {name}, you are {age} years old.")

# 6. Sidebar
st.header("Sidebar")
st.write("Using `st.sidebar` to add content to the sidebar.")


with st.sidebar:
    st.write("This is in the sidebar")
    st.button("Sidebar Button")

# 7. Tabs
st.header("Tabs")
st.write("Using `st.tabs()` to create tabbed sections.")

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.write("This is the cat tab")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=300)

with tab2:
    st.write("This is the dog tab")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=300)

with tab3:
    st.write("This is the owl tab")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=300)
