import pandas as pd

df = pd.DataFrame({
    'School_Code': ['S1', 'S2', 'S1', 'S2'],
    'Age': [14, 15, 13, 16]
})

result = df.groupby('School_Code')['Age'].agg(['mean', 'min', 'max'])
print(result)
