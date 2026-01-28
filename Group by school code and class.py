import pandas as pd

df = pd.DataFrame({
    'School_Code': ['S1', 'S1', 'S2'],
    'Class': ['10A', '10B', '10A'],
    'Age': [14, 15, 16]
})

print(df.groupby(['School_Code', 'Class']))
