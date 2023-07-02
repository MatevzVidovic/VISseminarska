import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np






# For now, outliers will be defined simply as N standard deviations from the mean.
N = 6
# 6 seems to be a good number, because none of the lower listed get cut at all,
# because that would be nonsencical.
# cast, crew, vote_average, releaseYear, releaseTimeOfYear

# With N=5 you already get releaseYearOutliers.










 
dfAllData = pd.read_csv('cleanedData.csv')
columnNames = dfAllData.columns

ixsToEliminate = set()

npArrs = [None] * dfAllData.shape[1]
means = [None] * dfAllData.shape[1]
stds = [None] * dfAllData.shape[1]
numsOfOutliers = [None] * dfAllData.shape[1]


for ix in range(dfAllData.shape[1]):

    if(columnNames[ix] == "original_language"):
        continue

    npArrs[ix] = dfAllData.iloc[:, ix].to_numpy()
    means[ix] = np.mean(npArrs[ix], axis=0)
    stds[ix] = np.std(npArrs[ix], axis=0)
    numsOfOutliers[ix] = 0
    # print(ix)


for ix1 in range(len(npArrs)):
    
    if(columnNames[ix1] == "original_language"):
        continue

    currArray = npArrs[ix1]
    for ix2 in range(len(currArray)):
        if abs(currArray[ix2] - means[ix1]) > N * stds[ix1]:
            ixsToEliminate.add(ix2)
            numsOfOutliers[ix1] += 1



for ix in range(dfAllData.shape[1]):
    print(columnNames[ix] + " num of outliers: " + str(numsOfOutliers[ix]))


print()
print("Indexes to be removed in total: " + str(len(ixsToEliminate)))




