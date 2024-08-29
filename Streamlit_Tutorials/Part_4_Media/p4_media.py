import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Title
st.title("Media: Images, Videos, Audio, Files")

# Header
st.header("Images")
img_url = "https://images.ctfassets.net/23aumh6u8s0i/2Qhstbnq6i34wLoPoAjWoq/9f66f58a22870df0d72a3cbaf77ce5b6/streamlit_hero.jpg"
response = requests.get(img_url)
image = Image.open(BytesIO(response.content))
st.image(image, caption="Streamlit Hero Image", use_column_width=True)



