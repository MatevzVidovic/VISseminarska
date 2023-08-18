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

 
dfAllData = pd.read_csv('dataExtracted.csv')



# castFemalePercentage,crewFemalePercentage,budget,revenue,revenueRatio,
# vote_average,vote_count,runtime,releaseYear,releaseTimeOfYear,original_language,popularity

Y = dfAllData[['budget_2013$', 'domgross_2013$', 'intgross_2013$']] # 'budget', 'domgross', 'intgross',

           
X = dfAllData[['binaryPASS', 'year']] 
dfAllData.head()
X = sm.add_constant(X) 

for i in Y:
    y = dfAllData[i] 
    est = sm.OLS(y, X).fit() 
    print(est.summary())

    print()
    print()
    print()
    print()
    print()
    print()


X = dfAllData[['notalkCleanTest',  'menCleanTest', 'dubiousCleanTest', 'okCleanTest', 'year']]
dfAllData.head()
X = sm.add_constant(X) 

for i in Y:
    y = dfAllData[i] 
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


# X = df.copy() 
# y = X.pop('chd') 
# df.head()

# y.groupby(X.famhist).mean()