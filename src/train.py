#       
#   Apache License 2.0
#   Repository: https://github.com/ZhengLinLei/ZDMP
#
#   This file is used to train and dump the model trained by ./train.py into ./build/model.pkl
#   The model is used in the future in ./predict.py to predict the reliability of the batch in the future
#   The realtime data will push data to the database, and the ./predict.py will predict it in every production line checking
#
#   ----- Model -----
#   KNN with k=1
#
#   Why? Because the dataset is not balanced, and the dataset is not big enough, so we use KNN with k=1 to predict the reliability of the batch
#   If the dataset is big enough, we can use other models, such as SVM, RandomForest, LinearRegression, etc.
#
#!               Method  Training MSE     Training R2             Test MSE                Test R2
#! 0  Linear regression      0.026466        0.651201    2603143596.200458    -34521933304.644592 ------> Worst model
#! 1      Random forest      0.054894        0.276561             0.053715               0.287655
#! 2        KNNeighbors      0.000056        0.999266             0.014994               0.801152 ------> Best model
#! 3                SVM      0.044920        0.408009             0.043429               0.424063
#
#   ----- Dataset -----
#   ./datasets/batch_data.csv
#
#   ----- Dataset Description -----
#   The dataset is collected from the production line

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
with open(os.path.join(CURRENT_PATH, CONFIG['build']['path'], CONFIG['build']['path']), 'wb') as f:
    pickle.dump(kn, f)


# Print execution time
print('Execution time: {} seconds'.format(time.time() - start_time))



# Device information: 
#   - CPU: Apple M2  
#   - RAM: 8GB
#   - OS: MacOs Ventura 13.1
#   - Python: 3.10.7
#   - Model: Apple MacBook Pro 2022


# Output:
# KNN Coefficient:  1
# Execution time: 15.409789085388184 seconds