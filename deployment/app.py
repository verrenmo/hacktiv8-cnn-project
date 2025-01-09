#------------------------------------------------
# Phase 2 - Graded Challenge 7
# Name: Verren Monica
# Batch: RMT - 038
# Model Deployment - App
#------------------------------------------------

# Import Libraries
import streamlit as st
import eda 
import prediction

# Set up the page configuration with custom title, layout and expanded side bar
st.set_page_config(
   page_title='Car vs Bike',
   layout='wide',
   initial_sidebar_state='expanded',
)

# Create sidebar dropdown menu to navigate between pages
page = st.sidebar.selectbox('Go to Page : ', ('Exploratory Data Analysis', 'Car vs Bike Prediction'))

# Navigate to selected page based on dropdown choosen
if page == 'Exploratory Data Analysis':
    eda.run()
else:
    prediction.run()
