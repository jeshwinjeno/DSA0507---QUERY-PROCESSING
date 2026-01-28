import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Price': [100, 105, 102, 108],
    'Volume': [2000, 3000, 2500, 4000]
})

plt.scatter(data['Price'], data['Volume'])
plt.xlabel("Price")
plt.ylabel("Volume")
plt.show()
