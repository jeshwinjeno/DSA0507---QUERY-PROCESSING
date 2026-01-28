import pandas as pd
data = {
    "Region": ["East","East","West"],
    "Manager": ["Martha","Martha","Timothy"],
    "SalesMan": ["Alex","Alex","Stephen"],
    "Sale_amt": [30000, 40000, 50000]
}

df = pd.DataFrame(data)

pivot = pd.pivot_table(
    df,
    values="Sale_amt",
    index=["Region","Manager","SalesMan"],
    aggfunc="sum"
)

print(pivot)
