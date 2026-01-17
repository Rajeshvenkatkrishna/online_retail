import os
import matplotlib.pyplot as plt
import seaborn as sns
import mlflow
from sklearn.decomposition import PCA
import pandas as pd


def visualize_clusters(rfm_scaled, labels, rfm_df):
    os.makedirs("plots", exist_ok=True)

    # -----------------------------
    # 1. PCA CLUSTER PLOT
    # -----------------------------
    pca = PCA(n_components=2, random_state=42)
    components = pca.fit_transform(rfm_scaled)

    pca_df = pd.DataFrame({
        "PC1": components[:, 0],
        "PC2": components[:, 1],
        "Cluster": labels
    })

    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        data=pca_df,
        x="PC1",
        y="PC2",
        hue="Cluster",
        palette="tab10"
    )
    plt.title("PCA Projection of Customer Clusters")
    plt.tight_layout()

    pca_path = "plots/pca_clusters.png"
    plt.savefig(pca_path)
    plt.close()

    mlflow.log_artifact(pca_path)

    # -----------------------------
    # 2. CLUSTER SIZE DISTRIBUTION
    # -----------------------------
    plt.figure(figsize=(6, 4))
    sns.countplot(x=labels)
    plt.title("Customers per Cluster")
    plt.xlabel("Cluster")
    plt.ylabel("Count")
    plt.tight_layout()

    size_path = "plots/cluster_distribution.png"
    plt.savefig(size_path)
    plt.close()

    mlflow.log_artifact(size_path)

    # -----------------------------
    # 3. RFM MEAN PER CLUSTER
    # -----------------------------
    rfm_clustered = rfm_df.copy()
    rfm_clustered["Cluster"] = labels

    cluster_means = rfm_clustered.groupby("Cluster").mean()

    cluster_means.plot(kind="bar", figsize=(8, 5))
    plt.title("Average RFM Values per Cluster")
    plt.tight_layout()

    rfm_path = "plots/rfm_cluster_means.png"
    plt.savefig(rfm_path)
    plt.close()

    mlflow.log_artifact(rfm_path)
