import pandas as pd
df = pd.DataFrame({"Name": ["Python", "DaTa"]})
df["Swapped"] = df["Name"].str.swapcase()
print(df)
