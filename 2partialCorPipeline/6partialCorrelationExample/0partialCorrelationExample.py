import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import pingouin as pg



dfAllData = pd.read_csv('langPreparedData.csv')



# castFemalePercentage,crewFemalePercentage,budget,revenue,revenueRatio,
# vote_average,vote_count,runtime,releaseYear,releaseTimeOfYear,      original_language,popularity


# Z = dfAllData[['budget', 'runtime', 'releaseYear', 'releaseTimeOfYear']] 
# x1 = dfAllData['castFemalePercentage']
# x2 = dfAllData['crewFemalePercentage']
# y1 = dfAllData['revenue']
# y2 = dfAllData['vote_average']
# y3 = dfAllData['revenueRatio']


# dfRelevantData = dfAllData[['budget', 'runtime', 'releaseYear', 'releaseTimeOfYear', 'castFemalePercentage', 'crewFemalePercentage', 'revenue', 'revenueRatio', 'vote_average', 'vote_count']]

# print(str(dfRelevantData.pcorr().round(3)))
# print("------------------------------------------")
# print("\n\n\n")



Z = ['budget']

corrType = ["pearson"] # , "spearman"
x = ["castFemalePercentage", "crewFemalePercentage"]
y = ["revenue"] # , "vote_average", "revenueRatio", "vote_count"

for j in x:
    for k in y:
        for i in corrType:
            print("------------------------------------------")
            print(j + ", " + k + ", " + i + ":")
            print(str(pg.partial_corr(data=dfAllData, x=j, y=k, covar=Z, method=i).round(3)))
            print("------------------------------------------")
            print("\n\n")

            


z = ['budget']

corrType = ["pearson"] # , "spearman"
x = ["castFemalePercentage", "crewFemalePercentage"]
y = ["revenue"] # , "vote_average", "revenueRatio", "vote_count"

for j in x:
    for k in y:
        for i in z:
            X = np.array(dfAllData[j])
            Y = np.array(dfAllData[k])
            Z = np.array(dfAllData[i])
            
            r = np.corrcoef(X, Y)

            print("------------------------------------------")
            print(j + ", " + k + ":")
            print(str(r[0, 1].round(3)))
            print("------------------------------------------")
            print("\n\n")

            r = np.corrcoef(X, Z)

            print("------------------------------------------")
            print(j + ", " + i + ":")
            print(str(r[0, 1].round(3)))
            print("------------------------------------------")
            print("\n\n")

            r = np.corrcoef(Y, Z)

            print("------------------------------------------")
            print(k + ", " + i + ":")
            print(str(r[0, 1].round(3)))
            print("------------------------------------------")
            print("\n\n")




# # po defaultu je pearson
# print("revenue, Pearson:")
# print(str(pg.partial_corr(data=dfAllData, x='castFemalePercentage', y='revenue', covar=['budget', 'runtime', 'releaseYear', 'releaseTimeOfYear']).round(3)))
# print("\n\n\n")

# print("revenue, Spearman:")
# print(str(pg.partial_corr(data=dfAllData, x='castFemalePercentage', y='revenue', covar=['budget', 'runtime', 'releaseYear', 'releaseTimeOfYear'], method='spearman').round(3)))
# print("\n\n\n")

# print("vote_average, Pearson:")
# print(str(pg.partial_corr(data=dfAllData, x='castFemalePercentage', y='vote_average', covar=['budget', 'runtime', 'releaseYear', 'releaseTimeOfYear']).round(3)))
# print("\n\n\n")

# print("vote_average, Spearman:")
# print(str(pg.partial_corr(data=dfAllData, x='castFemalePercentage', y='vote_average', covar=['budget', 'runtime', 'releaseYear', 'releaseTimeOfYear'], method='spearman').round(3)))
# print("\n\n\n")