import pandas as pd


def add_total_amount(df: pd.DataFrame) -> pd.DataFrame:
    df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]
    return df


def aggregate_customer_data(df: pd.DataFrame) -> pd.DataFrame:
    customer_df = df.groupby("CustomerID").agg(
        TotalSpend=("TotalAmount", "sum"),
        TotalQuantity=("Quantity", "sum"),
        TransactionCount=("InvoiceNo", "nunique")
    ).reset_index()

    return customer_df


def create_target(customer_df: pd.DataFrame) -> pd.DataFrame:
    median_spend = customer_df["TotalSpend"].median()
    customer_df["Target"] = (customer_df["TotalSpend"] > median_spend).astype(int)
    return customer_df
