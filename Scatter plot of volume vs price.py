import matplotlib.pyplot as plt

price = [100, 105, 102]
volume = [1200, 1500, 1000]

plt.scatter(price, volume)
plt.xlabel("Stock Price")
plt.ylabel("Volume")
plt.title("Price vs Volume")
plt.show()
