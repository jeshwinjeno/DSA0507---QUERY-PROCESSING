import pandas as pd
df = pd.DataFrame({
    "A": [1, np.nan, np.nan],
    "B": [np.nan, np.nan, 3],
    "C": [4, 5, np.nan]
})

result = df[df.isna().sum(axis=1) >= 2]
print(result)
