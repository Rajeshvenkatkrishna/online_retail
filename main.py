from src.load_data import load_data
from src.validate_data import validate_schema
from src.preprocess import preprocess
from src.feature_engineering import create_rfm
from src.train import train_model
from src.evaluate import evaluate_model
from src.visualize import visualize_clusters



def main():
    print("=== MLOps PIPELINE STARTED ===")

    # Load data
    df = load_data()

    # Validate schema
    validate_schema(df)

    # Preprocess
    df = preprocess(df)

    # Feature engineering
    rfm = create_rfm(df)

    # Train model
    model, scaler, rfm_scaled = train_model(rfm)

    # Evaluate model (ALL METRICS HERE)
    metrics = evaluate_model(rfm_scaled, model.labels_)

    visualize_clusters(rfm_scaled, model.labels_, rfm)


    print("=== PIPELINE COMPLETED SUCCESSFULLY ===")
    print("Evaluation Metrics:")
    for k, v in metrics.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
