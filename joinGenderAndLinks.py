

import pandas as pd
 
dfGender = pd.read_csv('genderParsed.csv')
dfLinks = pd.read_csv('links.csv')
 
 
# inner join
df = pd.merge(dfGender, dfLinks, on='tmdbId', how='inner')

df.to_csv("genderAndLinks.csv", index=False)

print(dfGender.shape[0])
print(dfLinks.shape[0])
print(df.shape[0])