import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def countplot(inputArray, numOfBuckets=100):  
    fig, ax = plt.subplots()
    ax.hist(inputArray, numOfBuckets)
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    plt.show(block=False)

 
dfAllData = pd.read_csv('BechdelCleanedData.csv')


castFemPercent = dfAllData.loc[:, "castFemalePercentage"].tolist()

# castFemalePercentage,crewFemalePercentage,budget_x,revenue_x,movieDatasetRevenueRatio,budget_y,revenue_y,bechdelRevenueRatio,vote_average,vote_count,runtime,binary,nowomen,notalk,men,dubious,ok,clean_test
dfMoviesDBIndepVars = dfAllData[["castFemalePercentage", "crewFemalePercentage", "budget_x", "runtime", "binary", "nowomen", "notalk", "men", "dubious", "ok"]]
dfBechdel = dfAllData[["castFemalePercentage", "crewFemalePercentage", "budget_y", "runtime", "binary", "nowomen", "notalk", "men", "dubious", "ok"]]

dfRevenue_x = dfAllData[["revenue_x"]]
dfRevenue_y = dfAllData[["revenue_y"]]
dfVote_average = dfAllData[["vote_average"]]




arrMoviesDBIndepVars = dfMoviesDBIndepVars.to_numpy()
print(arrMoviesDBIndepVars)
arrBechdel = dfBechdel.to_numpy()

arrRevenue_x = dfRevenue_x.to_numpy()
arrRevenue_y = dfRevenue_y.to_numpy()
arrVote_average = dfVote_average.to_numpy()
print(arrRevenue_y)



arrMoviesDBmeans = np.mean(arrMoviesDBIndepVars, axis=0)
arrMoviesDBstds = np.std(arrMoviesDBIndepVars, axis=0)

arrBechdelMeans = np.mean(arrBechdel, axis=0)
arrBechdelStds = np.std(arrBechdel, axis=0)

arrRevenue_xMean = np.mean(arrRevenue_x, axis=0)
arrRevenue_xStd = np.std(arrRevenue_x, axis=0)

arrRevenue_yMean = np.mean(arrRevenue_y, axis=0)
arrRevenue_yStd = np.std(arrRevenue_y, axis=0)

arrVote_averageMean = np.mean(arrVote_average, axis=0)
arrVote_averageStd = np.std(arrVote_average, axis=0)



print(arrMoviesDBmeans)
print(arrMoviesDBstds)

print(arrBechdelMeans)
print(arrBechdelStds)

print(arrRevenue_xMean)
print(arrRevenue_xStd)

print(arrRevenue_yMean)
print(arrRevenue_yStd)

print(arrVote_averageMean)
print(arrVote_averageStd)





testArray1 = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
testArray2 = np.array([[1, 2, 3]], np.int32)
testRes1 = testArray1 / testArray2
print(testRes1)








normMoviesDBIndepVars = (arrMoviesDBIndepVars - arrMoviesDBmeans) / arrMoviesDBstds
normBechdel = (arrBechdel - arrBechdelMeans) / arrBechdelStds

normRevenue_x = (arrRevenue_x - arrRevenue_xMean) / arrRevenue_xStd
normRevenue_y = (arrRevenue_y - arrRevenue_yMean) / arrRevenue_yStd
normVote_average = (arrVote_average - arrVote_averageMean) / arrVote_averageStd




print(normMoviesDBIndepVars)
print(normBechdel)

print(normRevenue_x)
print(normRevenue_y)
print(normVote_average)









# countplot(arrMoviesDBIndepVars)
# countplot(arrBechdel)

# countplot(arrRevenue_x)
# countplot(arrRevenue_y)
# countplot(arrVote_average)



# countplot(arrMoviesDBmeans)
# countplot(arrMoviesDBstds)

# countplot(arrBechdelMeans)
# countplot(arrBechdelStds)

# countplot(arrRevenue_xMean)
# countplot(arrRevenue_xStd)

# countplot(arrRevenue_yMean)
# countplot(arrRevenue_yStd)

# countplot(arrVote_averageMean)
# countplot(arrVote_averageStd)













# countplot(normMoviesDBIndepVars, 200)
# countplot(normBechdel, 200)

# countplot(normRevenue_x)
# countplot(normRevenue_y)
# countplot(normVote_average)

# print(normBechdel[0,:])


reasonableNormMoviesDBIndepVars = normMoviesDBIndepVars[:,0:4]
reasonableNormBechdel= normBechdel[:,0:4]

countplot(reasonableNormMoviesDBIndepVars, 200)
countplot(reasonableNormBechdel, 200)





countplot(reasonableNormBechdel[:,1], 200)
countplot(arrBechdel[:,1], 200)








input("Blocking until you press enter:")










# This conversion to numpy arrays just doesn't seem to work:


# listOfArrays = []

# columnNames = dfAllData.columns
# for ix in range(dfAllData.shape[1]):
#     listOfArrays.append(dfAllData[ix].to_numpy())
    # currColumn = dfAllData.iloc[:, ix].tolist()
    # listOfArrays.append(np.array(currColumn))

# print(listOfArrays)




# listOfMeans = []
# listOfStandardDeviations = []

# for ix in range(len(listOfArrays)-1):
#     listOfMeans.append(np.mean(listOfArrays[ix]))
#     listOfStandardDeviations.append(np.std(listOfArrays[ix]))

# print(listOfMeans)
# print(listOfStandardDeviations)




# listOfNormalizedArrays = []

# for ix in range(len(listOfArrays)-1):
#     arrayToAppend = (listOfArrays[ix] - listOfMeans[ix]) / listOfStandardDeviations[ix]
#     listOfNormalizedArrays.append(arrayToAppend)

# print(listOfNormalizedArrays)




# concatenatedArray = listOfNormalizedArrays[0]
# for ix in range(1, len(listOfNormalizedArrays)):
#     np.concatenate((concatenatedArray, listOfNormalizedArrays[ix]), axis=0)
# print(concatenatedArray)
# concatenatedArray = np.transpose(concatenatedArray)
# print(concatenatedArray)



