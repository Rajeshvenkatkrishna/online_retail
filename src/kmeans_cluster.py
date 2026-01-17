from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pickle
import os

def run_kmeans(rfm, k=3):
    features = ["Recency", "Frequency", "Monetary"]

    scaler = StandardScaler()
    scaled = scaler.fit_transform(rfm[features])

    kmeans = KMeans(n_clusters=k, random_state=42)
    rfm["Cluster"] = kmeans.fit_predict(scaled)

    os.makedirs("models", exist_ok=True)

    with open("models/kmeans.pkl", "wb") as f:
        pickle.dump(kmeans, f)

    with open("models/scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)

    return rfm
