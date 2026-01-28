import pandas as pd
df = pd.DataFrame({
    "Country": ["India","USA"],
    "Beer": [10, 15],
    "Wine": [5, 20]
})

print("Shape:", df.shape)
print("Columns:", df.columns)
