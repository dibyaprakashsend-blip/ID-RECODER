import streamlit as st
import pytesseract
from PIL import Image
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

st.title("🪪 ID Finder")

st.write("Place the ID card clearly in front of the camera")

camera_image = st.camera_input("📷 Take a picture of the ID card")

if camera_image:

    image = Image.open(camera_image)

    st.subheader("📷 Captured Image")
    st.image(image)

    # Convert image to OpenCV
    img = np.array(image)

    height, width = img.shape[:2]

    # Crop the CENTER area
    crop = img[
        int(height * 0.15):int(height * 0.90),
        int(width * 0.25):int(width * 0.75)
    ]

    st.subheader("🪪 ID Card Area")
    st.image(crop)

    # Resize the cropped ID
    processed = cv2.resize(
        crop,
        None,
        fx=3,
        fy=3,
        interpolation=cv2.INTER_CUBIC
    )

    # Convert to grayscale
    processed = cv2.cvtColor(
        processed,
        cv2.COLOR_RGB2GRAY
    )

    st.subheader("🔍 Image Used For OCR")
    st.image(processed)

    # OCR
    text = pytesseract.image_to_string(
        processed,
        config="--psm 11"
    )

    st.subheader("📄 Information Read From ID")

    if text.strip():
        st.text(text)
    else:
        st.warning(
            "No text detected. Move the ID card closer."
        )