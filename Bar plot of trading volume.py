import matplotlib.pyplot as plt

dates = ["Day1","Day2","Day3"]
volume = [1200, 1500, 1000]

plt.bar(dates, volume)
plt.xlabel("Date")
plt.ylabel("Volume")
plt.title("Trading Volume")
plt.show()
