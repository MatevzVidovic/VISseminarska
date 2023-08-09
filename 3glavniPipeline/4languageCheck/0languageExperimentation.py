import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np




ix = 11




 
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





for val in ixsToEliminate:
    print(str(dfAllData.loc[val, 'title']))
    print(str(dfAllData.loc[val, 'original_title']))
    print(npArr[val])
    print(val)
    print()





print("Num of outliers: " + str(numsOfOutliers))


print()
print("Indexes to be removed in total: " + str(len(ixsToEliminate)))







