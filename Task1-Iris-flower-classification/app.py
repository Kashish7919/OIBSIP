import streamlit as st
import pickle
import numpy as np

# Page Configuration
st.markdown("Iris Flower Classification")

# Load Model
with open("iris_model.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.title("Iris Flower Classification")
st.write(
    "Enter the flower measurements below to predict the Iris species."
)

st.markdown("---")

# User Inputs
sepal_length = st.number_input(
    "Sepal Length (cm)",
    min_value=0.0,
    max_value=10.0,
    value=5.1,
    step=0.1
)

sepal_width = st.number_input(
    "Sepal Width (cm)",
    min_value=0.0,
    max_value=10.0,
    value=3.5,
    step=0.1
)

petal_length = st.number_input(
    "Petal Length (cm)",
    min_value=0.0,
    max_value=10.0,
    value=1.4,
    step=0.1
)

petal_width = st.number_input(
    "Petal Width (cm)",
    min_value=0.0,
    max_value=10.0,
    value=0.2,
    step=0.1
)

# Predict Button
if st.button("Predict Species"):

    input_data = np.array([
        [
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]
    ])

    prediction = model.predict(input_data)[0]

    st.markdown("---")

    if prediction == "Iris-setosa" or prediction == "setosa":
        st.success("Predicted Species: Iris Setosa")

    elif prediction == "Iris-versicolor" or prediction == "versicolor":
        st.success("Predicted Species: Iris Versicolor")

    elif prediction == "Iris-virginica" or prediction == "virginica":
        st.success("Predicted Species: Iris Virginica")

    else:
        st.success(f"Predicted Species: {prediction}")