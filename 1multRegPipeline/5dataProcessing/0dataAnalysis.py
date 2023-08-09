import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm 


def countplot(inputArray, numOfBuckets=100, title=""):  
    fig, ax = plt.subplots()
    ax.hist(inputArray, numOfBuckets)
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    if(title != ""):
        plt.title(title)
    plt.show(block=False)

 
dfAllData = pd.read_csv('langPreparedData.csv')



# castFemalePercentage,crewFemalePercentage,budget,revenue,revenueRatio,
# vote_average,vote_count,runtime,releaseYear,releaseTimeOfYear,original_language,popularity

X = dfAllData[['castFemalePercentage', 'crewFemalePercentage', 'budget', 'runtime', 'releaseYear', 'releaseTimeOfYear']] 
y = dfAllData['vote_average'] 
dfAllData.head()


X = sm.add_constant(X) 
est = sm.OLS(y, X).fit() 
print(est.summary())

print()
print()
print()
print()
print()
print()



# Se je izkazalo za malo pointless:

# y = dfAllData['revenueRatio'] 
# est = sm.OLS(y, X).fit() 
# print(est.summary())

# print()
# print()
# print()





y = dfAllData['revenue'] 
est = sm.OLS(y, X).fit() 
print(est.summary())


# X = df.copy() 
# y = X.pop('chd') 
# df.head()

# y.groupby(X.famhist).mean()