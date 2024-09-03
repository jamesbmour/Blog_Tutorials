import pandas as pd
import streamlit as st
import time

# Title of the app
st.title("Intro to Streamlit")

# Subheader
st.subheader("This is a subheader")


# st.write() function
st.write("### Dataframe using st.write() function")

# Write a DataFrame
df = pd.DataFrame({
    "Column 1": [1, 2, 3, 4],
    "Column 2": [10, 20, 30, 40]
})

st.write(df)

# Write markdown
markdown_txt = ("### This is a Markdown Header\n"
                "#### This is a Markdown Subheader\n"
                "This is a Markdown paragraph.\n")
st.markdown(markdown_txt)

# Streaming 
st.write("## Streaming Data using st.write_stream() function")
stream_btn = st.button("Click Button to Stream Data")

TEXT = """
# Stream a generator, iterable, or stream-like sequence to the app.
"""

# Function to stream data
def stream_data(txt="Hello, World!"):
    for word in txt.split(" "):
        yield word + " "
        time.sleep(0.1)

if stream_btn:
    st.write_stream(stream_data(TEXT))
    

