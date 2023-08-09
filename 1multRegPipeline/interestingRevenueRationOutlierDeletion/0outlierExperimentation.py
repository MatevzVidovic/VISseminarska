import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np



# R is the ratio above which things are simply nonsensical outliers.
# R = 50

# But lets just use the N standard deviations from the mean for now.
N = 1
# This is crazy. Even with just N=1, there are only 5 outliers.
# Those outliers are so strong, they have changed the mean so much they are untouchable.

# Just hardcoding the ix of the revenueRatio
ix = 4




 
dfAllData = pd.read_csv('cleanedData.csv')

ixsToEliminate = set()

npArr = dfAllData.iloc[:, ix].to_numpy()
mean = np.mean(npArr)
std = np.std(npArr)
numsOfOutliers = 0




for ix2 in range(len(npArr)):
    if abs(npArr[ix2] - mean) > N * std:
    # if npArr[ix2] > R:
        ixsToEliminate.add(ix2)
        numsOfOutliers += 1



print("Num of outliers: " + str(numsOfOutliers))


print()
print("Indexes to be removed in total: " + str(len(ixsToEliminate)))




