# Car Price Prediction using Machine Learning

# Project Overview

The **Car Price Prediction** project is a Machine Learning application that predicts the selling price of a used car based on various features such as the car's present price, kilometers driven, fuel type, transmission type, seller type, ownership history, and age of the car.

The objective of this project is to help users estimate the resale value of a car accurately using machine learning techniques.

# Objective

To build a Machine Learning regression model capable of predicting the selling price of a used car using historical car data.

# Dataset Information

The dataset contains information about different used cars with the following attributes:

- Car Name
- Manufacturing Year
- Present Price
- Selling Price (Target)
- Driven Kilometers
- Fuel Type
- Seller Type
- Transmission Type
- Number of Previous Owners

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

# Data Preprocessing

The following preprocessing steps were performed before training the model:

- Removed unnecessary columns (`Car_Name`)
- Created a new feature (`Car_Age`) from the manufacturing year
- Applied One-Hot Encoding to categorical columns:
  - Fuel Type
  - Seller Type
  - Transmission

- Split the dataset into training and testing sets

# Machine Learning Models Used

The following regression algorithms were trained and compared:

- Linear Regression
- Random Forest Regressor

The best-performing model was selected based on evaluation metrics.

# Model Evaluation

The models were evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

The model with the highest R² score and lowest prediction error was selected as the final model.

# Project Structure

```
Task2_Car_Price_Prediction

│── app.py
│── car data.csv
│── car_price_prediction.ipynb
│── car_price_model.pkl
│── requirements.txt
│── README.md
```

# Installation

Clone the repository:

```bash
git clone <repository-link>
```

Move to the project folder:

```bash
cd Task2_Car_Price_Prediction
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

# Run the Application

Run the Streamlit application using:

<!-- terminal run this command -->

streamlit run app.py

The application will open in your browser where users can enter the required car details and receive the predicted selling price.

# Input Features

The model uses the following inputs:

- Present Price (Lakhs)
- Driven Kilometers
- Number of Previous Owners
- Manufacturing Year (used to calculate Car Age)
- Fuel Type
- Seller Type
- Transmission Type

# Output

The application predicts the estimated selling price of the used car in **Lakhs (₹)**.

# Features

- User-friendly Streamlit interface
- Real-time price prediction
- Machine Learning-based regression model
- Data preprocessing and feature engineering
- Model deployment using Streamlit

# Future Improvements

- Include additional vehicle features such as mileage, engine capacity, and location.
- Improve prediction accuracy using advanced ensemble models.
- Deploy the application on cloud platforms.
- Add interactive visualizations for data exploration.
