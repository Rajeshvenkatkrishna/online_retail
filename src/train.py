import logging
import os
import joblib
import mlflow
import mlflow.sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

logging.basicConfig(level=logging.INFO)

def train_model(rfm_df):
    """
    Train KMeans clustering model
    """
    try:
        logging.info("Model training started")

        # -------------------------------
        # Scaling
        # -------------------------------
        scaler = StandardScaler()
        rfm_scaled = scaler.fit_transform(rfm_df)

        # -------------------------------
        # Model training
        # -------------------------------
        model = KMeans(
            n_clusters=4,
            random_state=42
        )
        model.fit(rfm_scaled)

        # -------------------------------
        # CREATE ARTIFACTS DIRECTORY
        # -------------------------------
        os.makedirs("artifacts", exist_ok=True)

        # -------------------------------
        # SAVE LOCAL FILES (IMPORTANT)
        # -------------------------------
        joblib.dump(model, "artifacts/kmeans_model.pkl")
        joblib.dump(scaler, "artifacts/scaler.pkl")

        # -------------------------------
        # MLFLOW TRACKING
        # -------------------------------
        with mlflow.start_run():
            mlflow.log_param("algorithm", "KMeans")
            mlflow.log_param("clusters", 4)
            mlflow.log_param("random_state", 42)

            mlflow.sklearn.log_model(model, "kmeans_model")
            mlflow.sklearn.log_model(scaler, "scaler")

        logging.info("Model training completed")

        return model, scaler, rfm_scaled

    except Exception as e:
        logging.error(f"Training failed: {e}")
        raise RuntimeError("Training failed safely")
