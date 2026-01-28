import pandas as pd

sales = pd.DataFrame({
    'Region': ['East', 'West', 'East'],
    'Manager': ['A', 'B', 'A'],
    'Salesman': ['X', 'Y', 'Z'],
    'Sale': [500, 700, 300]
})

pivot = pd.pivot_table(
    sales,
    values='Sale',
    index=['Region', 'Manager', 'Salesman'],
    aggfunc='sum'
)

print(pivot)
