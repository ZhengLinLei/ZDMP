#       
#   Apache License 2.0
#   Repository: https://github.com/ZhengLinLei/ZDMP
#
#   This file is used to train and dump the model trained by ./train.py
#

# ------------------------- #

# Import modules
import json, os, pickle, time
from libs.loadData import load_data
from libs.preparateData import prepare_data, split_data

# We are goint to use KNN model with k=1 to predict the reliability of the batch in this case, for different datasets, you can use different models
# Execute ./train_eval.py to find the best model

# Import KNN model
from models.KNNeighbors import KNNModel

# Get execution time()
start_time = time.time()

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

# Train the model KNN with k=1
kn = KNNModel(X_train, Y_train, c=1)
Y_kn_train_pred = kn.predict(X_train)                       # Predict the training data
Y_kn_test_pred = kn.predict(X_test)                         # Predict the test data

# Dump the model
with open(os.path.join(CURRENT_PATH, CONFIG['build']['path']), 'wb') as f:
    pickle.dump(kn, f)


# Print execution time
print('Execution time: {} seconds'.format(time.time() - start_time))


# Output:
# KNN Coefficient:  1
# Execution time: 15.409789085388184 seconds