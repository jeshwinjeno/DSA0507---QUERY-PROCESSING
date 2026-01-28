import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Date': ['Day1', 'Day2', 'Day3'],
    'Volume': [3000, 4500, 2800]
})

plt.bar(data['Date'], data['Volume'])
plt.title("Trading Volume")
plt.show()
