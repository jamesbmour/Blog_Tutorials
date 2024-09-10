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

    # 2. Link Button
    st.subheader("2. Link Button")

    # 3. Download Button
    st.subheader("3. Download Button")

    # 4. Checkbox Input
    st.subheader("4. Checkbox")

    # 5. Radio Button Input
    st.subheader("5. Radio")

    # 6. Selectbox Input
    st.subheader("6. Selectbox")

    # 7. Multiselect Input
    st.subheader("7. Multiselect")

    # 8. Select Slider Input
    st.subheader("8. Select Slider")

# Column 2
with col2:
    # 9. Text Input
    st.subheader("9. Text Input")

    # 10. Text Area
    st.subheader("10. Text Area")

    # 11. Number Input
    st.subheader("11. Number Input")

    # 12. Date Input
    st.subheader("12. Date Input")

    # 13. Time Input
    st.subheader("13. Time Input")

    # 14. File Uploader
    st.subheader("14. File Uploader")

    # 15. Color Picker
    st.subheader("15. Color Picker")

    # 16. Camera Input
    st.subheader("16. Camera Input")