import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from kmeans import kmeans
from knearestneighbor import knn
from randomforest import random_forest
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn import neighbors, datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

df = pd.read_csv("terran_unclassified.csv")
y = df.iloc[1:, 2].values #build
X = df.iloc[1:, 0:] #values

reps = X.iloc[:, 0:2]
X = X.iloc[:, 3:]

X = X.astype(int)
X = X.replace(-1,np.NaN)
X_median = X.median()
X = X.fillna(X_median)
X = X.dropna(axis='columns', how='all')
labels = kmeans(X)

labels = [f"{rep[0]} - {rep[1]}" for rep in reps.values]
fig = ff.create_dendrogram(X, orientation='left', labels=labels)
fig.update_layout(width=1920, height=2000)
fig.show()

for i in range(0, len(labels)):
    print(f"{reps.values[i][0]} ({reps.values[i][1]})")