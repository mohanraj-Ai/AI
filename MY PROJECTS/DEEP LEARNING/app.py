import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load model
model = load_model("tire_defect_model.h5")

st.set_page_config(page_title="Tyre Defect Detection", page_icon="🚗", layout="centered")

st.title("🚗 Tyre Defect Detection System")
st.write("Upload a tyre image to check whether it is Good or Defective.")

uploaded_file = st.file_uploader("Choose a tyre image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)
    
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    prob = prediction[0][0]

    st.subheader("Prediction Result:")

    if prob > 0.5:
        st.success(f"🟢 Good Tyre ({prob*100:.2f}% confidence)")
    else:
        st.error(f"🔴 Defective Tyre ({(1-prob)*100:.2f}% confidence)")

    st.progress(float(prob))