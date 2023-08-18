

import pandas as pd

import ast


# nrows=1 za omejitev stevila prebranih vrstic
df = pd.read_csv('credits.csv')

# dataframe.insert(loc, column, value, allow_duplicates) 
initGenderCol = [None]* df.shape[0]
df.insert(0, "noDataCast", initGenderCol, True)
df.insert(1, "femaleCast", initGenderCol, True)
df.insert(2, "maleCast", initGenderCol, True)

df.insert(3, "noDataCrew", initGenderCol, True)
df.insert(4, "femaleCrew", initGenderCol, True)
df.insert(5, "maleCrew", initGenderCol, True)

# print(df.shape)
# print(df.loc[[0, 10]])


for i in range (df.shape[0]):
    castString = df.loc[i, "cast"]
    castListOfDicts = ast.literal_eval(castString)
    #print(temporaryList)

    castGenderList = [0, 0, 0]
    for characterDict in castListOfDicts:
        ix = characterDict["gender"]
        castGenderList[ix] += 1
    
    df.loc[i, "noDataCast"] = castGenderList[0]
    df.loc[i, "femaleCast"] = castGenderList[1]
    df.loc[i, "maleCast"] = castGenderList[2]




    crewString = df.loc[i, "crew"]
    crewListOfDicts = ast.literal_eval(crewString)
    #print(temporaryList)

    crewGenderList = [0, 0, 0]
    for characterDict in crewListOfDicts:
        ix = characterDict["gender"]
        crewGenderList[ix] += 1
    
    df.loc[i, "noDataCrew"] = crewGenderList[0]
    df.loc[i, "femaleCrew"] = crewGenderList[1]
    df.loc[i, "maleCrew"] = crewGenderList[2]


#inplace naredi, da ni vrnjen tak dataframe, ki nima teh columnov, ampak da se kar na tem to naredi
# axis=1 pa naredi, da se brise stolpce
df.drop(["crew", "cast"], axis=1, inplace=True)

df.rename(columns = {'id':'tmdbId'}, inplace = True)
    

df.to_csv("genderParsed.csv", index=False)



