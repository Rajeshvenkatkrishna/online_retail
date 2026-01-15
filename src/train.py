import pandas as pd
import numpy as np
from datetime import timedelta
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pickle
import os

# ---------------------------
# Load Data (FIXED)
# ---------------------------
df = pd.read_csv(
    "C:/Users/rajve/Online_retail/Online Retail.csv",
    encoding="utf-8-sig"
)

df.columns = df.columns.str.strip()

# ---------------------------
# Data Cleaning
# ---------------------------
df.dropna(subset=["CustomerID"], inplace=True)
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]

df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"],
    dayfirst=True,
    errors="coerce"
)

df.dropna(subset=["InvoiceDate"], inplace=True)

df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# ---------------------------
# RFM Calculation
# ---------------------------
snapshot_date = df["InvoiceDate"].max() + timedelta(days=1)

rfm = df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
    "InvoiceNo": "nunique",
    "TotalPrice": "sum"
})

rfm.rename(columns={
    "InvoiceDate": "Recency",
    "InvoiceNo": "Frequency",
    "TotalPrice": "Monetary"
}, inplace=True)

# ---------------------------
# Scaling
# ---------------------------
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

# ---------------------------
# K-Means
# ---------------------------
kmeans = KMeans(n_clusters=4, random_state=42)
rfm["Cluster"] = kmeans.fit_predict(rfm_scaled)

# ---------------------------
# Save Artifacts
# ---------------------------
os.makedirs("models", exist_ok=True)

rfm.to_csv("models/rfm_output.csv")

with open("models/kmeans_model.pkl", "wb") as f:
    pickle.dump(kmeans, f)

with open("models/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Training completed successfully")
