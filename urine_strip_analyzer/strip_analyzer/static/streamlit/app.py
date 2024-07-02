import streamlit as st
import requests
from PIL import Image

st.title("Urine Strip Analyzer")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.text(image.size)
    st.image(image, caption='Uploaded Image', width=270 ,use_column_width=True)

    if st.button("Analyze"):
        files = {'file': uploaded_file.getvalue()}
        response = requests.post('http://localhost:8000/', files=files)
        if response.status_code == 200:
            result = response.json()
            st.json(result)
        else:
            st.error("Failed to analyze the image")
