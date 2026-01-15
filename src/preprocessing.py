import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans raw retail data.
    Removes invalid transactions.
    """

    # Remove cancelled / invalid transactions
    df = df[df["Quantity"] > 0]
    df = df[df["UnitPrice"] > 0]

    # Convert InvoiceDate properly
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    return df
