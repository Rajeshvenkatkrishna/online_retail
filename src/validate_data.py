EXPECTED_COLUMNS = [
    'InvoiceNo', 'StockCode', 'Description',
    'Quantity', 'InvoiceDate', 'UnitPrice',
    'CustomerID', 'Country'
]

def validate_schema(df):
    missing = set(EXPECTED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    return True
