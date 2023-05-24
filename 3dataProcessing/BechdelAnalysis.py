import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def countplot(inputArray, numOfBuckets=100, title=""):  
    fig, ax = plt.subplots()
    ax.hist(inputArray, numOfBuckets)
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    if(title != ""):
        plt.title(title)
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
# print(arrMoviesDBIndepVars)
arrBechdel = dfBechdel.to_numpy()

arrRevenue_x = dfRevenue_x.to_numpy()
arrRevenue_y = dfRevenue_y.to_numpy()
arrVote_average = dfVote_average.to_numpy()
# print(arrRevenue_y)



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



# print(arrMoviesDBmeans)
# print(arrMoviesDBstds)

# print(arrBechdelMeans)
# print(arrBechdelStds)

# print(arrRevenue_xMean)
# print(arrRevenue_xStd)

# print(arrRevenue_yMean)
# print(arrRevenue_yStd)

# print(arrVote_averageMean)
# print(arrVote_averageStd)





# testArray1 = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
# testArray2 = np.array([[1, 2, 3]], np.int32)
# testRes1 = testArray1 / testArray2
# print(testRes1)








normMoviesDBIndepVars = (arrMoviesDBIndepVars - arrMoviesDBmeans) / arrMoviesDBstds
normBechdel = (arrBechdel - arrBechdelMeans) / arrBechdelStds

normRevenue_x = (arrRevenue_x - arrRevenue_xMean) / arrRevenue_xStd
normRevenue_y = (arrRevenue_y - arrRevenue_yMean) / arrRevenue_yStd
normVote_average = (arrVote_average - arrVote_averageMean) / arrVote_averageStd




# print(normMoviesDBIndepVars)
# print(normBechdel)

# print(normRevenue_x)
# print(normRevenue_y)
# print(normVote_average)






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

# countplot(reasonableNormMoviesDBIndepVars, 200)
# countplot(reasonableNormBechdel, 200)



# countplot(reasonableNormBechdel[:,1], 200)
# countplot(arrBechdel[:,1], 200)


reasonableNormMoviesDBIndepVarsAccountingForBechdel = np.concatenate((normMoviesDBIndepVars[:,0:4], arrMoviesDBIndepVars[:,4:]), axis=1)
reasonableNormBechdelAccountingForBechdel= np.concatenate((normBechdel[:,0:4], arrBechdel[:,4:]), axis=1)

# print(reasonableNormMoviesDBIndepVarsAccountingForBechdel)
# print(reasonableNormBechdelAccountingForBechdel)





# input("Blocking until you press enter:")





# Zdaj je plan uporabiti Moore-Penrose psevdoinverz za izracun najboljsih koeficientov v multilinearni regresiji.
# Povsod se uporablja linearna funkcija (k*x + c), torej v vseh obstojecih stolpcih samo ostane trenutna vrednost (saj je to x).
# K-ji bodo vektor koeficientov.

# C-ji pri vseh funkcijah pa se bodo sesteli v en sam C.
# Zanj moramo v matriko M na levo dodati stolpec samih 1 - da je (C = coef * 1 = coef), torej je C simple razbrati.
# Dobljen koeficient za ta stolpcec pa bo toraj povedal, kaksen je sestevek teh C.

# M * vecCoef = vecDepenVars
# M+ * M * vecCoef = M+ * vecDepenVars
# vecCoef = M+ * vecDepenVars


# norm izvedba, reasonable izvedba, reasonableAccountingForIzvedba. Za relevant revenue in za vote_average.

moviesDBmatrices = [normMoviesDBIndepVars, reasonableNormMoviesDBIndepVars, reasonableNormMoviesDBIndepVarsAccountingForBechdel]
bechdelMatrices = [normBechdel, reasonableNormBechdel, reasonableNormBechdelAccountingForBechdel]

dependentVarsVectors = [normRevenue_x, normRevenue_y, normVote_average]

relevantMatrices = moviesDBmatrices + bechdelMatrices

coefficientsList = []
for matrix in relevantMatrices:
    # numOfRows = matrix.shape[0]
    # print("numOfRows:")
    # print(numOfRows)
    vecOfOnes = np.ones_like(matrix[:,0:1])
    # print(vecOfOnes)
    # print(vecOfOnes.shape)

    # print("Shape of matrix before preparation for inversing:")
    # print(matrix.shape)

    matrix = np.concatenate((vecOfOnes, matrix), axis=1)
    # print(matrix)
    # print("Shape of matrix prepared for inversing:")
    # print(matrix.shape)

    Mplus = np.linalg.pinv(matrix)


    for dependantVec in dependentVarsVectors:
        resultingCoefs = np.matmul(Mplus, dependantVec)
        coefficientsList.append(resultingCoefs)

