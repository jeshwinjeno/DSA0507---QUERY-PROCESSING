import pandas as pd
df = pd.DataFrame({
    "Text": ["hello python", "data science"]
})

print(df["Text"].str.find("python"))
