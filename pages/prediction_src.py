import streamlit as st


st.header('MILK QUALITY PREDICTION')
st.subheader('This python code is implemented for Streamlit')
st.code(''' 
 # Notes
# do a "pip install streamlit" first 
# to run on terminal issue this command
# python -m streamlit run streamlit_test.py

import streamlit as st
import pickle

# Function to define milk features
def milk_features(pH, temperature, taste, odor, fat, turbidity, color):
    # Convert categorical inputs to binary (0 or 1)
    taste_value = 1 if taste == 'Good' else 0
    odor_value = 1 if odor == 'Good' else 0
    fat_value = 1 if fat == 'High' else 0
    turbidity_value = 1 if turbidity == 'High' else 0
    
    return {
        'pH': pH,
        'temperature': temperature,
        'taste': taste_value,
        'odor': odor_value,
        'fat': fat_value,
        'turbidity': turbidity_value,
        'color': color
    }

# Load the trained NaiveBayesClassifier from the saved file
filename = '/content/milk_grade_prediction.sav'
with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)

# Streamlit App
st.title("🥛 Milk Grade Predictor 🥛")
st.subheader("Enter the milk's attributes to predict its grade:")

# User inputs for milk attributes
pH = st.slider('pH', 3.0, 9.5, step=0.1, value=6.5)
temperature = st.slider('Temperature (°C)', 34, 90, value=40)
taste = st.selectbox('Taste', ['Bad', 'Good'])
odor = st.selectbox('Odor', ['Bad', 'Good'])
fat = st.selectbox('Fat', ['Low', 'High'])
turbidity = st.selectbox('Turbidity', ['Low', 'High'])
color = st.slider('Color', 240, 255, value=250)

# Function to make a prediction
def predict_milk_grade(pH, temperature, taste, odor, fat, turbidity, color):
    features = milk_features(pH, temperature, taste, odor, fat, turbidity, color)
    prediction = loaded_model.classify(features)
    return prediction

# Display prediction button and result
if st.button('Predict'):
    predicted_grade = predict_milk_grade(pH, temperature, taste, odor, fat, turbidity, color)
    st.success(f"The predicted milk grade is: {predicted_grade}")


''')