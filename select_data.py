# select_data.py

import pandas as pd
import numpy as np

series1 = pd.Series([1, 2, 3, 4, 5, 6, 7],
    index=["C", "D", "E", "F", "G", "A", "B"])

print("series1['E'] = {} \n".format(series1['E']));
print("series1.E = {} \n".format(series1.E));

df1 = pd.DataFrame({"note" : ["C", "D", "E", "F", "G", "A", "B"],
    "weekday": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]},
    index=['1', '2', '3', '4', '5', '6', '7'])
print("df1.loc['2']:\n{}\n".format(df1.loc['2']))

print("series1.loc['E':'A']=\n{}\n".format(series1.loc['E':'A']));
print("df1.iloc[2:3]=\n{}\n".format(df1.iloc[2:4]))

print("series1.at['E']={}\n".format(series1.at['E']));
print("df1.iloc[4,1]={}\n".format(df1.iloc[4,1]))

index = pd.Index(['C','D','E','F','G','A','B'])