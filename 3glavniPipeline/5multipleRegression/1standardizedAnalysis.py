
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

X = dfAllData[['directorGender', 'castFemalePercentage', 'crewFemalePercentage', 'budget', 'runtime', 'releaseYear', 'releaseTimeOfYear']] 

Y = ['vote_average', 'revenue', 'revenueRatio']


indepNp = X.to_numpy()
indepMeans = np.mean(indepNp, axis=0)
indepStds = np.std(indepNp, axis=0)

# Kategoricne spremenljivke ne bom standardiziral, ker mi bo bolj interpretabilno
for ix in range(1, X.shape[1]):
    X.iloc[:, ix] = X.apply(lambda col : ((col[ix] - indepMeans[ix]) / indepStds[ix]), axis = 1)

X = sm.add_constant(X) 




for i in Y:
    y = dfAllData[i]
    depNp = y.to_numpy()
    depMean = np.mean(depNp, axis=0)
    depStd = np.std(depNp, axis=0)

    y1 = y.apply(lambda col : ((col - depMean) / depStd))

    # print(dfAllData.head())
    
    est = sm.OLS(y1, X).fit() 
    print(est.summary())

    print()
    print()
    print()
    print()
    print()
    print()








# Se je izkazalo za malo pointless:

# y = dfAllData['revenueRatio'] 

# depNp = y.to_numpy()

# depMean = np.mean(depNp, axis=0)

# depStd = np.std(depNp, axis=0)

# y1 = y.apply(lambda col : ((col - depMean) / depStd))

# est = sm.OLS(y1, X).fit() 
# print(est.summary())

# print()
# print()
# print()





# y = dfAllData['revenue']


# depNp = y.to_numpy()

# depMean = np.mean(depNp, axis=0)

# depStd = np.std(depNp, axis=0)


# y1 = y.apply(lambda col : ((col - depMean) / depStd))

# est = sm.OLS(y1, X).fit() 
# print(est.summary())






# X = df.copy() 
# y = X.pop('chd') 
# df.head()

# y.groupby(X.famhist).mean()