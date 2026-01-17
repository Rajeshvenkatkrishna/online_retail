from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# -----------------------------
# Load model & scaler once
# -----------------------------
kmeans_model = joblib.load("artifacts/kmeans_model.pkl")
scaler = joblib.load("artifacts/scaler.pkl")

# -----------------------------
# Create FastAPI app
# -----------------------------
app = FastAPI(title="Customer Segmentation API")

# -----------------------------
# Cluster interpretation
# -----------------------------
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

# -----------------------------
# Input schema
# -----------------------------
class CustomerInput(BaseModel):
    recency: float
    frequency: float
    monetary: float

# -----------------------------
# Health check
# -----------------------------
@app.get("/")
def home():
    return {"status": "API is running"}

# -----------------------------
# Prediction endpoint
# -----------------------------
@app.post("/predict")
def predict_customer(data: CustomerInput):

    customer_data = np.array([[data.recency, data.frequency, data.monetary]])
    customer_scaled = scaler.transform(customer_data)
    cluster_id = int(kmeans_model.predict(customer_scaled)[0])

    customer_type, explanation = cluster_info[cluster_id]

    return {
        "cluster_id": cluster_id,
        "customer_type": customer_type,
        "explanation": explanation
    }
