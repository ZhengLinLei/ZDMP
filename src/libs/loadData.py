# Module loadData.py

# Import libraries
import pandas as pd

# Load the .csv file from ../datasets/batch_data.csv for global path

def load_data():
    df = pd.read_csv('../datasets/batch_data.csv')
    return df