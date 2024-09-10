# Streamlit Part 4: Input Elements
import streamlit as st

# set config for wide mode and auto rerun
st.set_page_config(layout="wide")

# Set the title of the app
st.title("Streamlit Part 4: Input Elements")

# Create columns for better UI
col1, col2 = st.columns(2)

# Column 1
with col1:
    # 1. Button Input
    st.subheader("1. Button")
    btn1 = st.button("Click Me", key="button", help="Click me to see the magic", type='secondary', disabled=False)
    if btn1:
        st.write("Button Clicked")

    # 2. Link Button
    st.subheader("2. Link Button")
    if st.link_button("Click Me", "https://www.streamlit.io/"):
        st.write("Link Button Clicked")

    # 3. Download Button
    st.subheader("3. Download Button")
    if st.download_button("Download Me", "hello world", "hello.txt", mime='text/plain'):
        st.write("Download Button Clicked")

    # 4. Checkbox Input
    st.subheader("4. Checkbox")
    checkbox_val = st.checkbox("Check Me", value=False)
    if checkbox_val:
        st.write("Checkbox Checked")

    # 5. Radio Button Input
    st.subheader("5. Radio")
    radio_val = st.radio("Select Color", ["Red", "Green", "Blue"], index=0)
    if radio_val:
        st.write(f"You selected {radio_val}")

    # 6. Selectbox Input
    st.subheader("6. Selectbox")
    select_val = st.selectbox("Select Color", ["Red", "Green", "Blue", "Black"], index=1)
    if select_val:
        st.write(f"You selected {select_val}")

    # 7. Multiselect Input
    st.subheader("7. Multiselect")
    multiselect_val = st.multiselect("Select Colors", ["Red", "Green", "Blue", "Black"], default=["Red"])
    if multiselect_val:
        st.write(f"You selected {multiselect_val}")

    # 8. Select Slider Input
    st.subheader("8. Select Slider")
    select_slider_val = st.select_slider("Select Value", options=range(1, 101), value=50)
    if select_slider_val:
        st.write(f"You selected {select_slider_val}")

# Column 2
with col2:
    # 9. Text Input
    st.subheader("9. Text Input")
    text_input_val = st.text_input("Enter some text", value="", max_chars=50)
    if text_input_val:
        st.write(f"You entered {text_input_val}")

    # 10. Text Area
    st.subheader("10. Text Area")
    text_area_val = st.text_area("Enter some text", value="", height=150, max_chars=200)
    if text_area_val:
        st.write(f"You entered {text_area_val}")

    # 11. Number Input
    st.subheader("11. Number Input")
    number_input_val = st.number_input("Enter a number", value=0, min_value=0, max_value=100, step=1)
    if number_input_val:
        st.write(f"You entered {number_input_val}")

    # 12. Date Input
    st.subheader("12. Date Input")
    date_input_val = st.date_input("Enter a date")
    if date_input_val:
        st.write(f"You selected {date_input_val}")

    # 13. Time Input
    st.subheader("13. Time Input")
    time_input_val = st.time_input("Enter a time")
    if time_input_val:
        st.write(f"You selected {time_input_val}")

    # 14. File Uploader
    st.subheader("14. File Uploader")
    file_uploader_val = st.file_uploader("Upload a file", type=["png", "jpg", "txt"])
    if file_uploader_val:
        st.write(f"You uploaded {file_uploader_val.name}")

    # 15. Color Picker
    st.subheader("15. Color Picker")
    color_picker_val = st.color_picker("Pick a color", value="#00f900")
    if color_picker_val:
        st.write(f"You picked {color_picker_val}")

    # 16. Camera Input
    st.subheader("16. Camera Input")
    camera_input_val = st.camera_input("Take a picture", help="Capture an image using your camera")
    if camera_input_val:
        st.write("Picture captured successfully")

