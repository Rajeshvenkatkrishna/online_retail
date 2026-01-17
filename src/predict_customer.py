import numpy as np
import joblib

# ---------------------------------------------------
# STEP 1: Load trained model and scaler
# ---------------------------------------------------
kmeans_model = joblib.load("artifacts/kmeans_model.pkl")
scaler = joblib.load("artifacts/scaler.pkl")

# ---------------------------------------------------
# STEP 2: Define cluster meanings (BUSINESS LOGIC)
# ---------------------------------------------------
cluster_info = {
    0: {
        "type": "Low-Value Customer",
        "reason": "Customer purchases rarely and spends very little."
    },
    1: {
        "type": "High-Value Customer",
        "reason": "Customer purchases frequently, spends a lot, and has purchased recently."
    },
    2: {
        "type": "Medium-Value Customer",
        "reason": "Customer shows average purchasing behavior."
    },
    3: {
        "type": "New / At-Risk Customer",
        "reason": "Customer has low frequency or is becoming inactive."
    }
}

# ---------------------------------------------------
# STEP 3: Take new customer input
# ---------------------------------------------------
def get_new_customer_input():
    recency = float(input("Enter days since last purchase (Recency): "))
    frequency = float(input("Enter total number of purchases (Frequency): "))
    monetary = float(input("Enter total amount spent (Monetary): "))

    return np.array([[recency, frequency, monetary]])

# ---------------------------------------------------
# STEP 4: Predict customer cluster
# ---------------------------------------------------
def predict_customer():
    customer_rfm = get_new_customer_input()

    # Apply same scaling used during training
    customer_scaled = scaler.transform(customer_rfm)

    # Predict cluster
    cluster_id = kmeans_model.predict(customer_scaled)[0]

    # Get business explanation
    customer_type = cluster_info[cluster_id]["type"]
    explanation = cluster_info[cluster_id]["reason"]

    print("\n----- PREDICTION RESULT -----")
    print("Predicted Cluster ID:", cluster_id)
    print("Customer Type:", customer_type)
    print("Explanation:", explanation)

# ---------------------------------------------------
# STEP 5: Run prediction
# ---------------------------------------------------
if __name__ == "__main__":
    predict_customer()
