import streamlit as st
import pandas as pd
import pickle
import os


# Page Configuration
st.set_page_config(
    page_title="Car Price Prediction",
    layout="centered"
)

# Load Model

model_path = os.path.join(os.path.dirname(__file__), "car_price_model.pkl")

with open(model_path, "rb") as file:
    model = pickle.load(file)

# Title
st.title("Car Price Prediction")
st.write("Predict the selling price of a used car.")

st.markdown("---")

# User Inputs


present_price = st.number_input(
    "Present Price (Lakhs)",
    min_value=0.0,
    value=5.50,
    step=0.10
)

driven_kms = st.number_input(
    "Driven Kilometers",
    min_value=0,
    value=30000,
    step=1000
)

owner = st.selectbox(
    "Number of Previous Owners",
    [0,1,2,3]
)

year = st.number_input(
    "Manufacturing Year",
    min_value=2000,
    max_value=2026,
    value=2018
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol","Diesel","CNG"]
)

selling_type = st.selectbox(
    "Seller Type",
    ["Dealer","Individual"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual","Automatic"]
)

# Feature Engineering

Car_age = 2026 - year

Fuel_Type_Diesel = 1 if fuel_type == "Diesel" else 0
Fuel_Type_Petrol = 1 if fuel_type == "Petrol" else 0

Selling_type_Individual = 1 if selling_type == "Individual" else 0

Transmission_Manual = 1 if transmission == "Manual" else 0

# Prediction

if st.button("Predict Selling Price"):

    input_df = pd.DataFrame({
        "Present_Price":[present_price],
        "Driven_kms":[driven_kms],
        "Owner":[owner],
        "Car_age":[Car_age],
        "Fuel_Type_Diesel":[Fuel_Type_Diesel],
        "Fuel_Type_Petrol":[Fuel_Type_Petrol],
        "Selling_type_Individual":[Selling_type_Individual],
        "Transmission_Manual":[Transmission_Manual]
    })

    prediction = model.predict(input_df)

    st.success(
        f"Estimated Selling Price: ₹ {prediction[0]:.2f} Lakhs"
    )