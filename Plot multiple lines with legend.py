import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [15, 25, 35, 45]

plt.plot(x, y1, label="Series 1")
plt.plot(x, y2, label="Series 2")
plt.legend()
plt.show()
