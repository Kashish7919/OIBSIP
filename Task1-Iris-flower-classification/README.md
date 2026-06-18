#Project Overview

The Iris Flower Classification project is a Machine Learning classification application that predicts the species of an Iris flower based on its physical measurements.

The model classifies flowers into one of the following three species:

Iris Setosa
Iris Versicolor
Iris Virginica

The prediction is made using machine learning algorithms trained on the Iris dataset.

#Objective

The objective of this project is to build a machine learning model that can accurately classify Iris flower species using:

Sepal Length
Sepal Width
Petal Length
Petal Width
Dataset Information

The Iris dataset contains 150 records and 5 columns:

Feature Description
SepalLengthCm Length of sepal in centimeters
SepalWidthCm Width of sepal in centimeters
PetalLengthCm Length of petal in centimeters
PetalWidthCm Width of petal in centimeters
Species Target class

Classes:

Iris-setosa
Iris-versicolor
Iris-virginica
Technologies Used
Python
Pandas
NumPy
Scikit-Learn
Streamlit
Pickle
Machine Learning Algorithms Used

#The following classification algorithms were trained and evaluated:

Logistic Regression
K-Nearest Neighbors (KNN)
Gaussian Naive Bayes

All three models achieved excellent performance on the dataset.

The K-Nearest Neighbors (KNN) model was selected as the final model for deployment.

Model Performance
Algorithm Accuracy
Logistic Regression 100%
K-Nearest Neighbors (KNN) 100%
Gaussian Naive Bayes 100%

Final Selected Model: K-Nearest Neighbors (KNN)

#Project Structure

Task1_Iris_Flower_Classification

├── iris.csv

├── iris_classification.ipynb

├── iris_model.pkl

├── app.py

├── requirements.txt

└── README.md

#Installation

Clone the repository:

git clone <repository_link>

Move to project directory:

cd Task1_Iris_Flower_Classification

#Install dependencies:

pip install -r requirements.txt

Run the Application

Start the Streamlit application:

streamlit run app.py

The application will open in your browser where you can enter flower measurements and get predictions.

#Features

User-friendly Streamlit interface
Real-time flower species prediction
Multiple algorithm comparison
High accuracy classification
Machine Learning model deployment
Future Enhancements
Add data visualizations
Deploy application on Streamlit Cloud
Add model comparison dashboard
Improve UI design
