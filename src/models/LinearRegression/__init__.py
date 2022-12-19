# Model: LinearRegression
# import the necessary packages

from sklearn.linear_model import LinearRegression

# initialize our Linear Regression model
def LinearRegressionModel(x, y):
    lr = LinearRegression()
    lr.fit(x, y)

    return lr