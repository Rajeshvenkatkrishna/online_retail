from src.data_ingestion import load_data
from src.data_validation import load_schema, validate_schema
from src.preprocessing import clean_data
from src.feature_engineering import (
    add_total_amount,
    aggregate_customer_data,
    create_target
)

DATA_PATH = "data/raw/Online Retail.xlsx"
SCHEMA_PATH = "schemas/data_schema.yaml"


def main():
    print("Loading data...")
    df = load_data(DATA_PATH)

    print("Loading schema...")
    schema = load_schema(SCHEMA_PATH)

    print("Validating raw dataset structure...")
    validate_schema(df, schema)

    print("Cleaning data...")
    df_clean = clean_data(df)

    print("Adding features...")
    df_with_amount = add_total_amount(df_clean)

    print("Aggregating to customer level...")
    customer_df = aggregate_customer_data(df_with_amount)

    print("Creating target variable...")
    final_df = create_target(customer_df)

    print(final_df.head())
    print("STEP-2 COMPLETED SUCCESSFULLY")


if __name__ == "__main__":
    main()
