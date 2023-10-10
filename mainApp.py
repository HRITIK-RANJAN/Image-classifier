import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from PIL import Image
import json
import joblib
import util
import io
import base64

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    selected



@st.cache_data
def load_model():
    with open('./saved_model.pkl', 'rb') as f:
        model = joblib.load(f)
    return model
with st.spinner('Model is being loaded..'):
  model=load_model()


# Set the page title and a brief description
st.title("Image Classifier App")
st.write("Upload an image and click 'Submit'")

# Create a file uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# Initialize a variable to store the uploaded image
image_data = None

# Check if a file has been uploaded
if uploaded_file is not None:
    # Read the uploaded image
    image = Image.open(uploaded_file)
    image_data = image

    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("Image uploaded successfully!")

def classify(image,model):
    print('Image type------------',type(image))
    image_bytes = image.tobytes()
    # Encode the image bytes to a base64 string
    base64_encoded = base64.b64encode(image_bytes).decode('utf-8')
    with open('abcd.txt','w') as f:
        f.write(base64_encoded)

    response = json.dumps(util.classify_image(base64_encoded,model))
    print(response)

    return response

# Create a submit button
if st.button("Submit"):
    if image_data is not None:
        # Process the uploaded image here (you can save it, analyze it, etc.)
        st.write("Processing image...")
        classify(image_data,model)
       
