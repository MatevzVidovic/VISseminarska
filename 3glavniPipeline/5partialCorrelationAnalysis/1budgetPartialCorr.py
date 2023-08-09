import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import pingouin as pg



dfAllData = pd.read_csv('langPreparedData.csv')





Z = ['runtime', 'releaseYear', 'releaseTimeOfYear']

corrType = ["pearson"] # , "spearman"
x = ["castFemalePercentage", "crewFemalePercentage", "directorGender"]
y = ['budget'] # "revenue", "vote_average" , "revenueRatio", "vote_count"

for j in x:
    for k in y:
        for i in corrType:
            print(j + ", " + k + ", " + i + ":")
            print(str(pg.partial_corr(data=dfAllData, x=j, y=k, covar=Z, method=i).round(3)))
            print("------------------------------------------")
            print("\n\n\n")

            