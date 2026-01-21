import streamlit as st
import requests
import random

API_URL="http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📉",
    layout="centered"

)

st.markdown("<h1 style='text-align: center;'>📊 Customer Churn Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Predict whether a customer is likely to leave your service</p>", unsafe_allow_html=True)

st.divider()

HIGH_RISK_ACTIONS = [
    "Offer a loyalty discount or cashback",
    "Provide a personalized retention plan",
    "Assign a dedicated support agent",
    "Upgrade service quality at a lower cost",
    "Offer long-term contract incentives"
]

MEDIUM_RISK_ACTIONS = [
    "Send satisfaction survey",
    "Offer minor discounts",
    "Provide service usage tips",
    "Promote bundle offers"
]

LOW_RISK_ACTIONS = [
    "Offer referral rewards",
    "Thank the customer for loyalty",
    "Upsell premium features",
    "Invite to loyalty program"
]

st.subheader("🧾 Customer Information")

col1, col2 = st.columns(2)

with col1:
    tenure = st.number_input("Tenure (Months)", min_value=0, max_value=100, value=12)
    monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, value=70.5)
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

with col2:
    total_charges = st.number_input("Total Charges ($)", min_value=0.0, value=850.0)
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    senior = st.selectbox("Senior Citizen", ["Yes", "No"])

payment = st.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)

st.divider()

if st.button("🔮 Predict Churn", use_container_width=True):

    payload = {
        "Tenure_Months": tenure,
        "Monthly_Charges": monthly_charges,
        "Total_Charges": total_charges,
        "Contract": contract,
        "Internet_Service": internet,
        "Payment_Method": payment,
        "Senior_Citizen": senior
    }

    try:
        response = requests.post(API_URL, json=payload)
        result = response.json()

        churn = result["Churn_Prediction"]
        churn_prob = result["Churn_Probability"]

        if churn_prob > 0.7:
            st.error("🔴 High Risk: Customer is likely to *CHURN*")
            st.markdown("*Recommended Action:*")
            st.markdown(f"- {random.choice(HIGH_RISK_ACTIONS)}")

        elif churn_prob > 0.4:
            st.warning("🟡 Medium Risk: Customer may *CHURN*")
            st.markdown("*Recommended Action:*")
            st.markdown(f"- {random.choice(MEDIUM_RISK_ACTIONS)}")

        else:
            st.success("🟢 Low Risk: Customer is likely to *STAY*")
            st.markdown("*Recommended Action:*")
            st.markdown(f"- {random.choice(LOW_RISK_ACTIONS)}")

    except Exception as e:
        st.error(f"Error: {e}")

st.divider()