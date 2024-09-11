# Streamlit Part 5: Working with Media Elements
import streamlit as st
from streamlit_autorefresh import st_autorefresh

count = st_autorefresh(interval=4000, limit=1000, key="refresh_counter")

st.markdown("## Streamlit Part 5: Media: Images, Videos, Audio, Files")

# 1. Displaying a logo
st.subheader("1. Display Logo")
logo_link = "https://cdn.simpleicons.org/youtube"
st.subheader("1. Display Logo")
st.logo(
    logo_link,
    link="https://streamlit.io/gallery",
)

# 2. Displaying Images
st.subheader("2. Display Images")
image_url = "https://images.unsplash.com/photo-1705900266125-3b999d5a5c62?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
st.image(
    image_url,
    caption="Twilight Whisper over Mount Cook of New Zealand",
    use_column_width=True,
)

# 3. Displaying Videos
st.subheader("3. Display Videos")
video_url = "https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_2mb.mp4"
st.video(video_url, start_time=3)

# 4. Displaying Audio
st.subheader("4. Display Audio")
audio_url = "https://sample-videos.com/audio/mp3/crowd-cheering.mp3"
st.audio(audio_url, format="audio/mp3", start_time=5)
