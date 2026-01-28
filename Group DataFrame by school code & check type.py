import pandas as pd

df = pd.DataFrame({
    'School_Code': ['S1', 'S2', 'S1'],
    'Age': [14, 15, 13]
})

grouped = df.groupby('School_Code')

print(type(grouped))
