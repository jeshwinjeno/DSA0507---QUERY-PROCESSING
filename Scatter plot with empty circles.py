import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(20)
y = np.random.rand(20)

plt.scatter(x, y, facecolors='none', edgecolors='black')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot with Empty Circles")
plt.show()
