import streamlit as st
import requests

st.title("🌸 Iris Flower Classifier")
st.write("Enter the flower measurements to predict the species.")

# Inputs
sepal_length = st.number_input("Sepal Length (cm)", 0.0, 10.0, step=0.1)
sepal_width = st.number_input("Sepal Width (cm)", 0.0, 10.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", 0.0, 10.0, step=0.1)
petal_width = st.number_input("Petal Width (cm)", 0.0, 10.0, step=0.1)

if st.button("Predict"):
    data = {
        "features": [sepal_length, sepal_width, petal_length, petal_width]
    }
    try:
        #response = requests.post("http://localhost:8000/predict", json=data)
        #following a iris-network is created
        #response = requests.post("http://iris-backend:8000/predict", json=data)
        #following when using docket compose
        response = requests.post("http://backend:8000/predict", json=data)
        
        if response.status_code == 200:
            pred = response.json()["prediction"]
            species = ["Setosa 🌱", "Versicolor 🌷", "Virginica 🌸"][pred]
            st.success(f"Predicted Class: {species} ({pred})")
        else:
            st.error(f"Error: {response.text}")
    except Exception as e:
        st.error(f"Connection error: {e}")
