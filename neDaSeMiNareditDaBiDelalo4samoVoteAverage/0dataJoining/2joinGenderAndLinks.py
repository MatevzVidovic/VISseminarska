

import pandas as pd
 
dfGender = pd.read_csv('genderParsed.csv')
dfLinks = pd.read_csv('links.csv')

# Brez tega se duplicate pri kljucih naredijo vse kombinacije vrstic in imas na koncu vec vrstic
# kot si jih v enem od df imel na zacetku
dfGender.drop_duplicates(subset=["tmdbId"], keep=False, inplace=True)
dfLinks.drop_duplicates(subset=["tmdbId"], keep=False, inplace=True)

 
# inner join
df = pd.merge(dfGender, dfLinks, on='tmdbId', how='inner')

df.to_csv("genderAndLinks.csv", index=False)

print(dfGender.shape[0])
print(dfLinks.shape[0])
print(df.shape[0])