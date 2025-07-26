# 🍷 Wine Quality Dashboard – Portfolio Project

## 🚀 Project Overview

This project showcases a production-ready architecture for a data-driven, machine learning-enabled dashboard using wine ratings. It combines modern tools and best practices for backend development, model deployment, data visualization, testing, and container orchestration.

The dashboard enables:
- 📊 Exploration of wine quality distributions based on chemical features
- 🔮 ML predictions for wine quality using freshly evaluated data
- 🛠️ Separation of services with Docker and Kubernetes
- 🧪 CI/CD with GitHub Actions and testing via Pytest
- 🎓 Practical experience with MLflow, BentoML, FastAPI, and Streamlit

The final system simulates a real-world environment where data arrives via APIs, predictions are served independently, and users can visualize or explore the results in an interactive UI.

---

## 🧭 Architecture Diagram

![architecture-diagram](/resources/img/architecture%20diagram.png)

### Main Components:
- **FastAPI Service** – Connects to the SQL database and handles core APIs
- **ML Training** – Uses MLflow to experiment and log model artifacts
- **Inference API** – BentoML-based service serving trained model
- **Streamlit UI** – Dashboard visualizing ratings & predictions
- **Database** – Stores processed data split into Wine and EvaluatedWine tables
- **Validation Data** – CSV fed directly to inference pipeline
- **CI/CD** – GitHub Actions automates testing, linting, and deployment
- **Kubernetes** – Optional deployment layer for showcasing scalability

---

## ✅ Scrum Sprint Checklist

This checklist tracks your development progress using Scrum methodology. Tasks are grouped by sprints and ordered sequentially.

### 🏁 Sprint 0: Project Skeleton & Planning – **Completed ✅**
- [x] Define project structure (modular directories, naming conventions)
- [x] Set up `.env`, `pyproject.toml`, and configs
- [x] Prepare initial exploratory notebook
- [x] Confirm code separation across loaders, models, routers
- [x] Provide architecture diagram
- [x] Outline product goal and scope

---

### 📆 Sprint 1: Data API Foundation
- [ ] Finalize FastAPI routers and endpoints
- [ ] Connect Wine and EvaluatedWine models to DB
- [ ] Set up SQLAlchemy with Alembic migrations
- [ ] Complete initial unit tests for loader modules

### 🐳 Sprint 2: Docker & Local Orchestration
- [ ] Containerize FastAPI + Database
- [ ] Implement Docker Compose for service orchestration
- [ ] Validate local inter-service connectivity

### 📊 Sprint 3: Static Dashboard Panels
- [ ] Design initial Streamlit layouts
- [ ] Visualize wine rating distribution by feature
- [ ] Test static charts with mock data
- [ ] Implement data endpoints for dashboard
    - Endpoint to list available features (/features)
    - Endpoint to return distribution data for a selected feature (/distributions/{feature})




### 🎓 Sprint 4: ML Pipeline Integration
- [ ] Train model and log to MLflow
- [ ] Save metrics and experiment configs
- [ ] Validate feature engineering pipeline

### 📡 Sprint 5: Model Serving via BentoML
- [ ] Containerize inference API separately
- [ ] Serve predictions from validation CSV
- [ ] Expose prediction endpoint via REST

### 🧠 Sprint 6: Dashboard Prediction Panel
- [ ] Load new evaluations from CSV
- [ ] Query BentoML API for predictions
- [ ] Display predictions in dashboard UI

### ⚙️ Sprint 7: CI/CD Integration
- [ ] Add Pytest coverage enforcement
- [ ] Integrate GitHub Actions for testing and builds
- [ ] Document automated workflows

### 📦 Sprint 8: Kubernetes Deployment (Optional)
- [ ] Write manifests for FastAPI, dashboard, and inference
- [ ] Deploy locally or in the cloud
- [ ] Record or document deployment steps

---

## 📝 Next Steps
- Refine interactive components of the dashboard
- Increase test coverage for ML components
- Create documentation assets (usage flow, screenshots)
- Record video demo or deploy public instance (optional)

---

Feel free to contribute or explore this repo as part of my portfolio. Cheers! 🍷