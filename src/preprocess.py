import pandas as pd
import logging

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the Online Retail dataset.
    Steps:
    1. Remove cancelled transactions
    2. Drop missing CustomerID
    3. Remove zero/negative quantity
    4. Convert InvoiceDate to datetime
    """

    try:
        logging.info("Starting preprocessing")

        # 1. Remove cancelled orders
        df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

        # 2. Drop missing CustomerID
        df = df.dropna(subset=["CustomerID"])

        # 3. Remove invalid quantities
        df = df[df["Quantity"] > 0]

        # 4. Convert InvoiceDate to datetime
        df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

        logging.info("Preprocessing completed successfully")
        return df

    except Exception as e:
        logging.error(f"Preprocessing failed: {e}")
        raise RuntimeError("Preprocessing step failed safely")
