
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

 
dfAllData = pd.read_csv('BechdelDataPrepared.csv')










# fig, ax = plt.subplots()
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3]) 
# plt.show()

castFemPercent = dfAllData.loc[:, "castFemalePercentage"].tolist()
revenueRatio = dfAllData.loc[:, "movieDatasetRevenueRatio"].tolist()
# da ne bo popalo napacnih elementov gremo v rikverc smeri
for ix, val in reversed(list(enumerate(revenueRatio))):
    if (val > 4 or val < 0):
        castFemPercent.pop(ix)
        revenueRatio.pop(ix)

fig, ax = plt.subplots()
ax.scatter(castFemPercent, revenueRatio)

# Fit linear regression via least squares with numpy.polyfit
# It returns an slope (b) and intercept (a)
# deg=1 means linear fit (i.e. polynomial of degree 1)
b, a = np.polyfit(castFemPercent, revenueRatio, deg=1)

# Create sequence of 100 numbers from 0 to 100 
xseq = np.linspace(0, 100, num=100)

# Plot regression line
ax.plot(xseq, a + b * xseq, color="k", lw=2.5)

plt.show()











dfAllData.shape[1]

 





# df.to_csv("genderAndLinks.csv", index=False)

