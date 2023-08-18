

import pandas as pd

import ast


def directorPrinter(crewListOfDicts):
    namesString = ""
    for crewDict in crewListOfDicts:
        if (crewDict["job"] == "Director"):
            namesString += crewDict["name"] + ", "

    print(namesString)


# nrows=1 za omejitev stevila prebranih vrstic
df = pd.read_csv('credits.csv')

# dataframe.insert(loc, column, value, allow_duplicates) 
initGenderCol = [None]* df.shape[0]
df.insert(0, "directorGender", initGenderCol, True)

# print(df.shape)
# print(df.loc[[0, 10]])

counterArray = [0, 0, 0, 0, 0]

for i in range (df.shape[0]):
    crewString = df.loc[i, "crew"]
    crewListOfDicts = ast.literal_eval(crewString)
    
    directorGenderList = [0, 0, 0]
    directorNum = 0
    for crewDict in crewListOfDicts:
        if (crewDict["job"] == "Director"):
            ix = crewDict["gender"]
            directorGenderList[ix] += 1
            directorNum += 1
    

    # 0 for male, 1 for female, 2 for no data, 3 for no directors, 4 for many directors
    finalNumber = 0
    if (directorNum) == 1:
        if (directorGenderList[0] == 1):
            finalNumber = 2
        if (directorGenderList[1] == 1):
            finalNumber = 1
        if (directorGenderList[2] == 1):
            finalNumber = 0
    else:
        if directorNum == 0:
            finalNumber = 3
        else:
            finalNumber = 4
    


    counterArray[finalNumber] += 1

    #  if (finalNumber == 0):
    #     directorPrinter(crewListOfDicts)
    # if (finalNumber == 1):
    #     directorPrinter(crewListOfDicts)
    #  if (finalNumber == 2):
    #     directorPrinter(crewListOfDicts)

    df.loc[i, "directorGender"] = finalNumber



print(counterArray)

#inplace naredi, da ni vrnjen tak dataframe, ki nima teh columnov, ampak da se kar na tem to naredi
# axis=1 pa naredi, da se brise stolpce
df.drop(["crew", "cast"], axis=1, inplace=True)

df.rename(columns = {'id':'tmdbId'}, inplace = True)
    

df.to_csv("directorGenderParsed.csv", index=False)



