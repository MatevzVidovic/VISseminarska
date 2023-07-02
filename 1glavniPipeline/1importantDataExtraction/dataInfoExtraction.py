import pandas as pd

from datetime import datetime as dt

def decimalOfYearPassed (date):
    year = date.year
    startOfYear = dt(date.year, 1, 1)
    endOfYear = dt(date.year+1, 1, 1)
    secondsSoFar = (date - startOfYear).total_seconds()   # the date subtraction gives a timedelta object
    secondsOfYear = (endOfYear - startOfYear).total_seconds()
    decimalOfIt = round( (secondsSoFar / secondsOfYear), 4)
    return decimalOfIt

 
dfAllData = pd.read_csv('allData.csv')


addingColumn = [None]* dfAllData.shape[0]

# dataframe.insert(loc, column, value, allow_duplicates)

#These will simply be ( numOfFem / (numOfFem + numOfMale)
# The third category has proven to be a mix of male and female, essentailly meaning noData.
# This is why I have to simply disregard it.
# It will be expressed in percent, and rounded to two decimal places.
# The value will be -1 if there are no male or female people recorded.
dfAllData.insert(0, "castFemalePercentage", addingColumn, True)
dfAllData.insert(1, "crewFemalePercentage", addingColumn, True)

dfAllData.insert(2, "revenueRatio", addingColumn, True)
dfAllData.insert(3, "releaseYear", addingColumn, True)
dfAllData.insert(4, "releaseTimeOfYear", addingColumn, True)


# dfAllData.insert(3, "bechdelRevenueRatio", addingColumn, True)
# Tole je prislo isto, kot Bechdel:
# dfAllData.insert(4, "bechdelRevenuePercentageAdjustedInflation", addingColumn, True)

# Dodajam, ker bi mogoce lahko bilo uporabno imeti tudi revenue:
# (revenue_x delam le, ker je bolj pregledna tale koda, pa ne rabim renameat revenue iz prejsnje tabele)
# dfAllData.insert(3, "revenue_x", addingColumn, True)
# dfAllData.insert(5, "revenue_y", addingColumn, True)

# dfAllData.insert(6, "nowomen", addingColumn, True)
# dfAllData.insert(7, "notalk", addingColumn, True)
# dfAllData.insert(8, "men", addingColumn, True)
# dfAllData.insert(9, "dubious", addingColumn, True)
# dfAllData.insert(10, "ok", addingColumn, True)



# What can be done on a single row:

