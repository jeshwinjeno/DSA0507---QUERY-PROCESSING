import pandas as pd
data = {
    "school_code": ["S1","S1","S2","S2"],
    "age": [12,14,13,15]
}

df = pd.DataFrame(data)
result = df.groupby("school_code")["age"].agg(["mean","min","max"])
print(result)
