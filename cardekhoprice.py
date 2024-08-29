import streamlit as st
import pandas as pd
import pickle

# Image URL for the background
image_url = "https://images.sftcdn.net/images/t_app-cover-l,f_auto/p/4fc946e1-aa36-4af9-971b-834ea4f4e0ef/4143215449/cardekho-new-second-hand-car-screenshot.png"

# Custom CSS to add background image and center content
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{image_url}");
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: flex-start;
        padding: 20px;
        margin-top: 20px;
        overflow: hidden;
        padding-right: 20px;
        box-sizing: border-box;
    }}
    .block-container {{
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 10px;
        width: 100%;
        max-width: 700px;
        margin-top: 50px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Load the saved model, scaler, and label encoders
model_path = r'C:\CARPRICEPREDICTION\virtualenvironment\best_model.pkl'  
scaler_path = r'C:\CARPRICEPREDICTION\virtualenvironment\scaler.pkl'
label_encoders_path = r'C:\CARPRICEPREDICTION\virtualenvironment\label_encoders.pkl'

# Load the best model, scaler, and label encoders
with open(model_path, 'rb') as model_file:
    best_model = pickle.load(model_file)

with open(scaler_path, 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

with open(label_encoders_path, 'rb') as le_file:
    label_encoders = pickle.load(le_file)

# Streamlit app title
st.title('Car Price Prediction')

# Two-column layout for input fields
col1, col2 = st.columns(2)

with col1:
    city = st.selectbox('City', ['bangalore', 'chennai', 'delhi', 'hyderabad', 'jaipur', 'kolkata'])
    bt = st.selectbox('Body Type', ['Hatchback', 'SUV', 'Sedan', 'MUV', 'Coupe', 'Minivans',
                                    'Pickup Trucks', 'Convertibles', 'Wagon'])
    transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
    fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'LPG', 'CNG'])

with col2:
    owner_no = st.slider('Number of Owners', min_value=1, max_value=5, value=1)
    seats = st.slider('No of seats', min_value=2, max_value=10, value=2)
    year_of_manufacture = st.slider('Year of Manufacture', min_value=2000, max_value=2024, value=2015)
    max_power = st.slider('Max Power (in BHP)', min_value=50, max_value=500, value=100)
    engine = st.slider('Engine Capacity (in CC)', min_value=500, max_value=5000, value=1500)

# Map the inputs to your model's feature names in the exact same order used during training
input_data = pd.DataFrame({
    'city': [city],
    'bt': [bt],
    'Year of Manufacture': [year_of_manufacture],
    'Transmission': [transmission],
    'Fuel Type': [fuel_type],
    'ownerNo': [owner_no],
    'Seats': [seats],
    'Engine': [engine],
    'Max Power': [max_power]
})

# Encode categorical features
for col, le in label_encoders.items():
    if col in input_data.columns:
        input_data[col] = le.transform(input_data[col].astype(str))

# Standardize features with the same scaler used during training
input_data_scaled = scaler.transform(input_data)

# Predict price
if st.button('Predict Price'):
    predicted_price = best_model.predict(input_data_scaled)[0]
    
    # Format the price
    if predicted_price >= 1_00_00_000:  # 1 crore
        formatted_price = f"₹ {predicted_price / 1_00_00_000:.2f} crores"
    elif predicted_price >= 1_00_000:  # 1 lakh
        formatted_price = f"₹ {predicted_price / 1_00_000:.2f} lakhs"
    elif predicted_price >= 1_000:  # 1 thousand
        formatted_price = f"₹ {predicted_price / 1_000:.2f} thousand"
    else:
        formatted_price = f"₹ {int(predicted_price):,}"
    
    # Display prediction
    st.subheader(f'Predicted Price: {formatted_price}')

# Run the Streamlit app
if __name__ == '__main__':
    st.write('Adjust the inputs and view the predicted price above.')
