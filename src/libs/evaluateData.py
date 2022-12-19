# Evaluate the predicted Y data with the real Y data

# Import libraries
from sklearn.metrics import mean_squared_error, r2_score

# ----------------------------------------
def eval_data(Y_real, Y_pred):
    # Calculate the mean squared error (MSE)
    mse = mean_squared_error(Y_real, Y_pred)
    # Calculate the coefficient of determination (R^2)
    r2 = r2_score(Y_real, Y_pred)

    # Return the result
    return mse, r2