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


#zergCSV, terranCSV = analyzeReplays()

url = "zerg_classified.csv"

# Read in the dataset
df = pd.read_csv(url)

y = df.iloc[1:, 2].values #build
X = df.iloc[1:, 0:6] 

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, shuffle=True)

reps_train = X_train.iloc[:, 0:2]
reps_test = X_test.iloc[:, 0:2]

X_train = X_train.iloc[:, 3:]
X_train = X_train.astype(int)
X_train = X_train.replace(-1,np.NaN)
X_train_median = X_train.median()
X_train = X_train.fillna(X_train_median)

X_test = X_test.iloc[:, 3:]
X_test = X_test.astype(int)
X_test = X_test.replace(-1,np.NaN)
X_test_median = X_test.median()
X_test = X_test.fillna(X_test_median)


y_pred = random_forest(X_train, y_train, X_test)
reps = df.iloc[1:, 0]
player = df.iloc[1:, 1]

print(accuracy_score(y_test, y_pred))

for i in range(0, len(y_test)):
    if y_test[i] != y_pred[i]:
        print(f"{reps_test.values[i][0]} ({reps_test.values[i][1]}) - predicted {y_pred[i]}, actual was {y_test[i]}")
