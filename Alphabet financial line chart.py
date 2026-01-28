import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Date": ["10-03-16","10-04-16","10-05-16"],
    "Close": [772.56, 776.43, 776.47]
}

df = pd.DataFrame(data)
plt.plot(df["Date"], df["Close"])
plt.show()