for i in range (dfAllData.shape[0]):

    # castFemalePercentage:
    numOfFemCast = dfAllData.loc[i, "femaleCast"]
    numOfMaleCast = dfAllData.loc[i, "maleCast"]
    femaleCastPercentage = round(100 * numOfFemCast / (numOfFemCast + numOfMaleCast), 1) if (numOfFemCast + numOfMaleCast) > 0 else -1
    
    dfAllData.loc[i, "castFemalePercentage"] = femaleCastPercentage


    # crewFemalePercentage:
    numOfFemCrew = dfAllData.loc[i, "femaleCrew"]
    numOfMaleCrew = dfAllData.loc[i, "maleCrew"]
    femaleCrewPercentage = round(100 * numOfFemCrew / (numOfFemCrew + numOfMaleCrew), 1) if (numOfFemCrew + numOfMaleCrew) > 0 else -1
    
    dfAllData.loc[i, "crewFemalePercentage"] = femaleCrewPercentage


    # Revenue calculations as percentages of the budget:
    # Movie dataset:
    budget = dfAllData.loc[i, "budget"]
    revenue = dfAllData.loc[i, "revenue"]
    revenuePercentage = round(revenue/budget, 10) if revenue > 0 and budget > 0 else -1
    dfAllData.loc[i, "revenueRatio"] = revenuePercentage
    # dfAllData.loc[i, "revenue_x"] = revenue



    dateString = dfAllData.loc[i, "release_date"]
    # print(type(dateString))
    try:
        splitDateArray = dateString.split("-")
        year = int(splitDateArray[0])
        month = int(splitDateArray[1])
        day = int(splitDateArray[2])
        # print(dateString)
        # print(year)
        # print(month)
        # print(day)
        currentDate = dt(year, month, day)
        # print(currentDate)
        dfAllData.loc[i, "releaseYear"] = year
        decimalOfYearSoFar = decimalOfYearPassed(currentDate)
        # print(decimalOfYearSoFar)
        dfAllData.loc[i, "releaseTimeOfYear"] = decimalOfYearSoFar
    except:
        print("Invalid date string: " + str(dateString))
        dfAllData.loc[i, "releaseYear"] = None
        dfAllData.loc[i, "releaseTimeOfYear"] = None




    originalLanguage = dfAllData.loc[i, "original_language"]
    if(type(originalLanguage) != str):
        print("Invalid original language type: " + str(type(originalLanguage)))
        print("Its language value: " + str(originalLanguage))
        dfAllData.loc[i, "original_language"] = "NoneString"
    



    # Bechdel:
    # budget = dfAllData.loc[i, "budget_y"]
    # revenue = dfAllData.loc[i, "domgross"] + dfAllData.loc[i, "intgross"]
    # revenuePercentage = round(revenue/budget, 10) if revenue > 0 and budget > 0 else -1
    # dfAllData.loc[i, "bechdelRevenueRatio"] = revenuePercentage
    # dfAllData.loc[i, "revenue_y"] = revenue


    # # Binary bechdel test:
    # binaryBechdel = dfAllData.loc[i, "binary"]
    # dfAllData.loc[i, "binary"] = 1 if binaryBechdel == "PASS" else (0 if "FAIL" else print("Binary bechdel, wrong value."))



    # # Clean bechdel test:

    # dfAllData.loc[i, "nowomen"] = 0
    # dfAllData.loc[i, "notalk"] = 0
    # dfAllData.loc[i, "men"] = 0
    # dfAllData.loc[i, "dubious"] = 0
    # dfAllData.loc[i, "ok"] = 0
    
    # clean_bechdel_string = dfAllData.loc[i, "clean_test"]
    # dfAllData.loc[i, clean_bechdel_string] = 1







    
    # To pride pac isto, kot Bechdel:

    # Bechdel adjusted for inflation:
    # budget = dfAllData.loc[i, "budget_2013$"]
    # revenue = dfAllData.loc[i, "domgross_2013$"] + dfAllData.loc[i, "intgross_2013$"]
    # revenuePercentage = round(100 * revenue/budget, 1) if revenue > 0 and budget > 0 else -1
    # dfAllData.loc[i, "bechdelRevenuePercentageAdjustedInflation"] = revenuePercentage

    




# 'castFemalePercentage', 'crewFemalePercentage', 'revenueRatio', 'noDataCast', 'femaleCast', 'maleCast', 'noDataCrew', 'femaleCrew', 'maleCrew', 'tmdbId', 'movieId', 'imdbId', 'adult', 'budget', 'genres', 'imdb_id', 'original_language', 'original_title', 'popularity', 'poster_path', 'production_companies', 'production_countries', 'release_date', 'revenue', 'runtime', 'spoken_languages', 'status', 'tagline', 'title', 'video', 'vote_average', 'vote_count'
print(dfAllData.columns)

# Popularity ne vem kako je izracunan, zato ne includeam.
# Includeam pa runtime, ker me zanima, kaksen je njegov vpliv.
# Budget je pomemben dejavnik za RevenueRatio in morda celo za vote_average, zato ju includeam.



# "release_date", dat v decimalko leta, ali pa samo leto vzet. Mogoče kar v 2 zadevi - leto kot celo st, in pa del leta kot decimalka med 0 in 1 
# "original_language", ta je se kar kul, ig bom pustil pa zanj naredil ANOVA da malo vidim              
# "popularity", nimam pojma kako ga dobijo
# 
# Ne bom vzel:
#  "spoken_languages" isto kot naslednje
# "production_countries", kinda koga briga, pa lahko jih je vec, pa malo vec za sparseat 
# "genres" isto
# "status" je samo ce je ze released
dfNewData = dfAllData[["castFemalePercentage", "crewFemalePercentage", "budget", "revenue", "revenueRatio",         "vote_average","vote_count",          "runtime",              "releaseYear", "releaseTimeOfYear", "original_language", "popularity"]]
dfNewData.to_csv("dataExtracted.csv", index=False)


