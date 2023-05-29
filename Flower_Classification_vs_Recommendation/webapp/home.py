import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.write("# Assignment 2")
st.markdown(
    """
    Photo recognition-based customised inquiries are necessary in ecommerce, particularly in flower shops. 
    To remain competitive, our machine learning experts developed an image-based search solution for an online florist. 
    Users may submit images of desired blossoms, and the system will recommend alternatives. 
    The primary objectives of the project are to categorise images into eight floral categories and select 10 related images from the dataset based on user input. 
    Machine learning specialists will classify images using CNN, ResNet50V2, and VGG19 models.
"""
)

# Introduction and team members
st.write("# Flower Recommendation and Classification System ")
st.write("Welcome to our Flower Recommendation and Classification System!"
         " This system helps you explore and classify different types of flowers.")

# Team members
st.write("## Team Members - T1-G02")
st.write("- Vo Thanh Luan - s3822042")
st.write("- Nguyen Vi Phi Long")
st.write("- Nguyen Xuan Thanh")
st.write("- Vo Ngoc Diem Tien")

st.write("## Flower Classification")
st.markdown(
    """
    Upload an image of a flower, and our system will classify it into one of the predefined categories.
    We use our best models so far for classification:
    - ResNet50v2: Achieving an accuracy of 93%
    """
)


# Flower recommendation and classification
st.write("## Flower Recommendation")
st.markdown(
    """
    Upload an image of a flower, and our system will recommend 10 similar flower images.
    We use our best models so far for classification:
    - VGG16: Achieving an accuracy of 95%
    """
)


# Model accuracy chart
st.write("## Model Accuracy")
model_names = ["ResNet50", "VGG16"]
accuracy_scores = [0.95, 0.92]

df = pd.DataFrame({"Model": model_names, "Accuracy": accuracy_scores})

fig, ax = plt.subplots()
ax.bar(df["Model"], df["Accuracy"])
ax.set_ylim([0, 1])
ax.set_ylabel("Accuracy")
ax.set_title("Model Accuracy")

st.pyplot(fig)

# Additional information
st.write("## Additional Information")
st.markdown(
    """
    For more details about our system and the models used, please visit our GitHub repository:
    - [Flower Recommendation and Classification System](https://github.com/s3822042/flower-classification)
    """
)