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

 
dfAllData = pd.read_csv('preparedData.csv')



# castFemalePercentage,crewFemalePercentage,budget,revenue,revenueRatio,
# vote_average,vote_count,runtime,releaseYear,releaseTimeOfYear,original_language,popularity

X = dfAllData[['castFemalePercentage', 'crewFemalePercentage', 'budget', 'runtime', 'releaseYear', 'releaseTimeOfYear']] 
y = dfAllData['revenueRatio'] 
dfAllData.head()


X = sm.add_constant(X) 
est = sm.OLS(y, X).fit() 
print(est.summary())


y = dfAllData['vote_average'] 
est = sm.OLS(y, X).fit() 
print(est.summary())


# X = df.copy() 
# y = X.pop('chd') 
# df.head()

# y.groupby(X.famhist).mean()