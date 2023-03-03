

import pandas as pd

import ast



df = pd.read_csv('credits.csv')

for i in range (1000):
    castString = df.loc[i].loc["cast"]


    #print(castListOfStrings)

    vesCast = personDict = ast.literal_eval(castString)
    

    try:
        TomHanks = vesCast[0].get("gender")
    except:
        a = 0
    # print(TomHanks)
    # print(type(TomHanks))

    if(i == 999):
            print(vesCast)
        

