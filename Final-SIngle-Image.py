import streamlit as st
import cv2
import numpy as np

def main():
    st.title("Image Background Replacement")

    # Upload background and foreground images
    background_image = st.file_uploader("Upload Background Image", type=["jpg", "png", "jpeg"])
    foreground_image = st.file_uploader("Upload Foreground Image", type=["jpg", "png", "jpeg"])

    # Add sliders in the sidebar
    fg_height = st.sidebar.slider("Foreground Height", min_value=10, max_value=1000, value=100)
    fg_width = st.sidebar.slider("Foreground Width", min_value=10, max_value=1000, value=100)
    x_fg_offset = st.sidebar.slider("X FG Offset", min_value=0, max_value=1000, value=0)
    y_fg_offset = st.sidebar.slider("Y FG Offset", min_value=0, max_value=1000, value=0)

    
    if background_image and foreground_image:
        # Read the uploaded images using OpenCV
        bg_image = cv2.imdecode(np.fromstring(background_image.read(), np.uint8), 1)
        fg_image = cv2.imdecode(np.fromstring(foreground_image.read(), np.uint8), 1)


        # Resize the foreground image based on slider values
        resized_fg_image = cv2.resize(fg_image, (fg_width, fg_height))

        # Calculate the position to place the resized foreground image based on slider values
        y_offset = y_fg_offset
        x_offset = x_fg_offset
        

        # Replace the background with the foreground on the specified location
        bg_image[y_offset:y_offset + fg_height, x_offset:x_offset + fg_width] = resized_fg_image

            
        # Display the result
        st.image(bg_image, channels="BGR", use_column_width=True, caption="Result")

if __name__ == "__main__":
    main()
