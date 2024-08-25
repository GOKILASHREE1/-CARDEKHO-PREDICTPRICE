import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Use a direct image URL here
image_url = "https://images.sftcdn.net/images/t_app-cover-l,f_auto/p/4fc946e1-aa36-4af9-971b-834ea4f4e0ef/4143215449/cardekho-new-second-hand-car-screenshot.png"  # Replace with a valid direct image URL

# Custom CSS to add background image and center content
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{image_url}");
        background-size: cover; /* Cover the entire screen */
        background-position: top left; /* Position image at the top left to keep the top visible */
        background-repeat: no-repeat;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: flex-start; /* Align items at the top to prevent cutting off the image */
        padding: 20px;
        margin-top: 20px; /* Additional margin to prevent cutting off the top */
        overflow: hidden; /* Prevent scrolling if background is too large */
        padding-right: 20px; /* Provide space on the right for the scrollbar */
        box-sizing: border-box;
    }}
    .block-container {{
        background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent background for better text readability */
        padding: 20px;
        border-radius: 10px;
        width: 100%;
        max-width: 500px;
        margin-top: 50px; /* Additional margin to avoid cutting off the top content */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Load the saved model, scaler, and label encoders
model_path = r'C:\CARPRICEPREDICTION\virtualenvironment\XGBoost.pkl'  
scaler_path = r'C:\CARPRICEPREDICTION\virtualenvironment\scaler.pkl'
label_encoders_path = r'C:\CARPRICEPREDICTION\virtualenvironment\label_encoders.pkl'

with open(model_path, 'rb') as file:
    model = pickle.load(file)

with open(scaler_path, 'rb') as file:
    scaler = pickle.load(file)

with open(label_encoders_path, 'rb') as file:
    label_encoders = pickle.load(file)

# Streamlit app title and input fields
st.title('Car Price Prediction')

# Input fields for user
city = st.selectbox('City', ['bangalore', 'chennai', 'delhi', 'hyderabad', 'jaipur', 'kolkata'])
bt = st.selectbox('Body Type', ['Hatchback', 'SUV', 'Sedan', 'MUV', 'Minivans', 'Wagon'])
transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'LPG', 'CNG'])
owner_no = st.slider('Number of Owners', min_value=1, max_value=5, value=1)
insurance_validity = st.selectbox('Insurance Validity', ['Third Party insurance', 'Comprehensive', 'Third Party', 'Zero Dep', '2', '1', 'Not Available'])
year_of_manufacture = st.slider('Year of Manufacture', min_value=2000, max_value=2024, value=2015)
max_power = st.slider('Max Power (in BHP)', min_value=50, max_value=500, value=100)
engine = st.slider('Engine Capacity (in CC)', min_value=500, max_value=5000, value=1500)
no_of_cylinders = st.slider('Number of Engine Cylinders', min_value=2, max_value=12, value=4)

# Map the inputs to your model's feature names
input_data = {
    'Max Power': max_power,
    'Year of Manufacture': year_of_manufacture,
    'ownerNo': owner_no,
    'Engine': engine,
    'Transmission': transmission,
    'bt': bt,
    'Fuel Type': fuel_type,
    'Engine and Transmission_Engine_No of Cylinder': no_of_cylinders,
    'Insurance Validity': insurance_validity,
    'city': city
}

# Label encode categorical features
for col, le in label_encoders.items():
    if col in input_data:
        input_data[col] = le.transform([input_data[col]])[0]

# Convert input_data to a DataFrame with the correct feature names
input_df = pd.DataFrame([input_data])

# Scale the input data
input_data_scaled = scaler.transform(input_df)

# Predict car price
if st.button('Predict Price'):
    prediction = model.predict(input_data_scaled)[0]
    
    # Format the price
    if prediction >= 1_00_00_000:  # 1 crore
        formatted_price = f"₹ {prediction / 1_00_00_000:.2f} crores"
    elif prediction >= 1_00_000:  # 1 lakh
        formatted_price = f"₹ {prediction / 1_00_000:.2f} lakhs"
    elif prediction >= 1_000:  # 1 thousand
        formatted_price = f"₹ {prediction / 1_000:.2f} thousand"
    else:
        formatted_price = f"₹ {int(prediction):,}"

    st.write(f"The predicted price of the car is {formatted_price}")
