# Prepare the input data

# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split


# Prepare the input data
def prepare_data(df):
    # Return Y and X
    return df['reliability'], df.drop('reliability', axis=1)


# Split input data into training and testing sets
def split_data(X, Y, test_size=0.2):
    # Split the data
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=42)

    # Return the data
    return X_train, X_test, Y_train, Y_test