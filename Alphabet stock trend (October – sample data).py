import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Date': pd.date_range('2016-10-01', periods=5),
    'Price': [780, 790, 800, 810, 820]
})

plt.plot(df['Date'], df['Price'])
plt.title("Alphabet Stock Trend (Oct 2016)")
plt.show()
