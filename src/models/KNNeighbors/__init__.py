# Model: KNN - K Nearest Neighbors
# import the necessary packages

from sklearn.neighbors import KNeighborsRegressor

# initialize our KNN model
def KNNModel(x, y, c=0):

    # Find the best k
    k = 0
    best_score = 0

    KNN_ARR = []
    KNN = None;

    if c != 0: # If c is not 0, use the coefficient c otherwise find the best coefficient
        KNN_ARR.append(KNeighborsRegressor(n_neighbors=c))
        KNN_ARR[0].fit(x, y)

        print("KNN Coefficient: ", c)

        KNN = KNN_ARR[0]

    else:
        for i in range(0, 10):
            KNN_ARR.append(KNeighborsRegressor(n_neighbors=i+1))
            KNN_ARR[i].fit(x, y)
            score = KNN_ARR[i].score(x, y)
            if score > best_score:
                best_score = score
                k = i

        print("KNN Best coefficient: ", k)

        KNN = KNN_ARR[k]

    return KNN