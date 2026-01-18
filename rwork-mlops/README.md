# Online Retail MLOps Project (Project 7)

## Overview
This repository contains an end-to-end MLOps project based on the **UCI Online Retail dataset**.
The project is completed as part of **Project 7 – Model Deployment & Monitoring**.

The work is divided into two major parts:
1. Original model development and preprocessing
2. Model deployment using R Plumber and Docker

---

## Original Work (Model Development)
This repository is forked from the original work developed by my teammate.

**Original Author:** Mr.H R Harigopal
**Original Repository:** https://github.com/MrHARI76/online_retail_r

### Original Contributions
- Data preprocessing and cleaning
- Feature engineering
- Customer segmentation using **K-Means clustering**
- Model training
- Saving trained model artifacts

The trained model artifact is stored at:
outputs/kmeans_artifact.rds

yaml
Copy code

---

## My Contributions (Deployment & MLOps)
I extended the original project by implementing the deployment and monitoring components using MLOps principles.

### Added Features
- REST API using **R Plumber**
- Dockerized deployment
- Health monitoring endpoint
- Swagger API documentation
- Version-controlled deployment workflow

---

## Technology Stack
- **Programming Language:** R
- **Model:** K-Means Clustering
- **API Framework:** Plumber
- **Containerization:** Docker
- **Version Control:** Git & GitHub
- **Dataset:** UCI Online Retail Dataset

---

## Project Structure
online_retail_r/
├── scripts/
│ ├── api.R
│ ├── monitor.R
├── outputs/
│ └── kmeans_artifact.rds
├── logs/
├── requirements.txt
├── Dockerfile
└── README.md

yaml
Copy code

---

## API Endpoints

### Health Check
GET /health

pgsql
Copy code

**Response**
```json
{
  "status": ["API running"]
}
Docker Deployment
Build Docker Image
bash
Copy code
docker build -t online-retail-api .
Run Docker Container
bash
Copy code
docker run -p 8000:8000 online-retail-api
Accessing the API
Health Endpoint:
http://localhost:8000/health

Swagger Documentation:
http://localhost:8000/__docs__/

Monitoring
Basic monitoring is implemented using:

API health endpoint

Runtime logs inside the Docker container

Version Control Workflow
Original model development maintained in upstream repository

Deployment work implemented in branch: r-plumber-docker

Changes pushed safely without affecting original work

Conclusion
This project demonstrates a complete MLOps workflow including model development,
API deployment, containerization, and basic monitoring.

Authors
Original Work: Mr H R Harigopal
MSc Data Science

Deployment & MLOps:Krishnaprasad P
MSc Data Science

