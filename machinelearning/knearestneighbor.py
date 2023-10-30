from sklearn.neighbors import KNeighborsClassifier

def knn(X, y, X_unknown):
    classifier = KNeighborsClassifier(n_neighbors=3, weights='distance')
    classifier.fit(X, y)

    y_pred = classifier.predict(X_unknown)
    return y_pred
