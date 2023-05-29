import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import base64
from io import BytesIO
import plotly.express as px
import base64
import os
import random

st.set_page_config(page_title="Flower Recognition", page_icon=":bouquet:")

st.markdown("# Flower Recognition")

# Load the pre-trained model
model = tf.keras.models.load_model('ResNet50V2_model.h5')

# Define the classes
class_names = ['Babi', 'Calimerio', 'Chrysanthemum', 'Hydrangeas', 'Lisianthus', 'Pingpong', 'Rosy', 'Tana']

# Define the predict function
def predict(file_obj):
    img = Image.open(file_obj)
    img = img.resize((256, 256))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype('float32') / 255.0
    predictions = model.predict(img_array)
    score = np.squeeze(predictions)
    return score

# Create a file uploader
uploaded_file = st.file_uploader('Upload an image', type=['jpg', 'jpeg'])

# Check if a file has been uploaded
if uploaded_file is not None:
    # Load the uploaded image
    image = Image.open(uploaded_file)

    # Resize the image if its width or height is greater than 500 pixels
    max_size = 500
    if image.width > max_size or image.height > max_size:
        image.thumbnail((max_size, max_size))

    # Convert the image to a data URL
    buffered = BytesIO()
    image.save(buffered, format='JPEG')
    uploaded_image_data_url = base64.b64encode(buffered.getvalue()).decode()

    # Make a prediction using your pre-trained model and predict function
    prediction = predict(uploaded_file)
    predicted_class_index = np.argmax(prediction)
    predicted_class = class_names[predicted_class_index]
    predicted_probability = prediction[predicted_class_index]

    # Load 10 random images from a local directory
    image_dir = f'Flowers/Flowers/{predicted_class}'
    image_files = random.sample(os.listdir(image_dir), 10)
    images_html = '<div style="display: flex; flex-wrap: wrap;">'
    for image_file in image_files:
        image_path = os.path.join(image_dir, image_file)
        with open(image_path, 'rb') as f:
            image_data_url = base64.b64encode(f.read()).decode()
        images_html += f'<div style="flex: 1 0 25%;"><img src="data:image/jpeg;base64,{image_data_url}" style="margin: 8px; width: 100%;" /></div>'
    images_html += '</div>'

    # Create an HTML table to display the image, its file name, the classification result, and the random images
    table_html = f'''
        <style>
            table {{
                background-color: white;
                text-align: center;
                vertical-align: middle;
            }}
        </style>
        <table>
            <tr>
                <th>File Name</th>
                <td>{uploaded_file.name}</td>
            </tr>
            <tr>
                <th>Image</th>
                <td><img src="data:image/jpeg;base64,{uploaded_image_data_url}" /></td>
            </tr>
            <tr>
                <th>Classification</th>
                <td>{predicted_class} ({predicted_probability:.2f})</td>
            </tr>
            <tr>
                <th>Same flower type</th>
                <td>{images_html}</td>
            </tr>
        </table>
    '''

    # Display the table in Streamlit
    st.markdown(table_html, unsafe_allow_html=True)