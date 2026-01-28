import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(-10, 10, (10, 4)),
                  columns=list('ABCD'))

def highlight(val):
    return 'color: red' if val < 0 else 'color: black'

styled_df = df.style.map(highlight)
styled_df
