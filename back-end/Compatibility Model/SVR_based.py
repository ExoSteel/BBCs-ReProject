from sklearn import svm
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import root_mean_squared_error
from sklearn.manifold import TSNE
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint
import math

def dist_diff(f_long,f_lat,l_long,l_lat): # Calculates distance via Geo-Coordinates
    f_lat = math.radians(float(f_lat))
    f_long = math.radians(float(f_long))
    l_lat = math.radians(float(l_lat))
    l_long = math.radians(float(l_long))

    # Haversine formula
    dlat = l_lat - f_lat
    dlon = l_long - f_long
    a = math.sin(dlat / 2)**2 + math.cos(f_lat) * math.cos(l_lat) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Radius of Earth in kilometers. Use 3956 for miles. Determines return value units.
    R = 6371.0
    
    # Calculate the result
    distance = R * c
    
    return distance

diag = pd.read_csv("back-end/Compatibility Model/diagonal.csv")
distri = pd.read_csv("back-end/datasets/distributors.csv")
recip = pd.read_csv("back-end/datasets/recipients.csv")

disrec = pd.concat([distri, recip], axis=1, join="inner")

# Date Difference
sDate_df = disrec["submission_Date"]
rDate_df = disrec["requirement_Date"]

arrayDate = []
for i in range(500):
    sDate = sDate_df[i]
    rDate = rDate_df[i]
    dayDiff = (int(rDate[8:10]) + (int(rDate[6]) * 31)) - (int(sDate[8:10]) + (int(sDate[6])*31))
    if dayDiff <= 0:
        dayDiff = 1
    arrayDate.append(dayDiff)


disrec["date_Difference"] = arrayDate

# print(disrec["date_Difference"])
# Distance Difference
distance = []
for i in range(500):
    distance.append(dist_diff(distri.iloc[i, 3], distri.iloc[i, 4], recip.iloc[i, 3], recip.iloc[i, 4]))

disrec["dist_Difference"] = distance

# print(disrec)

# Dietary Requirements
encoder = OneHotEncoder(categories=[["Y","N"]])
disrec[["nut_Y","nut_N"]] = encoder.fit_transform(disrec[["nut_A"]]).toarray()
disrec = disrec.drop(["nut_A"], axis=1)

disrec[["egg_Y","egg_N"]] = encoder.fit_transform(disrec[["egg_A"]]).toarray()
disrec = disrec.drop(["egg_A"], axis=1)

disrec[["soy_Y","soy_N"]] = encoder.fit_transform(disrec[["soy_A"]]).toarray()
disrec = disrec.drop(["soy_A"], axis=1)



# X = disrec.drop(["recipient_Name, recipient_Type, requirement_Date, distributor_Name, distributor_Type, submission_Date"])
# y = diag["0"]

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