

import pandas as pd

import ast



df = pd.read_csv('credits.csv')

initGenderCol = [None]* df.shape[0]
df.insert(0, "dunno", initGenderCol, True)
df.insert(1, "female", initGenderCol, True)
df.insert(2, "male", initGenderCol, True)


for i in range (df.shape[0]):
    castString = df.loc[i, "cast"]
    temporaryList = ast.literal_eval(castString)
    
    genderList = [0, 0, 0]
    for count, ele in enumerate(temporaryList):
        ix = ele["gender"]
        genderList[ix] += 1

    df.loc[i, "dunno"] = genderList[0]
    df.loc[i, "female"] = genderList[1]
    df.loc[i, "male"] = genderList[2]



    

df.to_csv("genderParsed.csv", index=False)



