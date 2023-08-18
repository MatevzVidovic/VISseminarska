import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import math

 
dfAllData = pd.read_csv('dataExtracted.csv')




castFemPercent = dfAllData.loc[:, "castFemalePercentage"].tolist()

columnNames = dfAllData.columns
for ix in range(dfAllData.shape[1] - 2):
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
        print("Regression unable: " + columnNames[ix])

    # mng = plt.get_current_fig_manager()
    # mng.resize(*mng.window.maxsize())
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    
    # plt.show(block=False)

input("Blocking until you press enter.")






print("directorGender invalid:")
invalid_num = 0
directorGender = dfAllData.loc[:, "directorGender"].tolist()
for ix, val in enumerate(directorGender):
    if val >= 2:
        invalid_num += 1
print(invalid_num)



print("castFemalePercentage invalid:")
invalid_num = 0
castFemalePercentage = dfAllData.loc[:, "castFemalePercentage"].tolist()
for ix, val in enumerate(castFemalePercentage):
    if val < 0:
        invalid_num += 1
print(invalid_num)



print("crewFemalePercentage invalid:")
invalid_num = 0
crewFemalePercentage = dfAllData.loc[:, "crewFemalePercentage"].tolist()
for ix, val in enumerate(crewFemalePercentage):
    if val < 0:
        invalid_num += 1
print(invalid_num)




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









print("revenueRatio invalid:")
invalid_num = 0
revenueRatio = dfAllData.loc[:, "revenueRatio"].tolist()
for ix, val in enumerate(revenueRatio):
    if val <= 0:
        invalid_num += 1
print(invalid_num)






print("revenue invalid:")
invalid_num = 0
revenue = dfAllData.loc[:, "revenue"].tolist()
for ix, val in enumerate(revenue):
    if val <= 0:
        invalid_num += 1
print(invalid_num)









print("budget invalid:")
invalid_num = 0
budget = dfAllData.loc[:, "budget"].tolist()
for ix, val in enumerate(budget):
    if val <= 0:
        invalid_num += 1
print(invalid_num)



print("language invalid:")
invalid_num = 0
originalLanguage = dfAllData.loc[:, "original_language"].tolist()
for ix, val in enumerate(originalLanguage):
    if val == "NoneString":
        invalid_num += 1
print(invalid_num)






print("\n\n\nWashing mashine goes brrrrr.\n\n\n")


print(dfAllData.shape)



castFemalePercentage = dfAllData.loc[:, "castFemalePercentage"].tolist()
for ix, val in enumerate(castFemalePercentage):
    if val < 0:
        dfAllData.drop([ix], inplace=True)

dfAllData.reset_index(drop=True, inplace=True)

print(dfAllData.shape)



crewFemalePercentage = dfAllData.loc[:, "crewFemalePercentage"].tolist()
for ix, val in enumerate(crewFemalePercentage):
    if val < 0:
        dfAllData.drop([ix], inplace=True)

dfAllData.reset_index(drop=True, inplace=True)


print(dfAllData.shape)





currentCleaningList = dfAllData.loc[:, "original_language"].tolist()
for ix, val in reversed(list(enumerate(currentCleaningList))):
    if val == "NoneString":
        dfAllData.drop([ix], inplace=True)

dfAllData.reset_index(drop=True, inplace=True)

print(dfAllData.shape)



currentCleaningList = dfAllData.loc[:, "runtime"].tolist()
for ix, val in reversed(list(enumerate(currentCleaningList))):
    if val <= 0:
        dfAllData.drop([ix], inplace=True)

dfAllData.reset_index(drop=True, inplace=True)

print(dfAllData.shape)



currentCleaningList = dfAllData.loc[:, "vote_count"].tolist()
for ix, val in reversed(list(enumerate(currentCleaningList))):
    if val <= 0:
        dfAllData.drop([ix], inplace=True)

dfAllData.reset_index(drop=True, inplace=True)

print(dfAllData.shape)



currentCleaningList = dfAllData.loc[:, "vote_average"].tolist()
for ix, val in reversed(list(enumerate(currentCleaningList))):
    if val <= 0:
        dfAllData.drop([ix], inplace=True)

dfAllData.reset_index(drop=True, inplace=True)

print(dfAllData.shape)




print("nan values in all non-word places:")
invalid_num = 0
for col in range(dfAllData.shape[1] - 2):
    
    if (col == dfAllData.shape[1] - 4):
        continue

    for row in range(dfAllData.shape[0]):
        if math.isnan(dfAllData.iloc[row,col]):
            invalid_num += 1
print(dfAllData.shape)


print("\n\n\nAfter cleaning stats:\n\n\n")



dfAllData.to_csv("cleanedData.csv", index=False)













print("castFemalePercentage invalid:")
invalid_num = 0
castFemalePercentage = dfAllData.loc[:, "castFemalePercentage"].tolist()
for ix, val in enumerate(castFemalePercentage):
    if val < 0:
        invalid_num += 1
print(invalid_num)



print("crewFemalePercentage invalid:")
invalid_num = 0
crewFemalePercentage = dfAllData.loc[:, "crewFemalePercentage"].tolist()
for ix, val in enumerate(crewFemalePercentage):
    if val < 0:
        invalid_num += 1
print(invalid_num)




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




print()
print()
print()
print()
print()
print()
print("Bound to be uncleaned:")







print("directorGender invalid:")
invalid_num = 0
directorGender = dfAllData.loc[:, "directorGender"].tolist()
for ix, val in enumerate(directorGender):
    if val >= 2:
        invalid_num += 1
print(invalid_num)



print("revenueRatio invalid:")
invalid_num = 0
revenueRatio = dfAllData.loc[:, "revenueRatio"].tolist()
for ix, val in enumerate(revenueRatio):
    if val <= 0:
        invalid_num += 1
print(invalid_num)






print("revenue invalid:")
invalid_num = 0
revenue = dfAllData.loc[:, "revenue"].tolist()
for ix, val in enumerate(revenue):
    if val <= 0:
        invalid_num += 1
print(invalid_num)









print("budget invalid:")
invalid_num = 0
budget = dfAllData.loc[:, "budget"].tolist()
for ix, val in enumerate(budget):
    if val <= 0:
        invalid_num += 1
print(invalid_num)



print("language invalid:")
invalid_num = 0
originalLanguage = dfAllData.loc[:, "original_language"].tolist()
for ix, val in enumerate(originalLanguage):
    if val == "NoneString":
        invalid_num += 1
print(invalid_num)




print("nan values in all non-word places:")
invalid_num = 0
for col in range(dfAllData.shape[1] - 2):
    
    if (col == dfAllData.shape[1] - 4):
        continue

    for row in range(dfAllData.shape[0]):
        if math.isnan(dfAllData.iloc[row,col]):
            invalid_num += 1
print(invalid_num)

