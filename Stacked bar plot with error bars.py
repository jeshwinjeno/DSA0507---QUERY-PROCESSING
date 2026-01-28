import matplotlib.pyplot as plt
import numpy as np

men = [22, 30, 35, 35, 26]
women = [25, 32, 30, 35, 29]
men_std = [4, 3, 4, 1, 5]
women_std = [3, 5, 2, 3, 3]

x = np.arange(len(men))

plt.bar(x, men, yerr=men_std, label='Men')
plt.bar(x, women, bottom=men, yerr=women_std, label='Women')

plt.xlabel("Groups")
plt.ylabel("Scores")
plt.title("Stacked Bar Plot with Error Bars")
plt.legend()
plt.show()
