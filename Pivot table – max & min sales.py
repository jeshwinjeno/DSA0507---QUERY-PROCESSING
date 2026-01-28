import pandas as pd

data = {
    "Item": ["TV","TV","Phone","Phone"],
    "Sale_amt": [50000, 70000, 20000, 30000]
}

df = pd.DataFrame(data)

pivot = df.pivot_table(values="Sale_amt", index="Item",
                       aggfunc=["max","min"])
print(pivot)
