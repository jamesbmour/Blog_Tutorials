# Streamlit Part 5: Working with Media Elements
import streamlit as st
from streamlit_autorefresh import st_autorefresh

count = st_autorefresh(interval=4000, limit=200, key="refresh_counter")

st.title("Streamlit Part 5: Media: Images, Videos, Audio, Files")

# 2. Displaying a logo
"""
    image: Anything supported by st.image
        The image to display in the upper-left corner of your app and its
        sidebar. If ``icon_image`` is also provided, then Streamlit will only
        display ``image`` in the sidebar.

        Streamlit scales the image to a height of 24 pixels and a maximum
        width of 240 pixels. Use images with an aspect ratio of 10:1 or less to
        avoid distortion.
    link : str or None
        The external URL to open when a user clicks on the logo. The URL must
        start with "\\http://" or "\\https://". If ``link`` is ``None`` (default),
        the logo will not include a hyperlink.
    icon_image: Anything supported by st.image or None
        An alternate image to replace ``image`` in the upper-left corner of the
        app's main body. If ``icon_image`` is ``None`` (default), Streamlit
        will render ``image`` in the upper-left corner of the app and its
        sidebar. Otherwise, Streamlit will render ``icon_image`` in the
        upper-left corner of the app and ``image`` in the upper-left corner
        of the sidebar.

        Streamlit scales the image to a height of 24 pixels and a maximum
        width of 240 pixels. Use images with an aspect ratio of 10:1 or less to
        avoid distortion.
"""
logo_link = "https://cdn.simpleicons.org/youtube"
st.subheader("1. Display Logo")
st.logo(
    logo_link,
    link="https://streamlit.io/gallery",
)
# st.logo() is a custom function (not standard in Streamlit)
# It's likely defined elsewhere in the project to display a clickable logo
# Parameters:
#   - logo_link: URL of the logo image
#   - link: URL to navigate to when the logo is clicked
#   - icon_image: URL of an icon to display alongside the logo

# 3. Displaying Images
st.subheader("2. Display Images")

image_url = "https://images.unsplash.com/photo-1705900266125-3b999d5a5c62?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
st.image(
    image_url,
    caption="Twilight Whisper over Mount Cook of New Zealand",
    use_column_width=True,
)
# st.image() displays an image in the Streamlit app
# Parameters:
#   - image_url: URL of the image to display
#   - caption: Optional text to display below the image
#   - use_column_width: If True, the image will expand to fill the column width

# 4. Displaying Videos
st.subheader("3. Display Videos")

video_url = "https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_2mb.mp4"
st.video(video_url, start_time=0)
# st.video() embeds a video player in the Streamlit app
# Parameters:
#   - video_url: URL of the video to play
#   - start_time: Time in seconds where the video should start playing

# 5. Displaying Audio
st.subheader("4. Display Audio")

audio_url = "https://sample-videos.com/audio/mp3/crowd-cheering.mp3"
st.audio(audio_url, format="audio/mp3", start_time=5)
# st.audio() embeds an audio player in the Streamlit app
# Parameters:
#   - audio_url: URL of the audio file to play
#   - format: MIME type of the audio file (e.g., 'audio/mp3')

# Key Takeaways:
# 1. Streamlit provides easy-to-use functions for displaying various media types.
# 2. These functions (st.image, st.video, st.audio) handle the complexities of
#    embedding media, allowing developers to focus on content.
# 3. Each function has parameters to customize the display and behavior of the media.
# 4. Using these media elements can greatly enhance the interactivity and
#    visual appeal of your Streamlit applications.

# Next Steps:
# - Experiment with different types of media in your Streamlit apps.
# - Try loading media from local files in addition to URLs.
# - Explore more advanced features like interactive widgets to control media playback.
