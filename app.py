import streamlit as st
import requests

st.title("🌸 Iris Flower Classifier")

# Inputs
sepal_length = st.number_input("Sepal Length", 0.0, 10.0, step=0.1)
sepal_width = st.number_input("Sepal Width", 0.0, 10.0, step=0.1)
petal_length = st.number_input("Petal Length", 0.0, 10.0, step=0.1)
petal_width = st.number_input("Petal Width", 0.0, 10.0, step=0.1)

if st.button("Predict"):
    input_data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    response = requests.post("http://localhost:8000/predict", json=input_data)
    prediction = response.json()["prediction"]

    class_names = ['Setosa', 'Versicolor', 'Virginica']
    st.success(f"🌼 Predicted Class: {class_names[prediction]}")
