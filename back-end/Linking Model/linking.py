from sklearn.neighbors import NearestNeighbors
import pandas as pd
import pprint

df = pd.read_csv("back-end/datasets/Compatibility Percentage Matrix fixed.csv")
recipients = df["Unnamed: 0"].iloc[1:]
df = df.drop(["Unnamed: 0", "Unnamed: 0.1", "Distributors"], axis=1)
distributors = df.columns
print(recipients, distributors)
df = df.iloc[1:]

# Initialize NearestNeighbors for distributors and recipients separately
nn_distri = NearestNeighbors(n_neighbors=2, metric='euclidean').fit(df)


# Find nearest distributor for each recipient
distri_i = nn_distri.kneighbors(df, return_distance=False)

for i in range(df.shape[0]):
    print(distributors[i], "links with", recipients.iloc[distri_i[i, 1]])
