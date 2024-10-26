# Car Dheko - Used Car Price Prediction
# Project Overview
Car Dheko - Used Car Price Prediction is a machine learning project aimed at enhancing customer experience and optimizing the used car pricing process. Using a variety of car features such as make, model, year, fuel type, and more, this project creates an interactive Streamlit web application that allows users to input car details and receive an estimated price instantly. This tool benefits both customers and sales representatives by providing accurate price predictions for used cars.

# Skills Demonstrated
Data Cleaning and Preprocessing
Exploratory Data Analysis (EDA)
Machine Learning Model Development
Price Prediction Techniques
Model Evaluation and Optimization
Model Deployment
Streamlit Application Development

# Domain
Automotive Industry
Data Science
Machine Learning
# Problem Statement
# Objective:
As a data scientist at Car Dheko, your goal is to enhance customer satisfaction and streamline the pricing process by developing a machine learning model that predicts used car prices accurately. The model is to be deployed as an interactive Streamlit tool that can be easily accessed and used by customers and sales representatives alike.

# Project Scope
Using historical data on used car prices across various cities, the model will predict prices based on specific car features. The final model will be deployed in a Streamlit web application, allowing users to input car features and instantly receive an estimated price. The project requires comprehensive data processing, feature engineering, model training, evaluation, and deployment.

# Approach
1. Data Processing
Import and Concatenate Data: Load and merge datasets from multiple cities, add a City column, and create a unified dataset.
Handling Missing Values: Use imputation techniques (mean, median, mode) to handle missing values in numerical and categorical columns.
Standardizing Formats: Clean and standardize data formats, e.g., converting "70 kms" to integer values.
Encoding Categorical Variables: Use encoding techniques:
One-Hot Encoding for nominal categorical variables.
Label Encoding for ordinal variables.
Normalizing Numerical Features: Scale features to a standard range using Min-Max Scaling or Standard Scaling.
Outlier Removal: Identify and remove or cap outliers using methods like IQR or Z-score analysis.
2. Exploratory Data Analysis (EDA)
Descriptive Statistics: Summarize data distributions using mean, median, mode, standard deviation, etc.
Data Visualization: Generate visual insights using scatter plots, histograms, box plots, and correlation heatmaps.
Feature Selection: Identify significant features through correlation analysis and feature importance scores.
3. Model Development
Train-Test Split: Split data into training and testing sets (typically 70-30 or 80-20).
Model Selection: Experiment with various machine learning models, such as:
Linear Regression
Decision Trees
Random Forests
Gradient Boosting Machines
Model Training: Train models using cross-validation for robust performance.
Hyperparameter Tuning: Use techniques like Grid Search or Random Search to optimize parameters.
4. Model Evaluation
Performance Metrics: Evaluate models using metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared.
Model Comparison: Compare models to identify the best-performing model based on evaluation metrics.
5. Optimization
Feature Engineering: Create or transform features based on domain knowledge and EDA insights.
Regularization: Apply regularization techniques like Lasso (L1) and Ridge (L2) to prevent overfitting.
6. Deployment
Streamlit Application: Deploy the model in an interactive Streamlit app for real-time price predictions.
User Interface Design: Ensure the application is user-friendly, with clear instructions and error handling for seamless user experience.
# Results
Accurate Price Prediction Model: A machine learning model capable of predicting used car prices with high accuracy.
Comprehensive Analysis: EDA with in-depth insights on customer demographics, purchasing behaviors, and car price determinants.
Interactive Web Application: A Streamlit-based app for real-time price predictions, tailored for ease of use by customers and sales teams.

![image](https://github.com/user-attachments/assets/b6f15af7-cb3c-4c02-bc74-e89275a5df27)

