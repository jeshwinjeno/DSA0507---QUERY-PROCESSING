import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Date': pd.date_range('2023-01-01', periods=5),
    'Close': [100, 105, 102, 108, 110]
})

plt.plot(data['Date'], data['Close'])
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Alphabet Stock Prices")
plt.show()
