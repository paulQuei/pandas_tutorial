# merge_join.py

import pandas as pd
import numpy as np

df1 = pd.DataFrame({'key': ['K1', 'K2', 'K3', 'K4'],
                    'A': ['A1', 'A2', 'A3', 'A8'],
                    'B': ['B1', 'B2', 'B3', 'B8']})

df2 = pd.DataFrame({'key': ['K3', 'K4', 'K5', 'K6'],
                    'A': ['A3', 'A4', 'A5', 'A6'],
                    'B': ['B3', 'B4', 'B5', 'B6']})

print("df1=\n{}\n".format(df1))
print("df2=\n{}\n".format(df2))

merge_df = pd.merge(df1, df2)
merge_inner = pd.merge(df1, df2, how='inner', on=['key'])
merge_left = pd.merge(df1, df2, how='left')
merge_left_on_key = pd.merge(df1, df2, how='left', on=['key'])
merge_right_on_key = pd.merge(df1, df2, how='right', on=['key'])
merge_outer = pd.merge(df1, df2, how='outer', on=['key'])

print("merge_df=\n{}\n".format(merge_df))
print("merge_inner=\n{}\n".format(merge_inner))
print("merge_left=\n{}\n".format(merge_left))
print("merge_left_on_key=\n{}\n".format(merge_left_on_key))
print("merge_right_on_key=\n{}\n".format(merge_right_on_key))
print("merge_outer=\n{}\n".format(merge_outer))

df3 = pd.DataFrame({'key': ['K1', 'K2', 'K3', 'K4'],
                    'A': ['A1', 'A2', 'A3', 'A8'],
                    'B': ['B1', 'B2', 'B3', 'B8']},
                    index=[0, 1, 2, 3])

df4 = pd.DataFrame({'key': ['K3', 'K4', 'K5', 'K6'],
                    'C': ['A3', 'A4', 'A5', 'A6'],
                    'D': ['B3', 'B4', 'B5', 'B6']},
                    index=[1, 2, 3, 4])

print("df3=\n{}\n".format(df3))
print("df4=\n{}\n".format(df4))

join_df = df3.join(df4, lsuffix='_self', rsuffix='_other')
join_left = df3.join(df4, how='left', lsuffix='_self', rsuffix='_other')
join_right = df1.join(df4, how='outer', lsuffix='_self', rsuffix='_other')

print("join_df=\n{}\n".format(join_df))
print("join_left=\n{}\n".format(join_left))
print("join_right=\n{}\n".format(join_right))
