import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def create_rfm(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert transaction data into customer-level RFM features
    """

    try:
        logging.info("RFM feature engineering started")

        snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

        rfm = df.groupby("CustomerID").agg({
            "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
            "InvoiceNo": "count",
            "UnitPrice": "sum"
        })

        rfm.columns = ["Recency", "Frequency", "Monetary"]

        logging.info("RFM feature engineering completed")
        return rfm

    except Exception as e:
        logging.error(f"RFM failed: {e}")
        raise RuntimeError("Feature engineering failed safely")
