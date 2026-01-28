import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(15)
y = np.random.rand(15)
sizes = np.random.randint(50, 500, 15)

plt.scatter(x, y, s=sizes)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot with Different Marker Sizes")
plt.show()
