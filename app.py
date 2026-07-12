import streamlit as st
import joblib
model = joblib.load("loan_model.pkl")
st.title("🏦 Loan Approval Prediction System")

# User Inputs
gender = st.selectbox("Gender", ["Female", "Male"])
married = st.selectbox("Married", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["No", "Yes"])
credit_history = st.selectbox("Credit History", [0, 1])
property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

applicant_income = st.number_input("Applicant Income", min_value=25000, max_value=55000, value=30000)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0, max_value=50000, value=0)
loan_amount = st.number_input("Loan Amount", min_value=50, max_value=500, value=150)
loan_amount_term = st.number_input("Loan Amount Term", min_value=12, max_value=480, value=360)
# Encoding
gender = 0 if gender == "Female" else 1
married = 0 if married == "No" else 1
education = 0 if education == "Graduate" else 1
self_employed = 0 if self_employed == "No" else 1

dependents = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3+": 3
}[dependents]

property_area = {
    "Rural": 0,
    "Semiurban": 1,
    "Urban": 2
}[property_area]
import numpy as np

   total_income = applicant_income + coapplicant_income
   applicant_income_log=np.log(applicant_income)
   loan_amount_log=np.log(loan_amount)
   loan_amount_term_log=np.log(loan_amount_term)
   total_income_log=np.log(total_income)

features = np.array([[
    gender,
    married,
    dependents,
    education,
    self_employed,
    credit_history,
    property_area,
    applicant_income_log,
    loan_amount_log=np,
    loan_amount_term_log,
    total_income_log=np.log(total_income)
]])
if st.button("Predict"):
    data = np.array([[gender, married, dependents, education,
                      self_employed, credit_history, property_area,
                      applicant_income_log, loan_amount_log,
                      loan_amount_term_log, total_income_log]])



prediction = model.predict(features)

if prediction[0] == 1:
    st.success("🎉 Loan Approved")
else:
    st.error("❌ Loan Not Approved")

