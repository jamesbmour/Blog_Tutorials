import streamlit as st


# def main():
st.title("Streamlit State Management Tutorial")

# Initialize session state
if "count" not in st.session_state:
    st.session_state.count = 0

if "name" not in st.session_state:
    st.session_state.name = ""

# Display current state
st.header("Current State")
st.write(st.session_state)

# Increment count
st.header("Increment Counter")
if st.button("Increment"):
    st.session_state.count += 1

# Reset count
st.header("Reset Counter")
if st.button("Reset"):
    st.session_state.count = 0

# Input field with callback
st.header("Name Input with Callback")


def name_callback():
    st.session_state.name = st.session_state.name_input.title()


st.text_input("Enter your name", key="name_input", on_change=name_callback)
st.write(f"Hello, {st.session_state.name}!")

# Form example
st.header("Form Example")


def form_callback():
    st.write(f"Slider value: {st.session_state.my_slider}")
    st.write(f"Checkbox value: {st.session_state.my_checkbox}")


with st.form(key="my_form"):
    st.slider("My slider", 0, 10, 5, key="my_slider")
    st.checkbox("Yes or No", key="my_checkbox")
    st.form_submit_button(label="Submit", on_click=form_callback)


#
# if __name__ == "__main__":
#     main()

# Created/Modified files during execution:
# No files were created or modified during the execution of this script.
