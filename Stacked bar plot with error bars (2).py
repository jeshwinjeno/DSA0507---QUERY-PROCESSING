import matplotlib.pyplot as plt

boys = [20, 35, 30]
girls = [25, 32, 34]

plt.bar([1, 2, 3], boys, yerr=2)
plt.bar([1, 2, 3], girls, bottom=boys, yerr=2)
plt.show()
