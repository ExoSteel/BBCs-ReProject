import pandas as pd
import sklearn

distributor_df = pd.read_csv("distributor.csv")
recipient_df = pd.read_csv("recipients.csv")

from sklearn.preprocessing import normalize
from sklearn.model_selection import train_test_split

x_d = distributor_df.drop(['distributor_Name', 'distributor_Type'], axis = 1)
y_d = distributor_df['submission_Date']

from sklearn.cluster import KMeans

kmeans = KMeans(
    n_clusters = 2, 
    init='k-means++',
    random_state=0
)
kmeans.fit(x_d)

from sklearn.metrics import f1_score

print("Non-inverted F1:", f1_score(y, kmeans.labels_))
print("Inverted F1:", f1_score(y, [0 if i == 1 else 1 for i in kmeans.labels_]))
