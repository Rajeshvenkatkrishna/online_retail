import streamlit as st
import numpy as np
import joblib

# -------------------------------
# Load trained model and scaler
# -------------------------------
kmeans_model = joblib.load("artifacts/kmeans_model.pkl")
scaler = joblib.load("artifacts/scaler.pkl")

# -------------------------------
# Cluster interpretation
# -------------------------------
cluster_info = {
    0: ("Low-Value Customer",
        "Purchases rarely and spends very little."),
    1: ("High-Value Customer",
        "Purchases frequently, spends a lot, and recently active."),
    2: ("Medium-Value Customer",
        "Shows average purchasing behavior."),
    3: ("New / At-Risk Customer",
        "Low frequency or becoming inactive.")
}

# -------------------------------
# UI Layout
# -------------------------------
st.set_page_config(page_title="Customer Segmentation", layout="centered")

st.title("Customer Segmentation System")
st.write(
    "This system predicts customer value using **RFM-based KMeans clustering**."
)

st.divider()

# -------------------------------
# Input form
# -------------------------------
with st.form("customer_form"):
    recency = st.number_input(
        "Recency (days since last purchase)",
        min_value=0.0,
        step=1.0
    )

    frequency = st.number_input(
        "Frequency (number of purchases)",
        min_value=0.0,
        step=1.0
    )

    monetary = st.number_input(
        "Monetary (total amount spent)",
        min_value=0.0,
        step=100.0
    )

    submitted = st.form_submit_button("Predict Customer Segment")

# -------------------------------
# Prediction logic
# -------------------------------
if submitted:
    customer_data = np.array([[recency, frequency, monetary]])
    customer_scaled = scaler.transform(customer_data)
    cluster_id = int(kmeans_model.predict(customer_scaled)[0])

    customer_type, explanation = cluster_info[cluster_id]

    st.success(f"Customer Segment: {customer_type}")
    st.write(f"**Cluster ID:** {cluster_id}")
    st.write(f"**Explanation:** {explanation}")
