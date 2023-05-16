import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

 
dfAllData = pd.read_csv('BechdelDataPrepared.csv')


castFemPercent = dfAllData.loc[:, "castFemalePercentage"].tolist()




listOfArrays = []

columnNames = dfAllData.columns
for ix in range(dfAllData.shape[1]):
    currColumn = dfAllData.iloc[:, ix].tolist()
    listOfArrays.append(np.array(currColumn))

print(listOfArrays)