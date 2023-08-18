import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import pingouin as pg

import seaborn as sns



dfAllData = pd.read_csv('langPreparedData.csv')



# castFemalePercentage,crewFemalePercentage,budget,revenue,revenueRatio,
# vote_average,vote_count,runtime,releaseYear,releaseTimeOfYear,      original_language,popularity



dfRelevantData = dfAllData[['budget', 'runtime', 'releaseYear', 'releaseTimeOfYear', 'castFemalePercentage', 'crewFemalePercentage', 'directorGender', 'revenue', 'revenueRatio', 'vote_average', 'vote_count']]


sns.heatmap(dfRelevantData.corr(), cmap='coolwarm', annot=True)
plt.show()




# df = (dfRelevantData.pcorr().round(3))

# df.to_csv("results.csv", index=False)
# print("------------------------------------------")
# print("\n\n\n")


            