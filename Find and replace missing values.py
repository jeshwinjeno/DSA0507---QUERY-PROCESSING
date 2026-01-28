import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Marks': [80, np.nan, 75, np.nan]
})

df_filled = df.fillna(0)
print(df_filled)
