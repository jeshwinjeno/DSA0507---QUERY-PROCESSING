import pandas as pd

sales = pd.DataFrame({
    'Item': ['Pen', 'Pen', 'Pencil'],
    'Units': [10, 20, 15]
})

pivot = pd.pivot_table(sales, values='Units',
                       index='Item', aggfunc='sum')
print(pivot)
