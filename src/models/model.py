"""
This module contains the model training and evaluation functionality.
It provides a simple interface for training, evaluating, and making predictions.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

class SimpleMLModel:
    """
    A simple ML model wrapper class that demonstrates basic ML workflow.
    """
    
    def __init__(self):
        """Initialize the model"""
        self.model = LogisticRegression()
        
    def train(self, X_train, y_train):
        """
        Train the model on the given data.
        
        Args:
            X_train (array-like): Training features
            y_train (array-like): Training labels
        """
        self.model.fit(X_train, y_train)
        
    def predict(self, X):
        """
        Make predictions on new data.
        
        Args:
            X (array-like): Features to predict
            
        Returns:
            array-like: Predictions
        """
        return self.model.predict(X)
    
    def evaluate(self, X_test, y_test):
        """
        Evaluate the model performance.
        
        Args:
            X_test (array-like): Test features
            y_test (array-like): True labels
            
        Returns:
            dict: Dictionary containing evaluation metrics
        """
        predictions = self.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        report = classification_report(y_test, predictions)
        
        return {
            'accuracy': accuracy,
            'classification_report': report
        }
    
    def save_model(self, filepath):
        """
        Save the trained model to disk.
        
        Args:
            filepath (str): Path where to save the model
        """
        joblib.dump(self.model, filepath)
    
    @classmethod
    def load_model(cls, filepath):
        """
        Load a trained model from disk.
        
        Args:
            filepath (str): Path to the saved model
            
        Returns:
            SimpleMLModel: Loaded model instance
        """
        instance = cls()
        instance.model = joblib.load(filepath)
        return instance