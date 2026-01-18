from datetime import timedelta


def create_rfm(df):
    snapshot_date = df["InvoiceDate"].max() + timedelta(days=1)

    rfm = (
        df.groupby("CustomerID")
        .agg({
            "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
            "InvoiceNo": "nunique",
            "TotalAmount": "sum"
        })
        .reset_index()
    )

    rfm.columns = ["CustomerID", "Recency", "Frequency", "Monetary"]

    return rfm
