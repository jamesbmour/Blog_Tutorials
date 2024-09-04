# Part 2: Text Elements in Streamlit
import streamlit as st

# 1. st.title:
st.title("Part 2: Text Elements in Streamlit")
st.divider()

# 2. st.header:
st.header("This is a Header")
st.divider()

# 3. st.subheader:
st.subheader("This is a Subheader")
st.divider()

# 4. st.caption:
st.caption("This is a caption")
st.divider()

# 5. st.code:
code_txt = """
import pandas as pd
import streamlit as st

st.title("Streamlit Tutorials")
for i in range(10):
    st.write(i)
"""

st.code(code_txt, language='python', wrap_lines=True, line_numbers=True)
st.divider()

# 6. st.text:
st.text("This is a text")
st.divider()

# 7. st.latex:
st.latex(r"e = mc^2")

# 8. st.divider:
st.write("This is some text below the divider.")
st.divider()
st.write("This is some other text below the divider.")