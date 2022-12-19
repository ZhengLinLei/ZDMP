# Model: RandomForest
# import the necessary packages
from sklearn.ensemble import RandomForestRegressor

# Initialize the model

def RandomForestModel(x, y):
    rf = RandomForestRegressor(max_depth=2, random_state=100)
    rf.fit(x, y)

    return rf