# process_na.py

import pandas as pd
import numpy as np

df = pd.DataFrame([[1.0, np.nan, 3.0, 4.0],
                  [5.0, np.nan, np.nan, 8.0],
                  [9.0, np.nan, np.nan, 12.0],
                  [13.0, np.nan, 15.0, 16.0]])

print("df:\n{}\n".format(df));
print("df:\n{}\n".format(pd.isna(df)));

print("df.dropna():\n{}\n".format(df.dropna()));
print("df.dropna(axis=1, how='all'):\n{}\n".format(df.dropna(axis=1, how='all')));

print("df.fillna(1):\n{}\n".format(df.fillna(1)));

df.rename(index={0: 'index1', 1: 'index2', 2: 'index3', 3: 'index4'},
          columns={0: 'col1', 1: 'col2', 2: 'col3', 3: 'col4'},
          inplace=True);
df.fillna(value={'col2': 2}, inplace=True)
df.fillna(value={'col3': 7}, inplace=True)
print("df:\n{}\n".format(df));
