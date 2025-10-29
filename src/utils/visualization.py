"""
This module provides utility functions used across the project.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_feature_importance(feature_names, importance_scores):
    """
    Create a bar plot of feature importance scores.
    
    Args:
        feature_names (list): Names of the features
        importance_scores (array-like): Importance scores for each feature
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(x=importance_scores, y=feature_names)
    plt.title('Feature Importance')
    plt.xlabel('Importance Score')
    plt.ylabel('Feature')
    plt.tight_layout()
    plt.show()

def save_results(results, filepath):
    """
    Save evaluation results to a file.
    
    Args:
        results (dict): Dictionary containing evaluation metrics
        filepath (str): Path where to save the results
    """
    with open(filepath, 'w') as f:
        for metric, value in results.items():
            f.write(f'{metric}:\n{value}\n\n')