import pandas as pd
from pathlib import Path


def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads raw dataset from disk.

    Parameters:
        file_path (str): Path to raw dataset

    Returns:
        pd.DataFrame: Loaded dataset
    """

    if not Path(file_path).exists():
        raise FileNotFoundError(f"Data file not found at {file_path}")

    df = pd.read_excel(file_path)

    return df
