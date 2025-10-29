"""
Main script for training the model.
"""

import os
from data.data_processing import load_data, preprocess_data, split_data, scale_features
from models.model import SimpleMLModel
from utils.visualization import save_results

def main():
    # Load and preprocess data
    data = load_data('data/raw/your_dataset.csv')  # Replace with your dataset
    processed_data = preprocess_data(data)
    
    # Separate features and target
    X = processed_data.drop('target', axis=1)  # Replace 'target' with your target column
    y = processed_data['target']
    
    # Split and scale data
    X_train, X_test, y_train, y_test = split_data(X, y)
    X_train_scaled, X_test_scaled, _ = scale_features(X_train, X_test)
    
    # Train model
    model = SimpleMLModel()
    model.train(X_train_scaled, y_train)
    
    # Evaluate model
    results = model.evaluate(X_test_scaled, y_test)
    
    # Save results
    os.makedirs('results', exist_ok=True)
    save_results(results, 'results/evaluation_results.txt')
    
    # Save model
    os.makedirs('models', exist_ok=True)
    model.save_model('models/trained_model.joblib')
    
    print("Training completed! Results saved in 'results' directory.")

if __name__ == '__main__':
    main()