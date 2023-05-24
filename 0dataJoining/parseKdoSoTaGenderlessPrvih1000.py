

import pandas as pd

import ast


# nrows=1 za omejitev stevila prebranih vrstic
df = pd.read_csv('credits.csv', nrows=1000)

# dataframe.insert(loc, column, value, allow_duplicates) 
initGenderCol = [None]* df.shape[0]
df.insert(0, "dunno", initGenderCol, True)
df.insert(1, "female", initGenderCol, True)
df.insert(2, "male", initGenderCol, True)

# print(df.shape)
# print(df.loc[[0, 10]])


for i in range (df.shape[0]):
    castString = df.loc[i, "cast"]
    temporaryList = ast.literal_eval(castString)
    #print(temporaryList)

    newList = []
    
    genderList = [0, 0, 0]
    for count, characterDict in enumerate(temporaryList):
        ix = characterDict["gender"]
        genderList[ix] += 1
        
        newDict = {}
        for key, value in characterDict.items():
            if key == "gender" or key == "character" or key == "name":
                newDict[key] = value
        
        if(newDict["gender"] == 0):
            newList.append(newDict)
        

    df.loc[i, "dunno"] = genderList[0]
    df.loc[i, "female"] = genderList[1]
    df.loc[i, "male"] = genderList[2]

    df.loc[i, "cast"] = str(newList)



    

df.to_csv("genderParsedPrvih1000.csv", index=False)



