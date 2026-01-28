import pandas as pd
data = {
    "school_code": ["S1","S1","S2","S2"],
    "class": ["A","B","A","B"],
    "age": [12,14,13,15]
}

df = pd.DataFrame(data)
print(df.groupby(["school_code","class"]).mean())
