import pandas as pd

matrix = pd.read_csv("back-end/Compatibility Model/Compatibility Percentage Matrix fixed.csv")
diagonal = []

print(matrix.head)
for i in range(0, 500):
    diagonal.append(matrix.iloc[i + 1, i + 3])


series = pd.Series(diagonal)

print(series)

series.to_csv("diagonal.csv", sep=",")