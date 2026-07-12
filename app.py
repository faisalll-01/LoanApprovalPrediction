import sys
import numpy as np
import joblib
import streamlit as st

st.write("Python:", sys.executable)

# Load model
model = joblib.load("loan_model.pkl")

st.title("🏦 Loan Approval Prediction System")

gender =  st.selectbox("Gender", ["Male","Female"])
gender = gender_encoder.transform([gender])[0]
married = st.selectbox("Married", ["Yes", "No"])
married = 0 if married== "No" else 1
dependents = st.selectbox("Dependents", [0, 1, 2, 3])
education = st.selectbox("Education", [0, 1])
self_employed = st.selectbox("Self Employed", [0, 1])
credit_history = st.selectbox("Credit History", [0, 1])
property_area = st.selectbox("Property Area", [0, 1, 2])

applicant_income_log = st.number_input("Applicant Income (log)")
loan_amount_log = st.number_input("Loan Amount (log)")
loan_term_log = st.number_input("Loan Amount Term (log)")
total_income_log = st.number_input("Total Income (log)")

if st.button("Predict"):
    data = np.array([[
        gender,
        married,
        dependents,
        education,
        self_employed,
        credit_history,
        property_area,
        applicant_income_log,
        loan_amount_log,
        loan_term_log,
        total_income_log
    ]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")
