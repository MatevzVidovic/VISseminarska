import pandas as pd

from datetime import datetime as dt


 
dfAllData = pd.read_csv('BechdelMovies.csv')


addingColumn = [None]* dfAllData.shape[0]

# dataframe.insert(loc, column, value, allow_duplicates)

#These will simply be ( numOfFem / (numOfFem + numOfMale)
# The third category has proven to be a mix of male and female, essentailly meaning noData.
# This is why I have to simply disregard it.
# It will be expressed in percent, and rounded to two decimal places.
# The value will be -1 if there are no male or female people recorded.

dfAllData.insert(0, "binaryPASS", addingColumn, True)
dfAllData.insert(1, "binaryFAIL", addingColumn, True)


dfAllData.insert(2, "nowomenCleanTest", addingColumn, True)
dfAllData.insert(3, "notalkCleanTest", addingColumn, True)
dfAllData.insert(4, "menCleanTest", addingColumn, True)
dfAllData.insert(5, "dubiousCleanTest", addingColumn, True)
dfAllData.insert(6, "okCleanTest", addingColumn, True)





# What can be done on a single row:

binaryPass = [0, 0]
cleanPass = [0, 0, 0, 0, 0]

for i in range (dfAllData.shape[0]):

    cleanTest = dfAllData.loc[i, "binary"]

    if cleanTest == "PASS":
       dfAllData.loc[i, "binaryPASS"] = 1
       binaryPass[0] += 1
    else:
       dfAllData.loc[i, "binaryPASS"] = 0

    if cleanTest == "FAIL":
       dfAllData.loc[i, "binaryFAIL"] = 1
       binaryPass[1] += 1
    else:
       dfAllData.loc[i, "binaryFAIL"] = 0
    



    cleanTest = dfAllData.loc[i, "clean_test"]

    if cleanTest == "nowomen":
       dfAllData.loc[i, "nowomenCleanTest"] = 1
       cleanPass[0] += 1
    else:
       dfAllData.loc[i, "nowomenCleanTest"] = 0
    

    if cleanTest == "notalk":
       dfAllData.loc[i, "notalkCleanTest"] = 1
       cleanPass[1] += 1
    else:
       dfAllData.loc[i, "notalkCleanTest"] = 0


    if cleanTest == "men":
       dfAllData.loc[i, "menCleanTest"] = 1
       cleanPass[2] += 1
    else:
       dfAllData.loc[i, "menCleanTest"] = 0


    if cleanTest == "dubious":
       dfAllData.loc[i, "dubiousCleanTest"] = 1
       cleanPass[3] += 1
    else:
       dfAllData.loc[i, "dubiousCleanTest"] = 0


    if cleanTest == "ok":
       dfAllData.loc[i, "okCleanTest"] = 1
       cleanPass[4] += 1
    else:
       dfAllData.loc[i, "okCleanTest"] = 0


    

        
print(dfAllData.shape)
print(binaryPass)
print(cleanPass)




# 'castFemalePercentage', 'crewFemalePercentage', 'revenueRatio', 'noDataCast', 'femaleCast', 'maleCast', 'noDataCrew', 'femaleCrew', 'maleCrew', 'tmdbId', 'movieId', 'imdbId', 'adult', 'budget', 'genres', 'imdb_id', 'original_language', 'original_title', 'popularity', 'poster_path', 'production_companies', 'production_countries', 'release_date', 'revenue', 'runtime', 'spoken_languages', 'status', 'tagline', 'title', 'video', 'vote_average', 'vote_count'
print(dfAllData.columns)


dfNewData = dfAllData[['binaryPASS', 'binaryFAIL', 'nowomenCleanTest', 'notalkCleanTest',  'menCleanTest', 'dubiousCleanTest', 'okCleanTest', 'year',            'budget', 'domgross', 'intgross', 'code', 'budget_2013$', 'domgross_2013$', 'intgross_2013$'                   'title', 'test', 'clean_test', 'binary',       'period code', 'decade code']]
dfNewData.to_csv("dataExtracted.csv", index=False)


