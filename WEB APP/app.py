import streamlit as st
from PIL import Image
from predict import function1

st.set_page_config(page_title="Plant Disease Detection and Pesticide Recommendation", page_icon=":seedling:",layout='wide')

# Set page width and alignment of elements to center
st.markdown(
    """
    <style>
    .reportview-container {
        max-width: 100%;
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 4rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Plant Disease Detection and Pesticide Recommendation")

def main():
    st.set_option('deprecation.showfileUploaderEncoding', False)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    st.write("")
    st.write("")
    st.write("")
    container = st.container()
    left_col, right_col = container.columns(2)
    
    image_file = st.file_uploader("Select an image", type=['jpg', 'jpeg'])
    if image_file is not None:
        img = Image.open(image_file)
        resized_img = img.resize((250, 250))
        left_col.image(resized_img, caption='Original image', use_column_width=True)

        image_path = f"./{image_file.name}"
        with open(image_path, 'wb') as f:
            f.write(image_file.getbuffer())
    
        with st.spinner('Processing image...'):
            plant_name, disease_name, pesticides = function1(image_path)
        right_col.header("Prediction Results")
        right_col.write(f"**Plant Name:** {plant_name}")
        right_col.write(f"**Disease Name:** {disease_name}")
        right_col.write(f"**Recommended Pesticides:** {pesticides}")
        if disease_name == '-':
            right_col.write("** **")
            right_col.header("**Plant is Healthy**")

if __name__ == '__main__':
    main()
