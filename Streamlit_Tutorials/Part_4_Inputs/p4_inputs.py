# Streamlit Part 4: Inputs in Streamlit
import streamlit as st

# Set config for wide mode and auto rerun
st.set_page_config(layout="wide")

# Set the title of the app
st.title("Streamlit Part 4: Inputs in Streamlit")

# Introduce the layout
# "We will use two columns to neatly organize our input widgets, allowing us to fit more on the screen and make it easier to follow along."

# Create columns for better UI
col1, col2 = st.columns(2)

# Column 1
with col1:

    # 1. Button Input
    # "Let's start with a basic button input. The `st.button` widget creates a simple clickable button.
    # You can use it to trigger events or actions in your app. Here, we’ll display a message when the button is clicked."
    st.subheader("1. Button")
    btn1 = st.button("Click Me", key="button", help="Click me to see the magic", type='secondary', disabled=False)
    if btn1:
        st.write("Button Clicked")

    # 2. Link Button
    # "Next, we have a link button using `st.link_button`. This is useful when you want to redirect users to an external link.
    # Here, clicking the button will open the Streamlit homepage."
    st.subheader("2. Link Button")
    if st.link_button("Click Me", "https://www.streamlit.io/"):
        st.write("Link Button Clicked")

    # 3. Download Button
    # "The `st.download_button` is perfect for allowing users to download files directly from your app.
    # You specify the file content and the filename. In this example, clicking the button will download a simple text file."
    st.subheader("3. Download Button")
    if st.download_button("Download Me", "hello world", "hello.txt", mime='text/plain'):
        st.write("Download Button Clicked")

    # 4. Checkbox Input
    # "Moving on to checkboxes, the `st.checkbox` widget is great for toggling options.
    # You can use it to control different states in your app. We’ll show a message when this checkbox is checked."
    st.subheader("4. Checkbox")
    checkbox_val = st.checkbox("Check Me", value=False)
    if checkbox_val:
        st.write("Checkbox Checked")

    # 5. Radio Button Input
    # "Radio buttons are perfect when you want users to select one option from a list.
    # We use `st.radio` for this. Here, users can choose a color, and we display the selected value."
    st.subheader("5. Radio")
    radio_val = st.radio("Select Color", ["Red", "Green", "Blue"], index=0)
    if radio_val:
        st.write(f"You selected {radio_val}")

    # 6. Selectbox Input
    # "The `st.selectbox` is similar to radio buttons but comes in a dropdown format, which is great for saving space
    # when you have many options. We'll demonstrate this by selecting a color from a dropdown menu."
    st.subheader("6. Selectbox")
    select_val = st.selectbox("Select Color", ["Red", "Green", "Blue", "Black"], index=1)
    if select_val:
        st.write(f"You selected {select_val}")

    # 7. Multiselect Input
    # "With `st.multiselect`, users can select multiple options from a list.
    # This is useful when more than one choice is allowed. Here, you can pick multiple colors."
    st.subheader("7. Multiselect")
    multiselect_val = st.multiselect("Select Colors", ["Red", "Green", "Blue", "Black"], default=["Red"])
    if multiselect_val:
        st.write(f"You selected {multiselect_val}")

    # 8. Select Slider Input
    # "The `st.select_slider` widget lets you select from a range of options but with discrete steps.
    # This is handy when you want users to pick from predefined values. Here, the range is from 1 to 100."
    st.subheader("8. Select Slider")
    select_slider_val = st.select_slider("Select Value", options=range(1, 101), value=50)
    if select_slider_val:
        st.write(f"You selected {select_slider_val}")

# Column 2
with col2:

    # 9. Text Input
    # "Now, let's move on to text inputs. The `st.text_input` widget allows users to enter a single line of text.
    # This is perfect for short inputs like names or titles. Here, we’ll capture and display the input."
    st.subheader("9. Text Input")
    text_input_val = st.text_input("Enter some text", value="", max_chars=50)
    if text_input_val:
        st.write(f"You entered {text_input_val}")

    # 10. Text Area
    # "For longer text inputs, we use `st.text_area`. This provides a multi-line text box, great for comments or descriptions.
    # In this example, we'll capture and display the entered text."
    st.subheader("10. Text Area")
    text_area_val = st.text_area("Enter some text", value="", height=150, max_chars=200)
    if text_area_val:
        st.write(f"You entered {text_area_val}")

    # 11. Number Input
    # "The `st.number_input` widget is used for numerical inputs. You can set minimum, maximum values, and the step size.
    # This is useful for things like quantities or ages. Here, users will input a number."
    st.subheader("11. Number Input")
    number_input_val = st.number_input("Enter a number", value=0, min_value=0, max_value=100, step=1)
    if number_input_val:
        st.write(f"You entered {number_input_val}")

    # 12. Date Input
    # "For selecting dates, `st.date_input` provides a nice calendar interface.
    # This is ideal for date-based inputs like appointments or deadlines. Here, we'll select and display a date."
    st.subheader("12. Date Input")
    date_input_val = st.date_input("Enter a date")
    if date_input_val:
        st.write(f"You selected {date_input_val}")

    # 13. Time Input
    # "Similarly, `st.time_input` allows users to input a time, which is useful for scheduling tasks.
    # We'll let users pick a time and then display it."
    st.subheader("13. Time Input")
    time_input_val = st.time_input("Enter a time")
    if time_input_val:
        st.write(f"You selected {time_input_val}")

    # 14. File Uploader
    # "The `st.file_uploader` widget is designed for uploading files. You can specify allowed file types to ensure the correct files are uploaded.
    # Here, we allow image and text file uploads."
    st.subheader("14. File Uploader")
    file_uploader_val = st.file_uploader("Upload a file", type=["png", "jpg", "txt"])
    if file_uploader_val:
        st.write(f"You uploaded {file_uploader_val.name}")

    # 15. Color Picker
    # "The `st.color_picker` widget is a fun one, allowing users to pick a color using a color picker tool.
    # This could be useful in design applications or when color selection is needed."
    st.subheader("15. Color Picker")
    color_picker_val = st.color_picker("Pick a color", value="#00f900")
    if color_picker_val:
        st.write(f"You picked {color_picker_val}")

    # 16. Camera Input
    # "Lastly, we have `st.camera_input`, which allows users to take pictures using their device's camera.
    # This can be really useful for applications that require real-time image capture. Here, we’ll let users take a picture."
    st.subheader("16. Camera Input")
    camera_input_val = st.camera_input("Take a picture", help="Capture an image using your camera")
    if camera_input_val:
        st.write("Picture captured successfully")