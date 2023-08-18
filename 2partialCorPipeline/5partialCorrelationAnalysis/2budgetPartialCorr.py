import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import pingouin as pg



dfAllData = pd.read_csv('langPreparedData.csv')



# castFemalePercentage,crewFemalePercentage,budget,revenue,revenueRatio,
# vote_average,vote_count,runtime,releaseYear,releaseTimeOfYear,      original_language,popularity

Z = dfAllData[['budget', 'runtime', 'releaseYear', 'releaseTimeOfYear']] 
x1 = dfAllData['castFemalePercentage']
x2 = dfAllData['crewFemalePercentage']
y1 = dfAllData['revenue']
y2 = dfAllData['vote_average']
y3 = dfAllData['revenueRatio']


dfRelevantData = dfAllData[['budget', 'runtime', 'releaseYear', 'releaseTimeOfYear', 'castFemalePercentage', 'crewFemalePercentage', 'revenue', 'revenueRatio', 'vote_average', 'vote_count']]


print(str(dfRelevantData.pcorr().round(3)))
print("------------------------------------------")
print("\n\n\n")



Z = ['runtime', 'releaseYear', 'releaseTimeOfYear']

corrType = ["pearson"] # , "spearman"
x = ["castFemalePercentage", "crewFemalePercentage"]
y = ['budget'] # "revenue", "vote_average" , "revenueRatio", "vote_count"

for j in x:
    for k in y:
        for i in corrType:
            print(j + ", " + k + ", " + i + ":")
            print(str(pg.partial_corr(data=dfAllData, x=j, y=k, covar=Z, method=i).round(3)))
            print("------------------------------------------")
            print("\n\n\n")

            