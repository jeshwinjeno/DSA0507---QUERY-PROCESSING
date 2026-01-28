import pandas as pd

jobs = pd.DataFrame({
    'job_id': ['DEV', 'HR', 'MGR'],
    'job_title': ['Developer', 'HR Executive', 'Manager']
})

print(jobs.sort_values(by='job_title', ascending=False))
