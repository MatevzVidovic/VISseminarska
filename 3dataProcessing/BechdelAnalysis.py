import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

 
dfAllData = pd.read_csv('BechdelCleanedData.csv')


castFemPercent = dfAllData.loc[:, "castFemalePercentage"].tolist()




listOfArrays = []

columnNames = dfAllData.columns
for ix in range(dfAllData.shape[1]):
    currColumn = dfAllData.iloc[:, ix].tolist()
    listOfArrays.append(np.array(currColumn))

# print(listOfArrays)






listOfMeans = []
listOfStandardDeviations = []

for ix in range(len(listOfArrays)-1):
    listOfMeans.append(np.mean(listOfArrays[ix]))
    listOfStandardDeviations.append(np.std(listOfArrays[ix]))





listOfNormalizedArrays = []

for ix in range(len(listOfArrays)-1):
    arrayToAppend = (listOfArrays[ix] - listOfMeans[ix]) / listOfStandardDeviations[ix]
    listOfNormalizedArrays.append(arrayToAppend)

print(listOfNormalizedArrays)
