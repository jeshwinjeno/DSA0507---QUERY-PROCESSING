import pandas as pd

data = {
    "JOB_ID": ["AD_PRES","AD_VP","AD_ASST","FI_MGR"],
    "JOB_TITLE": ["President","Admin VP","Assistant","Finance Manager"]
}

df = pd.DataFrame(data)

sorted_jobs = df.sort_values(by="JOB_TITLE", ascending=False)
print(sorted_jobs)

