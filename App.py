# Import necessary libraries
import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('solar_model.pkl')

# Define the Streamlit app
st.title("Solar Power Generation Prediction")

st.markdown("### Enter Environmental Variables")

# Input fields for environmental variables
distance_to_solar_noon = st.number_input("Distance to Solar Noon (in radians)", value=0.5, step=0.01)
temperature = st.number_input("Temperature (°C)", value=25.0, step=0.1)
wind_direction = st.number_input("Wind Direction (degrees)", value=180, step=1)
wind_speed = st.number_input("Wind Speed (m/s)", value=3.2, step=0.1)
sky_cover = st.selectbox("Sky Cover (0: Clear to 4: Fully Covered)", options=[0, 1, 2, 3, 4])
visibility = st.number_input("Visibility (km)", value=10.0, step=0.1)
humidity = st.number_input("Humidity (%)", value=70, step=1)
average_wind_speed = st.number_input("Average Wind Speed (m/s)", value=3.0, step=0.1)
average_pressure = st.number_input("Average Pressure (inHg)", value=29.92, step=0.01)

# Button for prediction
if st.button("Predict Power Generated"):
    # Prepare the input features as a NumPy array
    input_features = np.array([
        distance_to_solar_noon, temperature, wind_direction, wind_speed,
        sky_cover, visibility, humidity, average_wind_speed, average_pressure
    ]).reshape(1, -1)

    # Predict using the model
    prediction = model.predict(input_features)

    # Display the prediction
    st.success(f"Predicted Power Generated: {prediction[0]:.2f} Joules")