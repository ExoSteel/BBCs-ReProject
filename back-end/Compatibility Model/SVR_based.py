from sklearn import svm
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import root_mean_squared_error
from sklearn.manifold import TSNE
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint

compat = pd.read_csv("back-end/Compatibility Model/Compatibility Confusion Matrix fixed.csv")
distri = pd.read_csv("back-end/datasets/distributors.csv")
recip = pd.read_csv("back-end/datasets/recipients.csv")


# pprint(digits)


# X = 
# y = 

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# tsne = TSNE(n_components=2)

# # ss = StandardScaler()
# X_train = tsne.fit_transform(X_train)
# X_test = tsne.fit_transform(X_test)

# # plt.figure(figsize=[10,8])
# # plt.scatter(X_train[:,0], X_train[:,1], c=y_train, cmap="viridis")
# # plt.colorbar()
# # plt.show()

# param_grid = {
#     "C" : np.logspace(-2, 4, num=7),
#     "gamma" : np.logspace(-3, 2, num=6)
# }

# svr = svm.SVR()
# grid = GridSearchCV(svr, param_grid=param_grid, scoring="neg_mean_absolute_error")

# grid.fit(X_train, y_train)

# print(grid.best_params_)

# y_pred = grid.predict(X_test)

# rmse = root_mean_squared_error(y_test, y_pred)

# print(rmse)