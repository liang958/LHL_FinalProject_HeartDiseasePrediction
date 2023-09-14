# LHL Final Project: Heart Disease Prediction

## Project/Goals

Create a machine learning model that can predict a patient whether has heart disease or not based on a number of factors


## Process

1. Exploratory data analysis
   1) Explore data type, null values, missiong data, duplicated records etc.
   2) Distribution of features 
   3) Correlation between the predictor variables 

2. Data preprocessing and feature engineering
    1) Convert categorical features to numerically encoded integers 
    2) Standard scaler for normalization 
    3) Dimensionality reduction with PCA 

3. Training model
    Models include LogisticRegression, Kneighbors, Decision Tree, Random Forest, XGBoost Model
    Smote Over-samples algorithm for training set 

4. Hyperparameter Tuning and Evaluate Model performance
   RandomSearch Cross-Validation is used for hyperparameter Tuning 



## Results
XGBoost Model is the best model to predict heart disease, its accuracy is 92% and AUC score is 0.84

Age and Health condition may significantly impact on the risk of heart disease



## Future Goals
Apply a more complex model

Grid Seach Cross Validation for hyperparameter tuning

Deploy the prediction model in AWS