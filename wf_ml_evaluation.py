# wf_ml_evaluation.py
import pandas as pd
from sklearn.model_selection import train_test_split
from wf_ml_training import train_and_save_models
from wf_ml_prediction import make_predictions
import os
import pickle

# Load processed data
data_path = 'data_processed/out.csv'
data = pd.read_csv(data_path)

selected_features = [
    'YrSold', 'MoSold', 'mortgage_interest', 'inflation_rates',
    'OverallQual', 'OverallCond', 'GrLivArea', 'TotalBsmtSF',
    'GarageCars', 'GarageArea', 'Neighborhood', 'YearBuilt',
    'YearRemodAdd', 'SalePrice','Street','PoolArea','PoolQC','LotArea','Heating','CentralAir'
]
data = pd.get_dummies(data[selected_features])

X = data.drop('SalePrice', axis=1)
y = data['SalePrice']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save the split datasets back to the data_processed folder
X_train.to_csv('data_processed/X_train.csv', index=False)
y_train.to_csv('data_processed/y_train.csv', index=False)
X_test.to_csv('data_processed/X_test.csv', index=False)
y_test.to_csv('data_processed/y_test.csv', index=False)

# Train the models and save them
model_save_dir = 'models'  # Directory to save the trained models
train_and_save_models(X_train, y_train, model_save_dir)

# Evaluate each model
results = make_predictions()

# Create a DataFrame from results
summary_df = pd.DataFrame(results, columns=["Dataset", "Method", "Mean Squared Error", "R-squared"])

# Save the summary DataFrame to a file
evaluation_path = 'evaluation/summary.txt'
os.makedirs(os.path.dirname(evaluation_path), exist_ok=True)
with open(evaluation_path, 'w') as file:
    df_as_string = summary_df.to_string(header=True, index=False)
    file.write(df_as_string)
