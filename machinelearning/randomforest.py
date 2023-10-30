# Data Processing
import pandas as pd
import numpy as np

# Modelling
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint

# Tree Visualisations
from sklearn.tree import export_graphviz
from IPython.display import Image

def random_forest(X_train, y_train, X_test):
    rf = RandomForestClassifier()

    rf.fit(X_train, y_train)

    y_pred = rf.predict(X_test)
    return y_pred
