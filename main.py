from src.data_ingestion import load_data
from src.data_validation import load_schema, validate_schema
from src.preprocessing import clean_data

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

    print("Raw data cleaned successfully")

if __name__ == "__main__":
    main()
