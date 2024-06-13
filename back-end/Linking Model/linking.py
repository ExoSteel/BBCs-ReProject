from sklearn import svm
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import root_mean_squared_error
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math



x_d = distributor_df.drop(['distributor_Name', 'distributor_Type'], axis = 1)
y_d = distributor_df['submission_Date']



kmeans = KMeans(
    n_clusters = 2, 
    init='k-means++',
    random_state=0
)
kmeans.fit(x_d)

from sklearn.metrics import f1_score

print("Non-inverted F1:", f1_score(y, kmeans.labels_))
print("Inverted F1:", f1_score(y, [0 if i == 1 else 1 for i in kmeans.labels_]))
