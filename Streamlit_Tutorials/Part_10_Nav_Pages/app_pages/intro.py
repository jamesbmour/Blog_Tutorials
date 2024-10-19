# app_pages/intro.py
import streamlit as st


# Home Page
def intro():
    st.title("Streamlit Page Navigation Tutorial")
    st.write("Welcome to this tutorial on Streamlit page navigation!")
    st.write(
        "Use the sidebar to navigate between different pages and learn about various navigation methods."
    )


if __name__ == "__page__":
    intro()
