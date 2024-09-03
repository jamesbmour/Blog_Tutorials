import time
import pandas as pd
import streamlit as st

# =========================================
# Welcome to this tutorial series on Streamlit!
# In this first episode, we'll be diving into the basics of Streamlit by exploring two powerful features:
# `st.write()` and the magic commands in Streamlit.
# Let's get started by building a simple app that demonstrates these functionalities.

# Title of the app
st.title("Introduction to Streamlit: Part 1")

# Video Script: st.write and magic commands
# =========================================
# First, let's talk about `st.write()`.
# This function is one of the most versatile functions in Streamlit.
# You can use it to display text, data, charts, and much more with a single line of code.

# Subtitle
st.subheader("This is a Subtitle")

# Video Script: Displaying a DataFrame using st.write()
# =========================================
# For example, let’s display a DataFrame using `st.write()`.
# Here, we have a simple DataFrame with two columns.
# All we need to do is pass the DataFrame to `st.write()`.

# st.write() function
st.write("Dataframe using st.write() function")

# Write a DataFrame
df = pd.DataFrame({"Column 1": [1, 2, 3, 4], "Column 2": [10, 20, 30, 40]})
st.write(df)

# Video Script: Markdown with st.write and st.markdown
# =========================================
# Another cool feature is that `st.write()` can also handle Markdown text.
# But if you want more control over the formatting, you can use `st.markdown()`.

# write markdown
markdown_txt = (
    "### This is a Markdown Header\n"
    "#### This is a Markdown Subheader\n"
    "This is a Markdown paragraph.\n"
)
st.markdown(markdown_txt)

# Video Script: Streaming data with st.write_stream
# =========================================
# Now, let's move on to something a bit more dynamic: streaming data.
# Streamlit allows you to stream data to your app in real-time using the `st.write_stream()` function.
# This is particularly useful for displaying data that updates over time, like sensor readings or live analytics.

st.write("## Streaming Data using st.write_stream() function")
stream_btn = st.button("Click Button to Stream Data")

TEXT = """
# Stream a generator, iterable, or stream-like sequence to the app.
"""


# Function to stream data
def stream_data(txt="Hello, World!"):
    for word in txt.split(" "):
        yield word + " "
        time.sleep(0.01)


if stream_btn:
    st.write_stream(stream_data(TEXT))

# Video Script: Conclusion
# =========================================
# That's it for this introductory episode!
# We’ve covered how to use `st.write()` to display data and text, as well as how to stream data using `st.write_stream()`.
# In the next episode, we'll explore more widgets and interactivity features in Streamlit.
# If you found this video helpful, don’t forget to like and subscribe for more content.
# See you in the next episode!
