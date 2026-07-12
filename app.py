import streamlit as st
import joblib
import numpy as np

# Load model 
model = joblib.load("loan_model.pkl")

st.title("Loan Approval Prediction System")

# User Inputs
gender = st.selectbox("Gender", ["Female", "Male"])
married = st.selectbox("Married", ["No", "Yes"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
self_employed = st.selectbox("Self Employed", ["No", "Yes"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=1)
loan_amount_term = st.number_input("Loan Amount Term", min_value=1)
credit_history = st.selectbox("Credit History", [0, 1])
property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

# Encoding
gender = 0 if gender == "Female" else 1
married = 0 if married == "No" else 1
education = 0 if education == "Graduate" else 1
dependents = {"0": 0, "1": 1, "2": 2, "3+": 3}[dependents]
self_employed = 0 if self_employed == "No" else 1
property_area = {"Rural": 0, "Semiurban": 1, "Urban": 2}[property_area]

# Prediction
if st.button("Predict"):

    features = np.array([[
        gender,
        married,
        dependents,
        education,
        self_employed,
        credit_history,
        property_area,
        np.log(applicant_income),
        np.log(loan_amount),
        np.log(loan_amount_term),
        np.log(total_income)
        
        
    ]])

    


    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Not Approved")
