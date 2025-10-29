"""
This module handles all data loading and preprocessing operations.
It provides functions to load raw data, clean it, and prepare it for model training.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(filepath):
    """
    Load data from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pandas.DataFrame: Loaded data
    """
    return pd.read_csv(filepath)

def preprocess_data(df):
    """
    Clean and preprocess the data.
    
    Args:
        df (pandas.DataFrame): Raw data
        
    Returns:
        pandas.DataFrame: Cleaned and preprocessed data
    """
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    df = df.dropna()
    
    return df

def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split data into training and testing sets.
    
    Args:
        X (array-like): Features
        y (array-like): Target variable
        test_size (float): Proportion of data to use for testing
        random_state (int): Random seed for reproducibility
        
    Returns:
        tuple: (X_train, X_test, y_train, y_test)
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def scale_features(X_train, X_test):
    """
    Scale features using StandardScaler.
    
    Args:
        X_train (array-like): Training features
        X_test (array-like): Testing features
        
    Returns:
        tuple: (scaled_X_train, scaled_X_test, scaler)
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, scaler