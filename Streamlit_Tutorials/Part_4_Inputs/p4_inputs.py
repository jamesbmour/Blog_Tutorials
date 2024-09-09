# Part 4 Inputs
import streamlit as st

# Set the title of the app
st.title("Streamlit Part 4: Inputs in Streamlit")

# Create columns for better UI
# Using two columns to split the inputs across the screen for a cleaner and more organized layout.
col1, col2 = st.columns(2)

# Column 1
with col1:
    # Button Input
    # The st.button widget creates a clickable button.
    # Discuss how buttons can trigger events when clicked.
    st.header("Button")
    if st.button("Click Me"):
        st.write("Button Clicked")

    # Link Button
    # The st.link_button creates a button that links to an external URL.
    # This is useful for navigation or redirecting users to external resources.
    st.header("Link Button")
    if st.link_button("Click Me", "https://www.streamlit.io/"):
        st.write("Link Button Clicked")

    # Download Button
    # The st.download_button allows users to download files directly from your app.
    # This is useful for exporting data, reports, or any downloadable content.
    st.header("Download Button")
    if st.download_button("Download Me", "hello world", "hello.txt"):
        st.write("Download Button Clicked")

    # Checkbox Input
    # The st.checkbox widget creates a checkbox that users can check or uncheck.
    # You can use it to toggle between different states or options.
    st.header("Checkbox")
    if st.checkbox("Check Me"):
        st.write("Checkbox Checked")

    # Radio Button Input
    # The st.radio widget allows users to select one option from a list of radio buttons.
    # This is ideal for mutually exclusive choices.
    st.header("Radio")
    radio_val = st.radio("Select Color", ["Red", "Green", "Blue"])
    if radio_val:
        st.write(f"You selected {radio_val}")

    # Selectbox Input
    # The st.selectbox widget provides a dropdown menu for users to choose from.
    # This is useful for a long list of options where space is limited.
    st.header("Selectbox")
    select_val = st.selectbox("Select Color", ["Red", "Green", "Blue"])
    if select_val:
        st.write(f"You selected {select_val}")

    # Multiselect Input
    # The st.multiselect widget allows users to select multiple options from a list.
    # Useful for scenarios where multiple choices are allowed.
    st.header("Multiselect")
    multiselect_val = st.multiselect("Select Colors", ["Red", "Green", "Blue"])
    if multiselect_val:
        st.write(f"You selected {multiselect_val}")

    # Select Slider Input
    # The st.select_slider widget is similar to the slider but allows for discrete steps.
    # Useful when the range has specific, predefined values.
    st.header("Select Slider")
    select_slider_val = st.select_slider("Select Value", options=range(1, 101))
    if select_slider_val:
        st.write(f"You selected {select_slider_val}")

# Column 2
with col2:
    # Text Input
    # The st.text_input widget provides a single-line text box for user input.
    # Ideal for collecting short text information like names, titles, etc.
    st.header("Text Input")
    text_input_val = st.text_input("Enter some text")
    if text_input_val:
        st.write(f"You entered {text_input_val}")

    # Text Area
    # The st.text_area widget provides a multi-line text box for user input.
    # Ideal for collecting longer text inputs like descriptions or comments.
    st.header("Text Area")
    text_area_val = st.text_area("Enter some text")
    if text_area_val:
        st.write(f"You entered {text_area_val}")

    # Number Input
    # The st.number_input widget allows users to input numbers.
    # Useful for scenarios requiring numeric data entry like ages, quantities, etc.
    st.header("Number Input")
    number_input_val = st.number_input("Enter a number")
    if number_input_val:
        st.write(f"You entered {number_input_val}")

    # Date Input
    # The st.date_input widget allows users to select a date from a calendar.
    # Useful for date-related inputs like setting appointments, deadlines, etc.
    st.header("Date Input")
    date_input_val = st.date_input("Enter a date")
    if date_input_val:
        st.write(f"You entered {date_input_val}")

    # Time Input
    # The st.time_input widget provides a way to input time.
    # Great for time-related inputs such as setting alarms or meeting times.
    st.header("Time Input")
    time_input_val = st.time_input("Enter a time")
    if time_input_val:
        st.write(f"You entered {time_input_val}")

    # File Uploader
    # The st.file_uploader widget allows users to upload files.
    # Useful for scenarios where file input is needed, such as image uploads or data files.
    st.header("File Uploader")
    file_uploader_val = st.file_uploader("Upload a file")
    if file_uploader_val:
        st.write(f"You uploaded {file_uploader_val}")

    # Color Picker
    # The st.color_picker widget lets users pick a color using a color picker tool.
    # Useful for design tools or any scenario requiring color input.
    st.header("Color Picker")
    color_picker_val = st.color_picker("Pick a color", "#00f900")
    if color_picker_val:
        st.write(f"You picked {color_picker_val}")

    # Camera Input
    # The st.camera_input widget allows users to take pictures using their device's camera.
    # Useful for capturing real-time images in your app.
    st.header("Camera Input")
    camera_input_val = st.camera_input("Take a picture")
    if camera_input_val:
        st.write(f"You took a picture")
