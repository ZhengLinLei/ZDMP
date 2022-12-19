# Module loadData.py

# Import libraries
import pandas as pd
import numpy as np

# Load the .csv file from ../datasets/batch_data.csv for global path

def load_data(path='../datasets/batch_data.csv'):
    # Read the .csv file in global path
    df = pd.read_csv(path)
    # Remove all not Number item row
    df = df[np.isfinite(df).all(1)]

    return df