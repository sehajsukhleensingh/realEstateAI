# realEstateAI 
    an end-to-end machine learning application that predicts property prices, analyzes market trends, provides insights and recommends properties based on user preferences.
    This project demonstrates the complete data science workflow — from manual data collection to model training, analytics, and visualization — showcasing strong hands-on skills in core machine learning and data analytics.

# 1. Price Prediction Module
	•	Predicts property prices using XGBoost Regression.
	•	Considers key features like area, sector, number of bedrooms, bathrooms, and property type.
	•	Handles complex, non-linear relationships with high accuracy.

# 2. Analytics Module
	•	Visualizes property price trends across different sectors and areas.
	•	Analyzes how prices vary with different property features.
	•	Helps users understand the broader market dynamics.

# 3. Insights Module
	•	Provides feature-wise insights, such as how much price increases with an additional bedroom or increased area.
	•	Offers explainability and interpretability to model predictions.

# 4. Recommender System
	•	Suggests similar or nearby properties based on user preferences.
	•	Uses similarity-based logic to recommend top listings with best-value pricing.

# Workflow Overview
	1.	Data Collection – Manually scraped and compiled property data from multiple real estate listings to ensure authenticity, variety, and real-world diversity. The dataset was created entirely from scratch, reflecting genuine market conditions.

	2.	Data Cleaning & Preprocessing – Performed comprehensive cleaning and preprocessing, including removal of duplicates, handling of missing values, feature encoding, and transformation of raw attributes into a machine-readable format. Implemented robust feature engineering to enhance model accuracy.

	3.	Model Training – Implemented and fine-tuned the XGBoost Regressor, optimized hyperparameters, and validated the model to achieve strong predictive performance for property price estimation.

	4.	Analysis & Visualization – Developed rich analytics and insights dashboards to interpret how property prices vary across sectors, locations, and features such as area, bedrooms, and bathrooms. Provided interpretable visual trends and market patterns.

	5.	Recommender System – Built a similarity-based recommendation engine that suggests top property options based on user-selected preferences and location proximity. Helps users identify the best-value properties efficiently.

	6.	Interface Integration – Designed a seamless and interactive interface using Streamlit, integrating all modules — prediction, analytics, insights, and recommendations — under a single unified user experience.
    
	7.	Deployment – Deployed the entire application on AWS Cloud, ensuring high availability, scalability, and smooth end-user accessibility from any device.