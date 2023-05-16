import pandas as pd
 
dfAllData = pd.read_csv('rawAllDataPlusBechdel.csv')

for ix in range(dfAllData.shape[0]):
    if dfAllData.loc[ix, "clean_test"] == "nowomen":
        print(dfAllData.loc[ix, "title_x"])
        print(dfAllData.loc[ix, "title_y"])

        