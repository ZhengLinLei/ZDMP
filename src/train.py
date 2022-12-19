# Import ./libs/loadData.py
# Import ./libs/preparateData.py
import json, os
from libs.loadData import load_data
from libs.preparateData import prepare_data, split_data

# Import models in ./models folder
import models.LinearRegression as LinearRegression
import models.RandomForest as RandomForest


# Load training configuration ./config.ini
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__)) # ./src
CONFIG = json.load(open(os.path.join(CURRENT_PATH, 'config.ini'))) # ./config.ini
DATASET_PATH = os.path.join(CURRENT_PATH, CONFIG['dataset']['path']) # ./datasets/batch_data.csv

# Load the data
df = load_data(DATASET_PATH)

# Prepare the data
Y, X  = prepare_data(df)

# Split the data
X_train, X_test, Y_train, Y_test = split_data(X, Y)

# Train the model
# |
# |-> LinearRegression
# |-> RandomForest
# |-> ...