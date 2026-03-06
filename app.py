import streamlit as st
import pickle
import numpy as np

# Background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1e3a8a;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo
st.image("logo.png", width=200)

# Load model
model = pickle.load(open("model.pkl","rb"))

st.title("Customer Churn Prediction")
st.write("Enter customer details below")

# Load trained model
model = pickle.load(open("model.pkl","rb"))

st.title("Customer Churn Prediction")

st.write("Enter Customer Details")

# Inputs
# Gender
gender = st.selectbox("Gender", ["Female", "Male"])
gender = 1 if gender == "Male" else 0

# Senior Citizen
SeniorCitizen = st.selectbox("Senior Citizen", ["No", "Yes"])
SeniorCitizen = 1 if SeniorCitizen == "Yes" else 0

# Partner
Partner = st.selectbox("Partner", ["No", "Yes"])
Partner = 1 if Partner == "Yes" else 0

# Dependents
Dependents = st.selectbox("Dependents", ["No", "Yes"])
Dependents = 1 if Dependents == "Yes" else 0

# Tenure
tenure = st.number_input("Tenure (months)", min_value=0)

# Phone Service
PhoneService = st.selectbox("Phone Service", ["No", "Yes"])
PhoneService = 1 if PhoneService == "Yes" else 0

# Multiple Lines
MultipleLines = st.selectbox("Multiple Lines", ["No", "Yes"])
MultipleLines = 1 if MultipleLines == "Yes" else 0

# Internet Service
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
InternetService = {"DSL":0, "Fiber optic":1, "No":2}[InternetService]

# Online Security
OnlineSecurity = st.selectbox("Online Security", ["No", "Yes"])
OnlineSecurity = 1 if OnlineSecurity == "Yes" else 0

# Online Backup
OnlineBackup = st.selectbox("Online Backup", ["No", "Yes"])
OnlineBackup = 1 if OnlineBackup == "Yes" else 0

# Device Protection
DeviceProtection = st.selectbox("Device Protection", ["No", "Yes"])
DeviceProtection = 1 if DeviceProtection == "Yes" else 0

# Tech Support
TechSupport = st.selectbox("Tech Support", ["No", "Yes"])
TechSupport = 1 if TechSupport == "Yes" else 0

# Streaming TV
StreamingTV = st.selectbox("Streaming TV", ["No", "Yes"])
StreamingTV = 1 if StreamingTV == "Yes" else 0

# Streaming Movies
StreamingMovies = st.selectbox("Streaming Movies", ["No", "Yes"])
StreamingMovies = 1 if StreamingMovies == "Yes" else 0

# Contract
Contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
Contract = {"Month-to-month":0, "One year":1, "Two year":2}[Contract]

# Paperless Billing
PaperlessBilling = st.selectbox("Paperless Billing", ["No", "Yes"])
PaperlessBilling = 1 if PaperlessBilling == "Yes" else 0

# Payment Method
PaymentMethod = st.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)
PaymentMethod = {
    "Electronic check":0,
    "Mailed check":1,
    "Bank transfer (automatic)":2,
    "Credit card (automatic)":3
}[PaymentMethod]

# Monthly Charges
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0)

# Total Charges
TotalCharges = st.number_input("Total Charges", min_value=0.0)

# Prediction Button
if st.button("Predict"):

    input_data = np.array([[gender,SeniorCitizen,Partner,Dependents,tenure,
    PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,
    DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,
    PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Customer Will Churn")
    else:
        st.success("Customer Will Stay")