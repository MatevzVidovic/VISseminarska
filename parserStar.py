

import pandas as pd
import json

import ast


def JSONfinder(array_string):
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

    # print(castCompletelyString)

    # print(i)

    #print(castCompletelyString)

    castListOfStrings = JSONfinder(castCompletelyString)

    #print(castListOfStrings)

    vesCast = []
    for person in castListOfStrings:
        person = person.replace("'", "\"")
        #print(person)
        #print(vesCast)
        try:
            vesCast.append(json.loads(person))
        except:
            print(person)
            print(i)



# TomHanks = vesCast[0]
# print(TomHanks)