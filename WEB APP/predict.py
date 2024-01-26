from tensorflow.keras.models import load_model
from keras.preprocessing import image
import numpy as np
import pandas as pd


li = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

def predict(filepath,li):
    model = load_model('D:\\Academic projects\\Minor project\\code\\cnn2\\model.h5')

    image_path = filepath
    new_img = image.load_img(image_path, target_size=(224, 224))
    img = image.img_to_array(new_img)
    img = np.expand_dims(img, axis=0)
    img = img/255

    prediction = model.predict(img)

    d = prediction.flatten()
    j = d.max()
    for index,item in enumerate(d):
        if item == j:
            class_name = li[index]
    return class_name

def pest_name(input_string):
    df = pd.read_excel("D:\\Academic projects\\Minor project\\App\\pest data.xlsx")
    
    if input_string in df["Disease"].values:
        value = df.loc[df["Disease"] == input_string, "pest"].values[0]
        return value


def function1(fl,li=li):
    class_name = predict(fl,li)
    pN = pest_name(class_name)
    plantName, diseaseName = class_name.split('___')
    if 'healthy' in diseaseName:
        diseaseName = '-'
    return (plantName, diseaseName, pN)
