import pandas as pd

df = pd.DataFrame({
    'Name': ['Python Programming', 'Data Science']
})

index = df['Name'].str.find('Data')
print(index)
