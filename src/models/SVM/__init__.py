# Model: SVM - Support Vector Machine
# import the necessary packages

from sklearn.svm import SVR

# initialize our SVM model
def SVMModel(x, y):
    svm = SVR()
    svm.fit(x, y)

    return svm