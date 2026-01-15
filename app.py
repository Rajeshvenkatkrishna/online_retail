from flask import Flask, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load model artifacts
rfm = pd.read_csv("models/rfm_output.csv")

@app.route("/")
def home():
    return jsonify({
        "message": "Customer Segmentation API is running"
    })

@app.route("/clusters")
def clusters():
    return rfm["Cluster"].value_counts().to_dict()

@app.route("/customers")
def customers():
    return rfm.head(10).to_dict(orient="records")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
