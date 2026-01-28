import pandas as pd

df = pd.DataFrame({
    'Text': ['Python', 'DataFrame', 'PANDAS']
})

df['Swapped'] = df['Text'].str.swapcase()
print(df)
