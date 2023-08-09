import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np



# These have been the chosen numbers, because as soon as these are 4 digits, they are probably correct information.
# Knowing from manually looking through them.
# Most wrong info is either simply a 1, o the movies runtime, but most often it's budget in millions instead of just dollars.

# There is this movie Tarnation.
# It breaks this rule.
# But otherwise it seems to be good.

minBudget = 1000
minRevenue = 1000


ixBudget = 2
ixRevenue = 3




 
dfAllData = pd.read_csv('cleanedData.csv')

ixsToEliminate = set()

npBudgetArr = dfAllData.iloc[:, ixBudget].to_numpy()
npRevenueArr = dfAllData.iloc[:, ixRevenue].to_numpy()




for ix2 in range(len(npBudgetArr)):
    # if abs(npArr[ix2] - mean) > N * std:
    if npBudgetArr[ix2] < minBudget:
        ixsToEliminate.add(ix2)


for ix2 in range(len(npBudgetArr)):
    # if abs(npArr[ix2] - mean) > N * std:
    if npRevenueArr[ix2] < minRevenue:
        ixsToEliminate.add(ix2)


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



