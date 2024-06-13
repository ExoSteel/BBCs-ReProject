import random
import numpy as np
import pandas as pd

data = pd.read_csv("recipients.csv")
print(data.iloc[:,2])

for i in range(500):
    data.iloc[i, 2] = (f"2024-0{str(random.randint(5,7))}-{str(random.randint(1,31))}")
    data.iloc[i, 3] = round(random.uniform(103.833 - 1.0, 103.833 + 1.0), 3)
    data.iloc[i, 4] = round(random.uniform(1.283, 1.283 + 2.0), 3)
    data.iloc[i, 5] = random.randint(50, 125)
    

for i in range(6, 25):
    for j in range(500):
        data.iloc[j,i] = round(random.uniform(0.8, 5.0), 2)

for k in range(25, 31, 2):
    for i in range(500):
        boolean = bool(random.randint(0,1))
        if boolean:
            data.iloc[i, k] = "Y"
            data.iloc[i, k + 1] = random.randint(2, 20)
        else:
            data.iloc[i, k] = "N"
            data.iloc[i, k + 1] = 0
        


# print(data.head)

data.to_csv("recipients fixed.csv", sep=",")