# print(coefficientsList)



# make names for figures
depNames = ["normMoviesDBIndepVars", "reasonableNormMoviesDBIndepVars", "reasonableNormMoviesDBIndepVarsAccountingForBechdel", "normBechdel", "reasonableNormBechdel", "reasonableNormBechdelAccountingForBechdel"]
indepNames = ["normRevenue_x", "normRevenue_y", "normVote_average"]
titleNames = []
for i in depNames:
    for j in indepNames:
        titleNames.append(i + "    to    " + j)



for ix, coeffVector in enumerate(coefficientsList):
    
    if ix < 3*3 and ix%3 == 1:
        continue
    if ix >= 3*3 and ix%3 == 0:
        continue

    fig, ax = plt.subplots()
    coeffVector = (np.transpose(coeffVector))[0,:]
    # print(coeffVector)
    # print(coeffVector.shape)
    # print(list(dfMoviesDBIndepVars.columns))
    dependantVarNames = ["constant"] + list(dfMoviesDBIndepVars.columns[0:coeffVector.size-1])
    ax.bar(dependantVarNames, coeffVector)
    plt.title(titleNames[ix])
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    plt.show(block=False)



input("Blocking until you press enter:")











# !!!
# !!!
# Cilj je preveriti normality hypothesis napak. In cilj je preveriti unbiasedness napak.
# !!!
# Spodaj je kopija kode zgoraj, le da bom tokrat gledal napake, ki jih model povzroci.
# Torej, ustvaril bom vektorje:    vecDepenVars - (M+ * vecDepenVars)
# Potem pa gledal njihov countplot/histogram.
# !!!
# Ideja je - malo bolj razdelane zgornje enacbe:
# M * vecCoef + error = vecDepenVars
# M+ * M * vecCoef + M+ * error = M+ * vecDepenVars
# vecCoef + M+ * error = M+ * vecDepenVars
# M * vecCoef + M * M+ * error  = M * M+ * vecDepenVars
# M * vecCoef + error  = vecDepenVars
# error = vecDepenVars - M * vecCoef
# !!!
# !!!


# norm izvedba, reasonable izvedba, reasonableAccountingForIzvedba. Za relevant revenue in za vote_average.

moviesDBmatrices = [normMoviesDBIndepVars, reasonableNormMoviesDBIndepVars, reasonableNormMoviesDBIndepVarsAccountingForBechdel]
bechdelMatrices = [normBechdel, reasonableNormBechdel, reasonableNormBechdelAccountingForBechdel]

dependentVarsVectors = [normRevenue_x, normRevenue_y, normVote_average]

relevantMatrices = moviesDBmatrices + bechdelMatrices

errorVectors = []
for matrix in relevantMatrices:
    # numOfRows = matrix.shape[0]
    # print("numOfRows:")
    # print(numOfRows)
    vecOfOnes = np.ones_like(matrix[:,0:1])

    matrix = np.concatenate((vecOfOnes, matrix), axis=1)
    
    Mplus = np.linalg.pinv(matrix)

    for dependantVec in dependentVarsVectors:
        resultingCoefs = np.matmul(Mplus, dependantVec)
        resultingErrors = dependantVec -  np.matmul(matrix, resultingCoefs)

        errorVectors.append(resultingErrors)

# print(errorVectors)



# make names for figures
depNames = ["normMoviesDBIndepVars", "reasonableNormMoviesDBIndepVars", "reasonableNormMoviesDBIndepVarsAccountingForBechdel", "normBechdel", "reasonableNormBechdel", "reasonableNormBechdelAccountingForBechdel"]
indepNames = ["normRevenue_x", "normRevenue_y", "normVote_average"]
titleNames = []
for i in depNames:
    for j in indepNames:
        titleNames.append(i + " attempt.  "  + "Bias (sum of errors) of " + j)

for ix, errorVector in enumerate(errorVectors):
    if ix < 3*3 and ix%3 == 1:
        continue
    if ix >= 3*3 and ix%3 == 0:
        continue

    # countplot(errorVector, title=titleNames[ix])

    bias = np.sum(errorVector)
    # bias = (np.count_nonzero(errorVector > 0) - np.count_nonzero(errorVector < 0)) / (np.count_nonzero(errorVector > 0) + np.count_nonzero(errorVector <= 0))
    print(titleNames[ix])
    print(bias)

input("Blocking until you press enter:")

















