import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Title
st.title("Media: Images, Videos, Audio, Files")

# Display Image
st.header("Display Images")
image_url = "https://images.unsplash.com/photo-1705900266125-3b999d5a5c62?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
st.image(image_url, caption='Twilight Whisper over Mount Cook of New Zealand', use_column_width=True)




# st.video
st.header("Display Videos")
video_url = "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4"
st.video(video_url, start_time=0)ß


# st.audio
st.header("Display Audio")
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
st.audio(audio_url, format='audio/mp3')



