import pandas as pd

sales = pd.DataFrame({
    'Item': ['Pen', 'Pen', 'Pencil', 'Pencil'],
    'Sale': [100, 150, 80, 120]
})

pivot = pd.pivot_table(sales, values='Sale', index='Item',
                       aggfunc=['max', 'min'])
print(pivot)
