import pandas as pd
import numpy as np

# Create dataframe with random values
df = pd.DataFrame(np.random.randn(10, 4))

# Function to color values
def highlight(val):
    if val < 0:
        return 'color: red'
    else:
        return 'color: black'

# Use map() instead of applymap()
styled_df = df.style.map(highlight)

styled_df
