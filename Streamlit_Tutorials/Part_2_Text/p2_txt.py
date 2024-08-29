# Part 2: Text Elements
import streamlit as st


# st.title
st.title("Streamlit Tutorials")

# st.header
st.header("This is a Header")

# st.subheader
st.subheader("This is a Subheader")

# st.caption
st.caption("This is a caption")

# st.code
st.code("import pandas as pd\n"
        "print('Hello, World!')")

# st.text
st.text("This is a text")

# st.latex for e = mc^2
st.latex(r"e = mc^2")
st.latex(r"\int_a^b x^2 dx")

# st.divider
st.write("This is some text below the divider.")
st.divider()
st.write("This is some other text below the divider.")