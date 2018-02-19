# process_na.py

import pandas as pd
import numpy as np

dates = pd.date_range('1/1/2000', periods=8)
print("dates:\n{}\n".format(dates))

df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print("df:\n{}\n".format(df))

panel = pd.Panel({'one' : df, 'two' : df - df.mean()})
print("panel:\n{}\n".format(panel))

s = df['A']
print("s:\n{}\n".format(s))