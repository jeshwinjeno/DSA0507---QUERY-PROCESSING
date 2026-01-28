import pandas as pd

job_history = pd.DataFrame({
    'emp_id': [101, 101, 102, 103, 103, 103],
    'job_id': ['DEV', 'TEST', 'HR', 'DEV', 'TEST', 'MGR']
})

result = job_history['emp_id'].value_counts()
print(result[result >= 2].index.tolist())
