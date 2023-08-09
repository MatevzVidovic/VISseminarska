import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np




ix = 10




 
dfAllData = pd.read_csv('preparedData.csv')

ixsToEliminate = set()

npArr = dfAllData.iloc[:, ix].to_numpy()
numsOfOutliers = 0




for ix2 in range(len(npArr)):
    # if abs(npArr[ix2] - mean) > N * std:
    if npArr[ix2] != "en":
    # if npArr[ix2] > max:
        ixsToEliminate.add(ix2)
        numsOfOutliers += 1





print()
print("Indexes to be removed in total: " + str(len(ixsToEliminate)))
    







print()
print(dfAllData.shape)

for val in ixsToEliminate:
    dfAllData.drop([val], inplace=True)
dfAllData.reset_index(drop=True, inplace=True)

print()
print(dfAllData.shape)

dfAllData.to_csv("langPreparedData.csv", index=False)



