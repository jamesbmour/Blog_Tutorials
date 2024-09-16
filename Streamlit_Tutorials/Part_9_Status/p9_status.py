import streamlit as st
import time

st.set_page_config(
    page_title="Streamlit Part 9: Status",
    page_icon="random",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("Streamlit Part 9: Status Elements")

st.write("### status.progress")
progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()
st.button("Rerun")


st.write("### st.status")
st.success("This is a success message!", icon="✅")

st.write("### st.spinner")
with st.spinner("In progress..."):
    time.sleep(5)
st.success("Done!")

st.write("### st.success")
st.success("This is a success message!")


st.write("### st.error")
st.error("This is an error message!")

st.write("### st.warning")
st.warning("This is a warning message!")

st.write("### st.info")
st.info("This is an info message!")

st.write("### st.exception")
try:
    raise Exception("This is an exception!")
except Exception as e:
    st.exception(e)
st.write("### st.balloons")
st.balloons()

st.write("### st.snow")
st.snow()
