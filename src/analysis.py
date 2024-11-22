# src/analysis.py

import pandas as pd

def run_analysis():
    # Load the dataset
    data = pd.read_csv('data/sample.csv')

    # Perform simple analysis (e.g., calculate mean and sum of 'value' column)
    mean_value = data['value'].mean()
    sum_value = data['value'].sum()
    
    # Return the results as a dictionary
    return {
        'mean': mean_value,
        'sum': sum_value
    }

