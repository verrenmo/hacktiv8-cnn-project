#------------------------------------------------
# Phase 2 - Graded Challenge 7
# Name: Verren Monica
# Batch: RMT - 038
# Model Deployment - Prediction Page
#------------------------------------------------

# Import Libraries
import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
import gc


# Model Loading
model = load_model('modelPred.h5')


def run():
    """This function is the main entry point for running the webapps."""
    # Diplay Image
    image = Image.open('banner.jpg')
    st.image(image)

    # Display Title
    st.title('Bike vs Car Prediction')
    # Create form for user input 
    with st.form(key='formLoanApproval'):
        # Input unggah file gambar
        uploadFile = st.file_uploader("Please upload the image you want to predict.",type=["jpg", "jpeg", "png"],help="Please upload the image you want to predict.. Format gambar JPG, JPEG atau PNG.")

        st.markdown('---')
        # Predict button
        submitted = st.form_submit_button('Predict')    

    if submitted:
        st.subheader('Your image:')
        # Jika gambar belum di upload
        if not uploadFile:  
            st.warning("No image has been uploaded yet. Please upload the image before proceeding.")
            return
        else:
            def prediction(file):
                try:
                    progress = st.progress(0)
                    # Preprocessing: Resize image to target size (220x220) as required by the model
                    img = tf.keras.utils.load_img(file, target_size=(220,220))

                    # Preprocessing: Convert image to array and scale pixel values to [0, 1]
                    x = tf.keras.utils.img_to_array(img)/255

                    # Display image being predicted
                    st.image(img)

                    # Preprocessing: Expand dimensions to add a batch dimension for model input
                    x = np.expand_dims(x, axis=0)
                    images = np.vstack([x])

                    # Predict the probability of the input image belonging to each class
                    y_pred_proba = model.predict(images)

                    # Convert probability to binary class (0 or 1) using threshold of 0.5
                    y_pred_class =  1 if y_pred_proba[0] >= 0.5 else 0

                    # Map class index to class name
                    class_name = ['Bike', 'Car']
                    y_pred_class_name = class_name[y_pred_class]

                    # Display the prediction result
                    st.subheader('Prediction Result: {}'.format(y_pred_class_name))
                    progress.progress(100)
                finally:
                    # Bersihkan memori
                    gc.collect()
            prediction(uploadFile)
        

if __name__ =='__main__':
    run() 