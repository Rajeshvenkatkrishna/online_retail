import pandas as pd
import yaml


def load_schema(schema_path: str) -> dict:
    """Load schema YAML file"""
    with open(schema_path, "r") as file:
        schema = yaml.safe_load(file)
    return schema


def validate_schema(df: pd.DataFrame, schema: dict) -> None:
    """
    Validates DataFrame against schema.
    Raises error if validation fails.
    """

    schema_columns = schema["columns"]

    # 1. Check column existence
    for column in schema_columns:
        if column not in df.columns:
            raise ValueError(f"Missing column: {column}")

    # 2. Check data types and rules
    for column, rules in schema_columns.items():
        col_data = df[column]

        # Nullability check
        if not rules.get("nullable", True):
            if col_data.isnull().any():
                raise ValueError(f"Null values found in non-nullable column: {column}")

        # Type checks
        expected_type = rules["type"]

        if expected_type == "int" and not pd.api.types.is_integer_dtype(col_data):
            raise TypeError(f"{column} must be integer")

        if expected_type == "float" and not pd.api.types.is_float_dtype(col_data):
            raise TypeError(f"{column} must be float")

        if expected_type == "datetime" and not pd.api.types.is_datetime64_any_dtype(col_data):
            raise TypeError(f"{column} must be datetime")

        # Range checks
        if "min" in rules:
            if (col_data.dropna() < rules["min"]).any():
                raise ValueError(f"{column} contains values below minimum")

    print(" Dataset schema matches specification")
