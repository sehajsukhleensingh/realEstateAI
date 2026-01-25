# realEstateAI
An end-to-end **machine learning application** that predicts property prices, analyzes market trends, provides insights, and recommends properties based on user preferences.  

This project demonstrates the complete data science workflow — from **manual data collection to model training, analytics, and visualization** — showcasing strong hands-on skills in **core machine learning and data analytics**.

---

## 🐳 Run the Full System with Docker

This project uses a **two-service architecture**:

- **Frontend** → Streamlit dashboard (UI)  
- **Backend** → FastAPI server (ML models + analytics APIs)

You only need the Docker images and the compose file — no source code setup required.

###  Step 1 — Download the Docker Compose File

Download the `docker-compose.yml` file and place it in an empty folder.

```bash
curl -O https://raw.githubusercontent.com/sehajsukhleensingh/realEstateAI/main/docker-compose.yml
```

###  Step 2 — Pull the docker images 

```bash
docker pull sehajsukhleensingh/realestateai:v3
docker pull sehajsukhleensingh/realestateai-api:v1
```

###  Step 3 - Run the command 

```bash
docker compose up 
```

---

## Price Prediction Module
- Predicts property prices using **XGBoost Regression**.
- Considers key features like area, sector, number of bedrooms, bathrooms, and property type.
- Handles complex, non-linear relationships with high accuracy.

---

## Analytics Module
- Visualizes property price trends across different sectors and areas.
- Analyzes how prices vary with different property features.
 <p align="center">
  <img src="https://github.com/sehajsukhleensingh/realEstateAI/blob/f6772a47af4a5f9f80aedd0c31872973f23ffe53/images/Screenshot%202025-10-29%20at%2012.37.25%E2%80%AFPM.png" width="370">
  <img src="https://github.com/sehajsukhleensingh/realEstateAI/blob/f6772a47af4a5f9f80aedd0c31872973f23ffe53/images/Screenshot%202025-10-29%20at%2012.37.41%E2%80%AFPM.png" width="370">
  <img src="https://github.com/sehajsukhleensingh/realEstateAI/blob/f6772a47af4a5f9f80aedd0c31872973f23ffe53/images/Screenshot%202025-10-29%20at%2012.37.51%E2%80%AFPM.png" width="370">
</p>

- Helps users understand broader **market dynamics**

---

## Insights Module
- Provides **feature-wise insights**, such as how much price increases with an additional bedroom or larger area.
- Offers **explainability** and **interpretability** for model predictions.

---

## Recommender System
- Suggests similar or nearby properties based on **user preferences**.
- Uses similarity-based logic to recommend **top listings** with best-value pricing.

---
## 🔌 API-First Machine Learning Design

The core ML logic is exposed via **dedicated API endpoints using FastAPI**, making the system usable beyond the UI.

### API Capabilities
- Accepts structured JSON input for properties
- Performs preprocessing and feature transformation
- Returns:
  - Predicted property price
  - Recommendation results (where applicable)
- Decoupled from UI for:
  - Web integration
  - Mobile apps
  - Future microservices

This mirrors **real-world ML deployment patterns**, where models are consumed via APIs, not notebooks.

---

##  Workflow Overview

1. **Data Collection**  
   - Manually scraped and compiled property data from multiple real estate listings to ensure authenticity and diversity.  
   - The dataset was created entirely from scratch, reflecting genuine market conditions.

2. **Data Cleaning & Preprocessing**  
   - Removed duplicates, handled missing values, encoded categorical features, and engineered new features to enhance model accuracy.

3. **Model Training**  
   - Trained and fine-tuned an **XGBoost Regressor** with hyperparameter optimization to achieve strong predictive performance.

4. **Analysis & Visualization**  
   - Built rich analytics dashboards to interpret property price variations across different regions and features.

5. **Recommender System**  
   - Designed a similarity-based recommendation engine suggesting best-value properties based on preferences and location proximity.

6. **Interface Integration**  
   - Integrated all modules using **Streamlit**, creating a unified interactive experience for users.

7. **Deployment**  
   - Deployed on **streamlit cloud** for availability and seamless accessibility.

---

##  Tech Stack
- Python
- Pandas, NumPy, Scikit-learn, XGBoost
- Matplotlib, Seaborn, Plotly
- Streamlit
- requests
- beautifulSoup
- selenium
---

##  Results
Achieved high model accuracy and interpretability with visually rich insights into real estate market behavior.

---

##  Contact
Created by **Sehaj Sukhleen Singh**  
Feel free to connect via [GitHub](https://github.com/sehajsukhleensingh)
