import pandas as pd

employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4, 5],
    'department_id': [10, 20, 10, 30, 20]
})

print(employees['department_id'].unique())
