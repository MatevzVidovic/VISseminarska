

import pandas as pd
 
dfCredits = pd.read_csv('credits.csv')
dfLinks = pd.read_csv('links.csv')
 

dfCredits.rename(columns = {'id':'tmdbId'}, inplace = True)
 
# inner join
df = pd.merge(dfCredits, dfLinks, on='tmdbId', how='inner')


df.to_csv("genderAndLinks.csv", index=False)

print(dfCredits.shape[0])
print(dfLinks.shape[0])
print(df.shape[0])