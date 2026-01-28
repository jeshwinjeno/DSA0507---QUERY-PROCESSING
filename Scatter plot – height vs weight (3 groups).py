import matplotlib.pyplot as plt

height1 = [150, 155, 160]
weight1 = [50, 55, 60]

height2 = [165, 170, 175]
weight2 = [65, 70, 75]

height3 = [180, 185, 190]
weight3 = [80, 85, 90]

plt.scatter(height1, weight1, label='Group 1')
plt.scatter(height2, weight2, label='Group 2')
plt.scatter(height3, weight3, label='Group 3')

plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height vs Weight Comparison")
plt.legend()
plt.show()
