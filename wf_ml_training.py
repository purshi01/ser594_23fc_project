# wf_ml_training.py
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.svm import SVR
from sklearn.model_selection import cross_val_score
import pickle
import os

# Dictionary of models to train
models = {
    'RandomForest': RandomForestRegressor(n_estimators=100, random_state=42),
    'GradientBoosting': GradientBoostingRegressor(n_estimators=100, random_state=42),
    'LinearRegression': LinearRegression(),
    'SVR': SVR(C=1.0, epsilon=0.2)
}

def train_and_save_models(X_train, Y_train, model_save_path):
    trained_models = {}
    for model_name, model in models.items():
        # Train the model
        model.fit(X_train, Y_train)
        
        # Cross-validation can be used to evaluate the model
        scores = cross_val_score(model, X_train, Y_train, cv=5)
        print(f"{model_name} Cross-Validation Scores: {scores}")
        print(f"{model_name} Average Score: {scores.mean()}")
        
        # Save the trained model
        model_path = os.path.join(model_save_path, f'{model_name}.pkl')
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        with open(model_path, 'wb') as file:
            pickle.dump(model, file)
