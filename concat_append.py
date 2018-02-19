# concat_append.py

import pandas as pd
import numpy as np

df1 = pd.DataFrame({'Note': ['C', 'D'],
                    'Weekday': ['Mon', 'Tue']},
                    index=[1, 2])

df2 = pd.DataFrame({'Note': ['E', 'F'],
                    'Weekday': ['Wed', 'Thu']},
                    index=[3, 4])

df3 = pd.DataFrame({'Note': ['G', 'A', 'B'],
                    'Weekday': ['Fri', 'Sat', 'Sun']},
                    index=[5, 6, 7])

df_concat = pd.concat([df1, df2, df3], keys=['df1', 'df2', 'df3'])
print("df_concat=\n{}\n".format(df_concat))

df_concat_column = pd.concat([df1, df2, df3], axis=1)
print("df_concat_column=\n{}\n".format(df_concat_column))

df_append = df1.append([df2, df3])
print("df_append=\n{}\n".format(df_append))