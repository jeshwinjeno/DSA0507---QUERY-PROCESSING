import pandas as pd
data = {
    "school_code": ["S1", "S1", "S2"],
    "student": ["A", "B", "C"]
}

df = pd.DataFrame(data)
grouped = df.groupby("school_code")

print(type(grouped))
