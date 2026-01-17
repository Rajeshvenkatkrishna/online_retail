def label_clusters(rfm):
    cluster_mean = rfm.groupby("Cluster")["Monetary"].mean()
    high_value_cluster = cluster_mean.idxmax()

    rfm["Target"] = rfm["Cluster"].apply(
        lambda x: 1 if x == high_value_cluster else 0
    )

    return rfm
