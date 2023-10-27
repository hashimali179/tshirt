import streamlit as st
import cv2
import numpy as np

def main():
    st.title("Image Text Placement with OpenCV")

    # Upload an image
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    # Add text parameters in the sidebar
    text = st.sidebar.text_input("Text to add", "Hello, Streamlit!")
    text_color_r = st.sidebar.slider("Text Color (Red)", min_value=0, max_value=255, value=255)
    text_color_g = st.sidebar.slider("Text Color (Green)", min_value=0, max_value=255, value=255)
    text_color_b = st.sidebar.slider("Text Color (Blue)", min_value=0, max_value=255, value=255)
    font_size = st.sidebar.slider("Font Size", min_value=10, max_value=100, value=36)
    thickness = st.sidebar.slider("Thickness", min_value=1, max_value=10, value=2)
    x_center_position_percent = st.sidebar.slider("X Center Position (%)", min_value=0, max_value=100, value=50)
    y_position_percent = st.sidebar.slider("Y Position (%)", min_value=0, max_value=100, value=50)

    if uploaded_image:
        # Read the uploaded image using OpenCV
        img = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), 1)

        # Convert BGR image to RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Define the font
        font = cv2.FONT_HERSHEY_PLAIN

        # Calculate the text size
        text_size = cv2.getTextSize(text, font, font_size / 10, thickness)[0]

        # Calculate the position as percentages of the image size
        image_height, image_width, _ = img_rgb.shape
        x_position = int((x_center_position_percent / 100) * image_width - (text_size[0] // 2))
        y_position = y_position_percent

        # Set the font color and thickness
        color = (text_color_r, text_color_g, text_color_b)

        # Convert font size to OpenCV-compatible integer
        font_size = int(font_size)

        # Add the text to the image
        cv2.putText(img_rgb, text, (x_position, y_position), font, font_size / 10, color, thickness)

        # Display the image with the added text
        st.image(img_rgb, channels="RGB", use_column_width=True, caption="Image with Text")

if __name__ == "__main__":
    main()
