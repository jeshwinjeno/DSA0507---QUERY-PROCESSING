import pandas as pd

data = {
    "EMPLOYEE_ID": [102,101,101,201,114,122,200,176,176,200],
    "JOB_ID": ["IT_PROG","AC_ACCOUNT","AC_MGR","MK_REP","ST_CLERK",
               "ST_CLERK","AD_ASST","SA_REP","SA_MAN","AC_ACCOUNT"]
}

df = pd.DataFrame(data)

result = df.groupby("EMPLOYEE_ID").filter(lambda x: len(x) >= 2)
print(result["EMPLOYEE_ID"].unique())
