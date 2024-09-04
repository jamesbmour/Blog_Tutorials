# Part 2: Text Elements in Streamlit
import streamlit as st

# st.title: The st.title() function is used to display a large title at the top of the app.
# This is typically the main heading for your Streamlit application.
st.title("Streamlit Tutorials")

# st.header: The st.header() function is used for displaying a header.
# It's smaller than the title, making it ideal for section headings within your app.
st.header("This is a Header")

# st.subheader: The st.subheader() function displays a subheader.
# It's slightly smaller than the header and is great for subsections within your content.
st.subheader("This is a Subheader")

# st.caption: The st.caption() function allows you to add captions.
# This is useful for providing additional context or notes on your content, usually in a smaller font size.
st.caption("This is a caption")

# st.code: The st.code() function is used to display code snippets in your app.
# You can pass the code as a string, and it will be nicely formatted for readability.
code_txt = """

import pandas as pd
import streamlit as st

st.title("Streamlit Tutorials") 
for i in range(10):
    st.write(i)
    
"""
st.code(code_txt)
# st.code("import pandas as pd\n"
#         "print('Hello, World!')")

# st.text: The st.text() function is used for displaying plain text.
# It's basic and doesn't include any styling, making it useful for simple text elements.
st.text("This is a text")

# st.latex: The st.latex() function is used to display mathematical expressions using LaTeX.
# It's perfect for apps that require mathematical notation.
# Here, we're showing Einstein's famous equation e=mc^2.
st.latex(r"e = mc^2")

# Another example of st.latex: Let's also display the integral of x^2 from a to b.
st.latex(r"\int_a^b x^2 dx")

# st.divider: The st.divider() function adds a horizontal line to separate sections of your app.
# This can help to visually distinguish different parts of your content.
st.write("This is some text below the divider.")
st.divider()
st.write("This is some other text below the divider.")