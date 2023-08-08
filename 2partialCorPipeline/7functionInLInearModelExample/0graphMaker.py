import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

 




# fig, ax = plt.subplots()
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3]) 
# plt.show()

visina = np.random.rand(150)
visina = visina * 10 + 5

randomAbsoluteError = np.random.rand(150)
randomAbsoluteError *= 20

randomSign = np.random.rand(150)
randomSign[randomSign >= 0.5]

randomAddingOfError = randomAbsoluteError * randomSign

teza = visina ** (2) + randomAddingOfError



fig, ax = plt.subplots()
ax.scatter(visina, teza)

plt.title("")

try:
    k, c = np.polyfit(visina, teza, deg=1)
    xseq = np.linspace(min(visina), max(visina), num=100)
    ax.plot(xseq, c + k * xseq, color="k", lw=1.5)
except:
    print("Regression unable")

# mng = plt.get_current_fig_manager()
# mng.resize(*mng.window.maxsize())


# manager = plt.get_current_fig_manager()
# manager.full_screen_toggle()
plt.show(block=False)




visina = visina ** 2

fig, ax = plt.subplots()
ax.scatter(visina, teza)

plt.title("")

try:
    k, c = np.polyfit(visina, teza, deg=1)
    xseq = np.linspace(min(visina), max(visina), num=100)
    ax.plot(xseq, c + k * xseq, color="k", lw=1.5)
except:
    print("Regression unable")

# mng = plt.get_current_fig_manager()
# mng.resize(*mng.window.maxsize())


# manager = plt.get_current_fig_manager()
# manager.full_screen_toggle()
plt.show(block=False)






input("Blocking until you press enter.")





