import streamlit as st
import time

# -------------------------------
# Streamlit Execution Flow Elements Tutorial
# -------------------------------

st.title("Streamlit Execution Flow Elements Tutorial")

# -------------------------------
# 1. Using `st.dialog`
# -------------------------------
st.header("1. st.dialog")
st.write("`st.dialog` creates a modal dialog that can be triggered by user actions.")


# -------------------------------
# 2. Using `st.fragment`
# -------------------------------
st.header("2. st.fragment")
st.write("`st.fragment` allows a part of your app to rerun independently.")


# -------------------------------
# 3. Using `st.rerun`
# -------------------------------
st.header("3. st.rerun")
st.write("`st.rerun` allows you to rerun the entire app or just a fragment.")


# -------------------------------
# 4. Using `st.stop`
# -------------------------------
st.header("4. st.stop")
st.write("`st.stop` halts the execution of the script at that point.")


# -------------------------------
# 5. Using `st.form` and `st.form_submit_button`
# -------------------------------
st.header("5. st.form and st.form_submit_button")
st.write(
    "`st.form` groups inputs together, and `st.form_submit_button` submits the form."
)


# -------------------------------
# Bonus: Combining Elements
# -------------------------------
