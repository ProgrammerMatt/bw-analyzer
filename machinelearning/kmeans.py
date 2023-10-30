from sklearn.cluster import KMeans
from sklearn import preprocessing



def kmeans(X_train, X_test):
    X_train_norm = preprocessing.normalize(X_train)
    X_test_norm = preprocessing.normalize(X_test)

    kmeans = KMeans(n_clusters = 7, random_state = 0, n_init='auto')
    kmeans.fit(X)



