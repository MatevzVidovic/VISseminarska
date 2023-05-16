import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import math

 
dfAllData = pd.read_csv('BechdelDataPrepared.csv')




castFemPercent = dfAllData.loc[:, "castFemalePercentage"].tolist()

columnNames = dfAllData.columns
for ix in range(dfAllData.shape[1]-7):
    currColumn = dfAllData.iloc[:, ix].tolist()
    fig, ax = plt.subplots()
    ax.scatter(castFemPercent, currColumn)

    plt.title(columnNames[ix])
    #plt.figure(columnNames[ix])

    try:
        k, c = np.polyfit(castFemPercent, currColumn, deg=1)
        xseq = np.linspace(0, 100, num=100)
        ax.plot(xseq, c + k * xseq, color="k", lw=2.5)
    except:
        print("Regression unable")

    # mng = plt.get_current_fig_manager()
    # mng.resize(*mng.window.maxsize())
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    
    #plt.show(block=False)

input("Blocking until you press enter.")




print("Runtime invalid:")
runtimeInvalidNum = 0
runtime = dfAllData.loc[:, "runtime"].tolist()
for ix, val in enumerate(runtime):
    if val <= 0:
        runtimeInvalidNum += 1
print(runtimeInvalidNum)





print("Vote count invalid:")
voteCountInvalidNum = 0
voteCount = dfAllData.loc[:, "vote_count"].tolist()
for ix, val in enumerate(voteCount):
    if val <= 0:
        voteCountInvalidNum += 1
print(voteCountInvalidNum)






print("vote_average invalid:")
invalid_num = 0
vote_average = dfAllData.loc[:, "vote_average"].tolist()
for ix, val in enumerate(vote_average):
    if val <= 0:
        invalid_num += 1
print(invalid_num)





print("bechdelRevenueRatio invalid:")
invalid_num = 0
bechdelRevenueRatio = dfAllData.loc[:, "bechdelRevenueRatio"].tolist()
for ix, val in enumerate(bechdelRevenueRatio):
    if val <= 0:
        invalid_num += 1
print(invalid_num)





print("revenue_y invalid:")
invalid_num = 0
revenue_y = dfAllData.loc[:, "revenue_y"].tolist()
for ix, val in enumerate(revenue_y):
    if val <= 0:
        invalid_num += 1
print(invalid_num)






print("budget_y invalid:")
invalid_num = 0
budget_y = dfAllData.loc[:, "budget_y"].tolist()
for ix, val in enumerate(budget_y):
    if val <= 0:
        invalid_num += 1
print(invalid_num)





print("movieDatasetRevenueRatio invalid:")
invalid_num = 0
movieDatasetRevenueRatio = dfAllData.loc[:, "movieDatasetRevenueRatio"].tolist()
for ix, val in enumerate(movieDatasetRevenueRatio):
    if val <= 0:
        invalid_num += 1
print(invalid_num)






print("revenue_x invalid:")
invalid_num = 0
revenue_x = dfAllData.loc[:, "revenue_x"].tolist()
for ix, val in enumerate(revenue_x):
    if val <= 0:
        invalid_num += 1
print(invalid_num)









print("budget_x invalid:")
invalid_num = 0
budget_x = dfAllData.loc[:, "budget_x"].tolist()
for ix, val in enumerate(budget_x):
    if val <= 0:
        invalid_num += 1
print(invalid_num)








print("nan values in all non-word places:")
invalid_num = 0
for col in range(dfAllData.shape[1]-1):
    for row in range(dfAllData.shape[0]):
        if math.isnan(dfAllData.iloc[row,col]):
            invalid_num += 1
print(invalid_num)



print("\n\n\nWashing mashine goes brrrrr.\n\n\n")

revenue_y = dfAllData.loc[:, "revenue_y"].tolist()
for ix, val in reversed(list(enumerate(revenue_y))):
    if math.isnan(val):
        dfAllData.drop([ix], inplace=True)

dfAllData.reset_index(drop=True, inplace=True)

#print(dfAllData.shape)

revenue_x = dfAllData.loc[:, "revenue_x"].tolist()
for ix, val in reversed(list(enumerate(revenue_x))):
    if val <= 0:
        dfAllData.drop([ix], inplace=True)

dfAllData.reset_index(drop=True, inplace=True)

#print(dfAllData.shape)


budget_x = dfAllData.loc[:, "budget_x"].tolist()
for ix, val in reversed(list(enumerate(budget_x))):
    if val <= 0:
        dfAllData.drop([ix], inplace=True)

dfAllData.reset_index(drop=True, inplace=True)






print("\n\n\nAfter cleaning stats:\n\n\n")




print("bechdelRevenueRatio invalid:")
invalid_num = 0
bechdelRevenueRatio = dfAllData.loc[:, "bechdelRevenueRatio"].tolist()
for ix, val in enumerate(bechdelRevenueRatio):
    if val <= 0:
        invalid_num += 1
        # print(dfAllData.loc[ix, "bechdelRevenueRatio"])
        # print(dfAllData.loc[ix, "revenue_y"])
        # print(dfAllData.loc[ix, "budget_y"])


print(invalid_num)







print("movieDatasetRevenueRatio invalid:")
invalid_num = 0
movieDatasetRevenueRatio = dfAllData.loc[:, "movieDatasetRevenueRatio"].tolist()
for ix, val in enumerate(movieDatasetRevenueRatio):
    if val <= 0:
        invalid_num += 1
print(invalid_num)




print("revenue_x invalid:")
invalid_num = 0
revenue_x = dfAllData.loc[:, "revenue_x"].tolist()
for ix, val in enumerate(revenue_x):
    if val <= 0:
        invalid_num += 1
print(invalid_num)







print("budget_x invalid:")
invalid_num = 0
budget_x = dfAllData.loc[:, "budget_x"].tolist()
for ix, val in enumerate(budget_x):
    if val <= 0:
        invalid_num += 1
print(invalid_num)



print("nan values in all non-word places:")
invalid_num = 0
for col in range(dfAllData.shape[1]-1):
    for row in range(dfAllData.shape[0]):
        if math.isnan(dfAllData.iloc[row,col]):
            invalid_num += 1
print(invalid_num)








dfAllData.to_csv("BechdelCleanedData.csv", index=False)
