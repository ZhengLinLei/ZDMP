#       
#   Apache License 2.0
#   Repository: https://github.com/ZhengLinLei/ZDMP
#
#   This file is used to train and evaluate the model, and compare the results, to find the best model
#   The best model is saved in ./build/trained_model.pkl
#   The best model is used in the future in ./predict.py to predict the reliability of the batch in the future
#   The realtime data will push data to the database, and the ./predict.py will predict it
#

# ------------------------- #

# Import ./libs/loadData.py
# Import ./libs/preparateData.py
import json, os, pandas, time
from libs.loadData import load_data
from libs.preparateData import prepare_data, split_data
from libs.evaluateData import eval_data

# Import models in ./models folder
from models.LinearRegression import LinearRegressionModel
from models.RandomForest import RandomForestModel
from models.KNNeighbors import KNNModel
from models.SVM import SVMModel

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

# Train the model
# |
# |-> LinearRegression
# |-> RandomForest
# |-> KNNeighbors
# |-> SVM

# LinearRegression
lr = LinearRegressionModel(X_train, Y_train)
Y_lr_train_pred = lr.predict(X_train)                       # Predict the training data
Y_lr_test_pred = lr.predict(X_test)                         # Predict the test data

# RandomForest
rf = RandomForestModel(X_train, Y_train)
Y_rf_train_pred = rf.predict(X_train)                       # Predict the training data
Y_rf_test_pred = rf.predict(X_test)                         # Predict the test data

# KNNeighbors
kn = KNNModel(X_train, Y_train)
Y_kn_train_pred = kn.predict(X_train)                       # Predict the training data
Y_kn_test_pred = kn.predict(X_test)                         # Predict the test data

# SVM
svm = SVMModel(X_train, Y_train)
Y_svm_train_pred = svm.predict(X_train)                     # Predict the training data
Y_svm_test_pred = svm.predict(X_test)                       # Predict the test data

# Evaluate the model
# |
# |-> LinearRegression - 0
# |-> RandomForest     - 1
# |-> KNNeighbors      - 2
# |-> SVM              - 3


EVAL_MODEL = []
R2_EVAL = []
MSE_EVAL = []
#
# LinearRegression
mse_lr_train, r2_lr_train = eval_data(Y_train, Y_lr_train_pred)     # Evaluate the training data
mse_lr_test, r2_lr_test = eval_data(Y_test, Y_lr_test_pred)         # Evaluate the test data
R2_EVAL.append([r2_lr_train, r2_lr_test])
MSE_EVAL.append([mse_lr_train, mse_lr_test])

# RandomForest
mse_rf_train, r2_rf_train = eval_data(Y_train, Y_rf_train_pred)     # Evaluate the training data
mse_rf_test, r2_rf_test = eval_data(Y_test, Y_rf_test_pred)         # Evaluate the test data
R2_EVAL.append([r2_rf_train, r2_rf_test])
MSE_EVAL.append([mse_rf_train, mse_rf_test])

# KNNeighbors
mse_kn_train, r2_kn_train = eval_data(Y_train, Y_kn_train_pred)     # Evaluate the training data
mse_kn_test, r2_kn_test = eval_data(Y_test, Y_kn_test_pred)         # Evaluate the test data
R2_EVAL.append([r2_kn_train, r2_kn_test])
MSE_EVAL.append([mse_kn_train, mse_kn_test])

# SVM
mse_svm_train, r2_svm_train = eval_data(Y_train, Y_svm_train_pred)  # Evaluate the training data
mse_svm_test, r2_svm_test = eval_data(Y_test, Y_svm_test_pred)      # Evaluate the test data
R2_EVAL.append([r2_svm_train, r2_svm_test])
MSE_EVAL.append([mse_svm_train, mse_svm_test])


MODEL = [lr, rf, kn, svm]
MODEL_NAME = ['LinearRegression', 'RandomForest', 'KNNeighbors', 'SVM']

for i in range(len(MODEL)):
    r = pandas.DataFrame([MODEL_NAME[i], MSE_EVAL[i][0], R2_EVAL[i][0], MSE_EVAL[i][1], R2_EVAL[i][1]]).transpose()
    r.columns = ['Method', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2']
    EVAL_MODEL.append(r)

# Get the result  
df_models = pandas.concat(EVAL_MODEL, axis=0)


# Print the result
print(df_models.reset_index(drop=True))

# --------------------- Result ---------------------
# KNN Best coefficient: k = 1
#
#
#               Method Training MSE Training R2           Test MSE             Test R2
# 0  Linear regression     0.026466    0.651201  2603143596.200458 -34521933304.644592
# 1      Random forest     0.054894    0.276561           0.053715            0.287655
# 2        KNNeighbors     0.000056    0.999266           0.014994            0.801152
# 3                SVM     0.044920    0.408009           0.043429            0.424063

# In this case, the best model is the KNNeighbors
# MSE: 0.014994
# R2: 0.801152



# Print the execution time
# Device information: 
#   - CPU: Intel(R) Core(TM) i7-12700H CPU @ 2.70GHz
#   - RAM: 32GB
#   - OS: Windows 10
#   - Python: 3.10.7
#   - Model: MSI Ryder GS76
print("----- %s seconds -----" % (time.time() - start_time))

# ----- 764.8955461978912 secods -----
# 12,7 minutes