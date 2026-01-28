import pandas as pd

df = pd.DataFrame({
    'Country': ['India', 'USA'],
    'Beer': [1.2, 2.5],
    'Wine': [0.5, 1.8]
})

print("Shape:", df.shape)
print("Columns:", df.columns)
