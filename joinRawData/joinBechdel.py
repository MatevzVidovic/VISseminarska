

import pandas as pd
 
dfAllSoFar = pd.read_csv('genderAndLinksAndMetadata.csv')
dfBechdel = pd.read_csv('BechdelMovies.csv')

print(dfAllSoFar.columns)
print(dfBechdel.columns)

dfBechdel.rename(columns = {'imdb':'imdb_id'}, inplace = True)

 
# inner join
df = pd.merge(dfAllSoFar, dfBechdel, on='imdb_id', how='inner')

df.to_csv("rawAllDataPlusBechdel.csv", index=False)

print(dfAllSoFar.shape[0])
print(dfBechdel.shape[0])
print(df.shape[0])