from sklearn.preprocessing import OneHotEncoder, StandardScaler, Normalizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.manifold import TSNE
from sklearn.metrics import mean_squared_error

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

distributor_df = pd.read_csv("datasets\distributors.csv")

from sklearn.preprocessing import OrdinalEncoder
encoder = OrdinalEncoder(categories = [["Restaurant/Food outlet", "Supermarket"]])
distributor_df[["distributor_Type"]] = encoder.fit_transform(distributor_df[["distributor_Type"]])

recipient_df = pd.read_csv("datasets/recipients.csv")

rec_catgry = [["Old Folks Home", "Food shelter", "Homeless shelter", "Animal shelter"]]

encoder = OrdinalEncoder(categories = rec_catgry)
recipient_df[["recipient_Type"]] = encoder.fit_transform(recipient_df[["recipient_Type"]])
