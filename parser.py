

import pandas as pd

import ast


def dictFinder(array_string):
    outputList = []

    inJSON = False
    startIX = -1
    for i in range(len(array_string)):
        if array_string[i] == '{':
            inJSON = True
            startIX = i
        elif array_string[i] == '}' and inJSON:
            outputList.append(array_string[startIX:i+1])
            inJSON = False
    return outputList





df = pd.read_csv('credits.csv')

for i in range (1000):
    castCompletelyString = df.loc[i].loc["cast"]


    #print(castCompletelyString)

    castListOfStrings = dictFinder(castCompletelyString)

    #print(castListOfStrings)

    vesCast = []
    for person in castListOfStrings:
        personDict = ast.literal_eval(person)
        vesCast.append(personDict)
    

    try:
        TomHanks = vesCast[0]
    except:
        a = 0
    print(TomHanks)
    print(type(TomHanks))

    if(i == 999):
            print(vesCast)
        

