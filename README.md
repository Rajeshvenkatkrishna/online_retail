# Customer Segmentation using MLOps Pipeline

## Project Overview
This project implements an end-to-end MLOps pipeline for customer segmentation using the UCI Online Retail dataset. Customers are grouped using KMeans clustering based on Recency, Frequency, and Monetary (RFM) analysis. The pipeline includes data preprocessing, feature engineering, model training, evaluation, experiment tracking using MLflow, visualization, and deployment using Streamlit and Docker.

## Dataset Description
Dataset: UCI Online Retail Dataset

The dataset contains transactional data from an online retail store. The following columns are used for analysis:
- InvoiceDate
- CustomerID
- Quantity
- UnitPrice

## Objective
- Build a reproducible MLOps pipeline
- Perform customer segmentation using unsupervised learning
- Track experiments and metrics using MLflow
- Visualize clustering results
- Deploy the model using Docker

## Pipeline Workflow
1. Data loading from local storage
2. Schema validation
3. Data preprocessing
4. RFM feature engineering
5. KMeans model training
6. Model evaluation using clustering metrics
7. Cluster visualization
8. Experiment tracking using MLflow
9. Deployment using Streamlit and Docker

## Model and Evaluation
Algorithm used:
- KMeans Clustering

Since this is an unsupervised learning problem, accuracy is not applicable. The following evaluation metrics are used:
- Silhouette Score
- Calinski-Harabasz Index
- Davies-Bouldin Index

A silhouette score around 0.61 indicates good cluster separation for real-world customer data.

## MLflow Tracking
MLflow is used to track:
- Model parameters
- Evaluation metrics
- Trained models
- Visualization artifacts

MLflow ensures reproducibility and allows comparison of different experiment runs.

To start MLflow UI:
mlflow ui

Open in browser:
http://127.0.0.1:5000

## Visualizations
The following visualizations are generated and logged as MLflow artifacts:
- PCA-based cluster visualization
- Customer distribution per cluster
- Average RFM values per cluster

## Deployment
A Streamlit application is created to accept customer RFM values and predict the customer segment. The application is containerized using Docker to ensure portability and environment consistency.

## How to Run the Project

1. Run the training pipeline:
   python main.py

2. Start MLflow UI:
   mlflow ui

3. Build Docker image:
   docker build -t customer-segmentation-ui .

4. Run Docker container:
   docker run -p 8501:8501 customer-segmentation-ui

5. Open the application in browser:
   http://localhost:8501

## Conclusion
This project demonstrates a complete MLOps lifecycle from data preprocessing to deployment. The pipeline is modular, reproducible, and deployable using Docker, following industry-standard MLOps practices.

