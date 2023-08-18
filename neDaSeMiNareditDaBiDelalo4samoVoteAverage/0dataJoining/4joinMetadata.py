

import pandas as pd
 
dfGenderAndLinks = pd.read_csv('directorAndGenderAndLinks.csv')
dfMetadata = pd.read_csv('movies_metadata.csv')

print(dfMetadata.columns)
for ix, elem in enumerate(dfMetadata.loc[ : , "id"]):
    try:
        int(elem)
    except:
        print(dfMetadata.loc[ix, "id"])
        dfMetadata.drop(ix, inplace=True)
        print(elem)


# print(len(dfMetadata.loc[:,"id"]))
# print(len(dfMetadata.loc[:,"id"].drop_duplicates()))
# print(len(dfGenderAndLinks.loc[:,"tmdbId"]))
# print(len(dfGenderAndLinks.loc[:,"tmdbId"].drop_duplicates()))

# print(dfMetadata.loc[dfMetadata.duplicated(['id'], keep=False), ["imdb_id", "title"]])

 

dfMetadata.rename(columns = {'id':'tmdbId'}, inplace = True)
dfMetadata.drop(["belongs_to_collection", "homepage", "overview"], axis=1, inplace=True)

dfMetadata['tmdbId']=dfMetadata['tmdbId'].astype(int)


# Brez tega se duplicate pri kljucih naredijo vse kombinacije vrstic in imas na koncu vec vrstic
# kot si jih v enem od df imel na zacetku
dfGenderAndLinks.drop_duplicates(subset=["tmdbId"], keep=False, inplace=True)
dfMetadata.drop_duplicates(subset=["tmdbId"], keep=False, inplace=True)

# inner join
df = pd.merge(dfGenderAndLinks, dfMetadata, on='tmdbId', how='inner')

# Zdaj ko imam ze to zgoraj vec ne potrebujem tega linea.
# df.drop_duplicates(subset=["tmdbId"], keep=False, inplace=True)

df.to_csv("allData.csv", index=False)

print("This many lines before: ")
print(dfGenderAndLinks.shape[0])
print("This many lines after: ")
print(df.shape[0])