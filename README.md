Project Description: Car Dheko - Used Car Price Prediction
This project involves developing a machine learning model to predict the prices of used cars based on various features such as make, model, year, fuel type, transmission type, and other relevant attributes. The objective is to enhance customer experience and streamline the pricing process for Car Dheko by creating an accurate and user-friendly Streamlit-based web application that provides real-time price predictions for both customers and sales representatives.

Key Techniques Used:
Data Cleaning and Preprocessing: Imported and concatenated unstructured datasets from different cities into a structured format, handled missing values (dropped columns with more than 25% missing data, filled numerical with median, and categorical with mode), standardized data formats, and encoded categorical variables.

Outlier Removal: Used the IQR (Interquartile Range) method to remove outliers, ensuring a robust and unbiased model training process.

Feature Engineering and Selection: Conducted Exploratory Data Analysis (EDA) to visualize data patterns, calculate descriptive statistics, and select important features using correlation analysis and model-based feature importance.

Model Development: Implemented multiple regression models including Linear Regression, Decision Trees, Random Forests, and Gradient Boosting. Used train-test split and cross-validation to train and evaluate models for robustness.

Hyperparameter Tuning: Applied GridSearchCV to optimize model parameters, enhancing model accuracy and generalization to unseen data.

Model Evaluation: Evaluated models using metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared to identify the best-performing model.
![image](https://github.com/user-attachments/assets/d198da22-083d-414b-904a-5cb44802bceb)



Model Deployment: Deployed the final model using Streamlit to create an interactive web application, allowing users to input car features and get instant price predictions. The app is designed to be user-friendly and includes error handling for better user experience.

This comprehensive approach ensures an accurate, efficient, and scalable solution for predicting used car prices, integrating data science techniques and machine learning best practices to deliver a valuable tool for Car Dheko's customers and sales teams.
