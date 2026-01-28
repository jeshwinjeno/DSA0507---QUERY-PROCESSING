import matplotlib.pyplot as plt
import numpy as np

men = [22, 30, 35, 35, 26]
women = [25, 32, 30, 35, 29]

x = np.arange(len(men))

plt.bar(x - 0.2, men, width=0.4, label='Men')
plt.bar(x + 0.2, women, width=0.4, label='Women')

plt.xlabel("Groups")
plt.ylabel("Scores")
plt.title("Scores by Group and Gender")
plt.legend()
plt.show()
