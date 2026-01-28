import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4))
df.iloc[2, 1] = np.nan
df.iloc[5, 3] = np.nan

styled_df = df.style.highlight_null(color='yellow')
styled_df
