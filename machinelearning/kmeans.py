from sklearn.cluster import KMeans
from sklearn import preprocessing



def kmeans(X):

    kmeans = KMeans(n_clusters = 7, random_state = 0, n_init='auto')
    kmeans.fit(X)

    return kmeans.labels_



