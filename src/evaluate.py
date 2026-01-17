import logging
from sklearn.metrics import (
    silhouette_score,
    calinski_harabasz_score,
    davies_bouldin_score
)
import mlflow

logging.basicConfig(level=logging.INFO)

def evaluate_model(X, labels):
    """
    Evaluate KMeans clustering using multiple metrics
    """

    logging.info("Evaluating clustering performance")

    silhouette = silhouette_score(X, labels)
    calinski = calinski_harabasz_score(X, labels)
    davies = davies_bouldin_score(X, labels)

    # Log to MLflow
    mlflow.log_metric("silhouette_score", silhouette)
    mlflow.log_metric("calinski_harabasz_index", calinski)
    mlflow.log_metric("davies_bouldin_index", davies)

    logging.info(f"Silhouette Score: {silhouette}")
    logging.info(f"Calinski-Harabasz Index: {calinski}")
    logging.info(f"Davies-Bouldin Index: {davies}")

    return {
        "silhouette": silhouette,
        "calinski_harabasz": calinski,
        "davies_bouldin": davies
    }
