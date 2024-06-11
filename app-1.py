import streamlit as st
import requests

url = 'http://127.0.0.1:5000/predict'

# Streamlit app
st.title("Credit Card Approval Prediction")

# Input features
age = st.slider("Select your age", 18, 70)
annual_income = st.number_input("Enter your annual income (in USD)", min_value=0)
num_dependents = st.number_input("Enter the number of dependents", min_value=0)
owns_car = st.selectbox("Do you own a car?", ["Yes", "No"])
owns_house = st.selectbox("Do you own a house?", ["Yes", "No"])
years_employed = st.slider("Enter your employment length (years)", 0, 30)
num_credit_cards = st.number_input("Enter the number of credit cards", min_value=0)
previously_defaulted = st.selectbox("Have you previously defaulted?", ["Yes", "No"])
current_debt = st.number_input("Enter your current debt (in USD)", min_value=0)
monthly_mortgage = st.number_input("Enter your monthly mortgage or rent (in USD)", min_value=0)
monthly_expenses = st.number_input("Enter your monthly expenses (in USD)", min_value=0)
active_loans = st.selectbox("Do you have any active loans?", ["Yes", "No"])
previously_bankrupt = st.selectbox("Have you previously been bankrupt?", ["Yes", "No"])
credit_score = st.number_input("Enter your credit score", min_value=0)
employed = st.selectbox("Are you currently employed?", ["Yes", "No"])
education_level = st.selectbox("Select your education level", ["None", "High School", "College"])
marital_status = st.selectbox("Select your marital status", ["Single", "Married", "Divorced", "Widowed"])
loan_to_value_ratio = st.slider("Enter your loan to value ratio", 0.0, 1.0)

# Convert inputs to feature list
features = [
    age, annual_income, num_dependents, 
    1 if owns_car == "Yes" else 0, 
    1 if owns_house == "Yes" else 0, 
    years_employed, num_credit_cards, 
    1 if previously_defaulted == "Yes" else 0, 
    current_debt, monthly_mortgage, monthly_expenses, 
    1 if active_loans == "Yes" else 0, 
    1 if previously_bankrupt == "Yes" else 0, 
    credit_score, 
    1 if employed == "Yes" else 0, 
    2 if education_level == "College" else (1 if education_level == "High School" else 0), 
    3 if marital_status == "Widowed" else (2 if marital_status == "Divorced" else (1 if marital_status == "Married" else 0)),
    loan_to_value_ratio
]

# Ensure the correct number of features
assert len(features) == 18, f"Expected 18 features, but got {len(features)}"

# Make prediction
if st.button("Predict"):
    url = 'http://127.0.0.1:5000/predict'
    response = requests.post(url, json={'features': features})
    prediction = response.json()['prediction']
    st.write("The prediction is:", "Approved" if prediction == 1 else "Not Approved")
