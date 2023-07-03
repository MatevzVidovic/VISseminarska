import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np



# If under min, it's an outlier.
min = 1000



# This really doesn't present any problems.
# max = 1e9



#Not used now:

# But lets just use the N standard deviations from the mean for now.
# N = 6




# Just hardcoding the ix of revenue
ix = 3




 
dfAllData = pd.read_csv('cleanedData.csv')

ixsToEliminate = set()

npArr = dfAllData.iloc[:, ix].to_numpy()
mean = np.mean(npArr)
std = np.std(npArr)
numsOfOutliers = 0




for ix2 in range(len(npArr)):
    # if abs(npArr[ix2] - mean) > N * std:
    if npArr[ix2] < min:
    # if npArr[ix2] > max:
        ixsToEliminate.add(ix2)
        numsOfOutliers += 1





for val in ixsToEliminate:
    print(str(dfAllData.loc[val, 'title']))
    print(str(dfAllData.loc[val, 'original_title']))
    print(val)
    print(str(dfAllData.loc[val, 'budget']))
    print(str(dfAllData.loc[val, 'revenue']))
    print(str(dfAllData.loc[val, 'revenueRatio']))
    print()





print("Num of outliers: " + str(numsOfOutliers))


print()
print("Indexes to be removed in total: " + str(len(ixsToEliminate)))







