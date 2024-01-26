# Plant Pathology and Diagnosis

Plant Pathology and Diagnosis is a project that uses deep learning to diagnose and treat plant diseases. This project is designed to help farmers quickly identify and treat plant diseases, which can have a significant impact on crop yields and quality.

## Overview
The project uses a convolutional neural network (CNN) to classify images of plants into healthy or diseased categories, and if the plant is diseased, the type of disease is identified. The model is trained on a dataset of plant images using transfer learning, and the accuracy of the model is validated on a test dataset.

The user interface is built using the Python Tkinter library. The user can select an image of a plant and the model will predict whether the plant is healthy or diseased, and if it is diseased, the type of disease is identified. The user is also provided with information on the type of pesticide that can be used to treat the disease.

## Getting started
To use the Plant Pathology and Diagnosis project, the user must have Python 3.x installed on their computer. The project requires the following Python packages:

    - Tkinter
    - PIL
    - Pandas
    - Keras
    - TensorFlow
To run the project, download the code and run the gui.py file using Python.

## Dataset
The project uses the "New Plant Diseases Dataset" (https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset) from Kaggle. This dataset contains 38 different classes of plant diseases, with each class containing 700-800 images.

## Model
The CNN used in this project is based on the VGG16 architecture, with the last fully connected layer replaced with a new layer with the number of classes equal to the number of classes in the dataset. The model is trained using transfer learning, with the pre-trained weights of the VGG16 model used as the initial weights for the new model.

## User Interface
The user interface is designed using the Python Tkinter library. The user can select an image of a plant using the "Select Image" button, and the model will predict whether the plant is healthy or diseased, and if it is diseased, the type of disease is identified. The user is also provided with information on the type of pesticide that can be used to treat the disease.

## Streamlit App
The Streamlit app allows users to diagnose plant diseases by uploading an image of a plant. The app uses a deep learning model to analyze the image and identify the disease, if any.

To run the app, follow these steps:

1. Install Streamlit by running pip install streamlit in your command line.
2. Download the app files from the streamlit_app folder in this repository.
3. Open a command prompt or terminal and navigate to the folder where you downloaded the app files.
4. Run the app by typing streamlit run app.py in your command line.
5. The app will open in your default web browser. Follow the on-screen instructions to upload an image and diagnose any plant diseases.

The app requires an internet connection to download the deep learning model and dependencies.

## Conclusion
The Plant Pathology and Diagnosis project provides a simple and effective way to diagnose and treat plant diseases. The project can be easily extended to include more classes of plant diseases and to provide additional information on the treatment of diseases. The project can be useful for farmers who want to ensure the health and productivity of their crops.