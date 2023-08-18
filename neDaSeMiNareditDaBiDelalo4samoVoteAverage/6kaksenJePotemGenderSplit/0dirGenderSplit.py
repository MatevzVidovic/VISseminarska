import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import math

 
dfAllData = pd.read_csv('langPreparedData.csv')





print("directorGender split:")
gender = [0, 0]
directorGender = dfAllData.loc[:, "directorGender"].tolist()
for ix, val in enumerate(directorGender):
    if val < 2:
        gender[val] += 1
print(gender)

