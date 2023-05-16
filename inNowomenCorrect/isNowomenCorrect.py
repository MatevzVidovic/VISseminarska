import pandas as pd
import ast
 
dfAllData = pd.read_csv('genderAndRawAllDataPlusBechdel.csv')

counter = 0
for ix in range(dfAllData.shape[0]):
    if dfAllData.loc[ix, "clean_test"] == "nowomen":
        print(dfAllData.loc[ix, "title_x"])
        print(dfAllData.loc[ix, "title_y"])
        print(dfAllData.loc[ix, "femaleCast"])
        counter += 1
        
        castString = dfAllData.loc[ix, "cast"]
        castDict = ast.literal_eval(castString)
        charactersString = ""
        for character in castDict:
            if character["gender"] == 1:
                charactersString += character["name"] + ", "
        
        print(charactersString)

print("How many times this happens:")
print(counter)

        