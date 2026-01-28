import pandas as pd

data = {
    "DEPARTMENT_ID": [10,20,30,40,50,60,70,80,90,100,110,120],
    "DEPARTMENT_NAME": ["Admin","Marketing","Purchase","HR","Shipping",
                        "IT","PR","Sales","Executive","Finance","Accounting","Treasury"]
}

df = pd.DataFrame(data)

distinct_departments = df["DEPARTMENT_ID"].unique()
print(distinct_departments)

