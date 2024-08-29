import time
import pandas as pd
import streamlit as st

# Title of the app
st.title("Introduction to Streamlit: Part 1")

# Subtitle
st.subheader("st.write and magic command")

# st.write() function
st.write("Dataframe using st.write() function")

# Write a DataFrame
df = pd.DataFrame({
    "Column 1": [1, 2, 3, 4],
    "Column 2": [10, 20, 30, 40]
})
st.write(df)

# write markdown
markdown_txt = ("### This is a Markdown Header\n"
                "#### This is a Markdown Subheader\n"
                "This is a Markdown paragraph.\n")
st.markdown(markdown_txt)

st.write("## Streaming Data using st.write_stream() function")
stream_btn = st.button("Click Button to Stream Data")

TEXT = """
# Stream a generator, iterable, or stream-like sequence to the app.

st.write_stream iterates through the given sequences and writes all chunks to the app. String chunks will be written 
using a typewriter effect. Other data types will be written using st.write.
write(string) : Prints the formatted Markdown string, with
support for LaTeX expression, emoji shortcodes, and colored text. See docs for st.markdown for more.

- write(dataframe) : Displays any dataframe-like object in an interactive table.
- write(dict) : Displays dict-like in an interactive viewer.
- write(list) : Displays list-like in an interactive viewer.
- write(error) : Prints an exception specially.
- write(func) : Displays information about a function.
- write(module) : Displays information about the module.
- write(class) : Displays information about a class.
- write(mpl_fig) : Displays a Matplotlib figure.
- write(generator) : Streams the output of a generator.
- write(openai.Stream) : Streams the output of an OpenAI stream.
- write(altair) : Displays an Altair chart.
- write(PIL.Image) : Displays an image.
- write(keras) : Displays a Keras model.
- write(graphviz) : Displays a Graphviz graph.
- write(bokeh_fig) : Displays a Bokeh figure.
- write(sympy_expr) : Prints SymPy expression using LaTeX.
- write(htmlable) : Prints _repr_html_() for the object if available.
- write(db_cursor) : Displays DB API 2.0 cursor results in a table.
- write(obj) : Prints str(obj) if otherwise unknown.
"""


def stream_data(txt="Hello, World!"):
    """
    Generator function that yields words from the TEXT variable with a delay.

    This function splits the TEXT variable into words, and then yields each word followed by a space.
    It introduces a delay of 0.01 seconds between yielding each word to simulate streaming data.

    Yields:
        str: A word from the TEXT variable followed by a space.
    """
    for word in txt.split(" "):
        yield word + " "
        time.sleep(0.01)


if stream_btn:
    st.write_stream(stream_data(TEXT))
