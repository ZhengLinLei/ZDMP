# Model: KNN - K Nearest Neighbors
# import the necessary packages

from sklearn.neighbors import KNeighborsRegressor

# initialize our KNN model
def KNNModel(x, y):

    # Find the best k
    k = 0
    best_score = 0

    KNN_ARR = []
    for i in range(0, 10):
        KNN_ARR.append(KNeighborsRegressor(n_neighbors=i))
        KNN_ARR[i].fit(x, y)
        score = KNN_ARR[i].score(x, y)
        if score > best_score:
            best_score = score
            k = i

    print(k)

    return KNN_ARR[k]