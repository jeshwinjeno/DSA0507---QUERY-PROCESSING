import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [10, np.nan, 30],
    "B": [np.nan, 50, 60]
})

print("Before replacing:")
print(df)

df_filled = df.fillna(0)

print("\nAfter replacing:")
print(df_filled)
