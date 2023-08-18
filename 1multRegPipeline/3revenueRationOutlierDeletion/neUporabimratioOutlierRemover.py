import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np



# R is the ratio above which things are simply nonsensical outliers.
R = 300
# 300 for now, because I will be following the rule of roughly 0.3 percent being out, because they are 3 sderr of normal distr out
# Although, this database is quite unique in that way, so this is bad.
# But for now, okay.

# 50000 gives 5
# 5000 gives 8
# 1500 gives 10
# 1000 gives 11
# 500 gives 13
# 400 gives 17
# 300 gives 19
# 200 gives 23
# 100 gives 43
# 50 gives 83
# 25 gives 153
# 15 gives 266
# 10 gives 432
# 5 gives 1056

#Not used now:

# But lets just use the N standard deviations from the mean for now.
# N = 1
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
    # if abs(npArr[ix2] - mean) > N * std:
    if npArr[ix2] > R:
        ixsToEliminate.add(ix2)
        numsOfOutliers += 1



print("Num of outliers: " + str(numsOfOutliers))


print()
print("Indexes to be removed in total: " + str(len(ixsToEliminate)))
    







print()
print(dfAllData.shape)

for val in ixsToEliminate:
    dfAllData.drop([val], inplace=True)
dfAllData.reset_index(drop=True, inplace=True)

print()
print(dfAllData.shape)

dfAllData.to_csv("preparedData.csv", index=False)


