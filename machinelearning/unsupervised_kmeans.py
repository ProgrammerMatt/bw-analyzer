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


df = pd.read_csv("terran_unclassified.csv")
y = df.iloc[1:, 2].values #build
X = df.iloc[1:, 0:] #values

reps = X.iloc[:, 0:2]
X = X.iloc[:, 3:]
labels = kmeans(X)

for i in range(0, len(labels)):
    print(f"{reps.values[i][0]} ({reps.values[i][1]}): {labels[i]}")

