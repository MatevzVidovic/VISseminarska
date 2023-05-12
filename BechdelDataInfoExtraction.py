import pandas as pd
 
dfAllData = pd.read_csv('allDataPlusBechdel.csv')


addingColumn = [None]* dfAllData.shape[0]

# dataframe.insert(loc, column, value, allow_duplicates)

#These will simply be ( numOfFem / (numOfFem + numOfMale)
# The third category has proven to be a mix of male and female, essentailly meaning noData.
# This is why I have to simply disregard it.
# It will be expressed in percent, and rounded to two decimal places.
# The value will be -1 if there are no male or female people recorded.
dfAllData.insert(0, "castFemalePercentage", addingColumn, True)
dfAllData.insert(1, "crewFemalePercentage", addingColumn, True)

dfAllData.insert(2, "movieDatasetRevenueRatio", addingColumn, True)
dfAllData.insert(3, "bechdelRevenueRatio", addingColumn, True)
# Tole je prislo isto, kot Bechdel:
# dfAllData.insert(4, "bechdelRevenuePercentageAdjustedInflation", addingColumn, True)



# What can be done on a single row:

for i in range (dfAllData.shape[0]):

    # castFemalePercentage:
    numOfFemCast = dfAllData.loc[i, "femaleCast"]
    numOfMaleCast = dfAllData.loc[i, "maleCast"]
    femaleCastPercentage = round(100 * numOfFemCast / (numOfFemCast + numOfMaleCast), 1) if (numOfFemCast + numOfMaleCast) != 0 else -1
    
    dfAllData.loc[i, "castFemalePercentage"] = femaleCastPercentage


    # crewFemalePercentage:
    numOfFemCrew = dfAllData.loc[i, "femaleCrew"]
    numOfMaleCrew = dfAllData.loc[i, "maleCrew"]
    femaleCrewPercentage = round(100 * numOfFemCrew / (numOfFemCrew + numOfMaleCrew), 1) if (numOfFemCrew + numOfMaleCrew) else -1
    
    dfAllData.loc[i, "crewFemalePercentage"] = femaleCrewPercentage


    # Revenue calculations as percentages of the budget:
    # Movie dataset:
    budget = dfAllData.loc[i, "budget_x"]
    revenue = dfAllData.loc[i, "revenue"]
    revenuePercentage = round(revenue/budget, 1) if revenue > 0 and budget > 0 else -1
    dfAllData.loc[i, "movieDatasetRevenueRatio"] = revenuePercentage

    # Bechdel:
    budget = dfAllData.loc[i, "budget_y"]
    revenue = dfAllData.loc[i, "domgross"] + dfAllData.loc[i, "intgross"]
    revenuePercentage = round(revenue/budget, 1) if revenue > 0 and budget > 0 else -1
    dfAllData.loc[i, "bechdelRevenueRatio"] = revenuePercentage

    
    # To pride pac isto, kot Bechdel:

    # Bechdel adjusted for inflation:
    # budget = dfAllData.loc[i, "budget_2013$"]
    # revenue = dfAllData.loc[i, "domgross_2013$"] + dfAllData.loc[i, "intgross_2013$"]
    # revenuePercentage = round(100 * revenue/budget, 1) if revenue > 0 and budget > 0 else -1
    # dfAllData.loc[i, "bechdelRevenuePercentageAdjustedInflation"] = revenuePercentage

    




# noDataCast,femaleCast,maleCast,noDataCrew,femaleCrew,maleCrew,tmdbId,movieId,imdbId,adult,budget_x,genres,imdb_id,original_language,original_title,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title_x,video,vote_average,vote_count,year,title_y,test,clean_test,binary,budget_y,domgross,intgross,code,budget_2013$,domgross_2013$,intgross_2013$,period code,decade code
print(dfAllData.columns)

# Popularity ne vem kako je izracunan, zato ne includeam.
# Budget je pomemben dejavnik za RevenueRatio in morda celo za vote_average, zato ju includeam.
dfNewData = dfAllData[["castFemalePercentage", "crewFemalePercentage", "budget_x", "movieDatasetRevenueRatio", "budget_y", "bechdelRevenueRatio",          "clean_test", "binary",          "popularity", "vote_average","vote_count"]]
dfNewData.to_csv("BechdelDataPrepared.csv", index=False)


