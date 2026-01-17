from src.load_data import load_data
from src.validate_data import validate_schema
from src.preprocess import preprocess
from src.feature_engineering import create_rfm
from src.train import train_model
from src.evaluate import evaluate_model

def main():
    print("PIPELINE STARTED")

    # Step 1: Load data
    df = load_data()

    # Step 2: Validate schema (TC1)
    validate_schema(df)

    # Step 3: Preprocess data
    df = preprocess(df)

    # Step 4: Feature engineering
    rfm = create_rfm(df)

    # Step 5: Train model (TC2)
    model, scaler, rfm_scaled = train_model(rfm)

    # Step 6: Evaluate model (TC3)
    score = evaluate_model(rfm_scaled, model.labels_)

    print("PIPELINE COMPLETED SUCCESSFULLY")
    print("Final Silhouette Score:", score)

if __name__ == "__main__":
    main()
