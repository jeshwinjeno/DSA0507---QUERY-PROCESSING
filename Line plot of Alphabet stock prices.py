import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Date": ["2023-01-01","2023-01-02","2023-01-03"],
    "Close": [100, 105, 102]
}

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])

plt.plot(df["Date"], df["Close"])
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.title("Alphabet Stock Prices")
plt.show()
