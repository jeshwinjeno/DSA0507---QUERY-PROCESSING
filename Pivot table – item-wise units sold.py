import pandas as pd
data = {
    "Item": ["TV","TV","Phone","Phone"],
    "Units": [10, 20, 5, 15]
}

df = pd.DataFrame(data)

pivot = df.pivot_table(values="Units", index="Item", aggfunc="sum")
print(pivot)
