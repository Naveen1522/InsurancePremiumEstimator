import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("models/premium_model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))

st.set_page_config(page_title="Insurance Premium Estimator", layout="centered")
st.title("Insurance Premium Estimator")

st.markdown("Enter the customer's health and demographic details to estimate the insurance premium.")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("🎂 Age", 18, 80, 30)
    bmi = st.slider("📏 BMI", 15.0, 40.0, 25.0)
    diabetes = st.radio("🩸 Diabetes", [0, 1], format_func=lambda x: "Yes" if x else "No")
    bp = st.radio("🩺 Blood Pressure Problem", [0, 1], format_func=lambda x: "Yes" if x else "No")
    transplant = st.radio("🧬 Any Transplants", [0, 1], format_func=lambda x: "Yes" if x else "No")

with col2:
    chronic = st.radio("📋 Any Chronic Diseases", [0, 1], format_func=lambda x: "Yes" if x else "No")
    allergy = st.radio("🌼 Known Allergies", [0, 1], format_func=lambda x: "Yes" if x else "No")
    cancer = st.radio("🧬 Family History of Cancer", [0, 1], format_func=lambda x: "Yes" if x else "No")
    surgeries = st.slider("🔪 Number of Major Surgeries", 0, 3, 0)

if st.button("🧮 Estimate Premium"):
    # Arrange inputs in correct model order
    features = np.array([[age, bmi, surgeries, diabetes, bp, transplant, chronic, allergy, cancer]])
    scaled_features = scaler.transform(features)
    prediction = model.predict(scaled_features)[0]
    
    st.markdown(
        f"<div style='background-color:#f0f2f6; padding:20px; border-radius:10px; text-align:center;'>"
        f"<h3 style='color:#4B8BBE;'>Estimated Premium: ₹ {round(prediction, 2):,.2f}</h3>"
        "</div>",
        unsafe_allow_html=True
    )