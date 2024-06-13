import random
import numpy as np
import pandas as pd
import math

distributor = pd.read_csv("back-end/datasets/distributors.csv")
recipient = pd.read_csv("back-end/datasets/recipients.csv")
compat = pd.read_csv("./Compatibility Percentage Matrix.csv")

print(distributor.iloc[0, 3])

def dist_diff(f_long,f_lat,l_long,l_lat):
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

def calc_compat_food(item_d, expir, item_r, qty):
    result = math.log10(item_d * expir) / (item_r * qty)
    return result

for i in range(500):
    for j in range(500):
        distance = dist_diff(distributor.iloc[i, 3], distributor.iloc[i, 4], recipient.iloc[j, 3], recipient.iloc[j, 4])
        pork = calc_compat_food(distributor.iloc[i, 5], distributor.iloc[i, 6], recipient.iloc[j, 6], recipient.iloc[j, 7])
        beef = calc_compat_food(distributor.iloc[i, 7], distributor.iloc[i, 8], recipient.iloc[j, 7], recipient.iloc[j, 7])
        mutton = calc_compat_food(distributor.iloc[i, 9], distributor.iloc[i, 10], recipient.iloc[j, 8], recipient.iloc[j, 7])
        dist_p = (1 - 0.002 * distance)
        if dist_p < 0:
            dist_p = 0.0001
        compat.iloc[j + 1, i + 2] = dist_p * pork * beef * mutton


compat.to_csv("Compatibility Confusion Matrix fixed.csv", sep=",")