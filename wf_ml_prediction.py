# wf_ml_prediction.py
import pandas as pd
import pickle
import os
from sklearn.metrics import mean_squared_error, r2_score

def load_model(model_path):
    """Load a trained model from a file."""
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def make_predictions():
    X_test_path = 'data_processed/X_test.csv'
    Y_test_path = 'data_processed/y_test.csv'
    X_test = pd.read_csv(X_test_path)
    Y_test = pd.read_csv(Y_test_path)

    # Prepare DataFrame for storing results
    results = []
    model_save_dir = 'models' 

    # Load and evaluate each model
    for model_file in os.listdir(model_save_dir):
        if model_file.endswith('.pkl'):
            model_path = os.path.join(model_save_dir, model_file)
            model = load_model(model_path)
            model_name = os.path.splitext(model_file)[0]

            # Make predictions using the model
            predictions = model.predict(X_test)
            mse = mean_squared_error(Y_test, predictions)
            r2 = r2_score(Y_test, predictions)
            
            # Append results
            results.append([X_test_path, model_name, mse, r2])
    
    return results

