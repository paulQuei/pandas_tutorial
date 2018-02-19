# data_structure.py

import pandas as pd
import numpy as np

series1 = pd.Series([1, 2, 3, 4])
print("series1:\n{}\n".format(series1))

print("series1.values: {}\n".format(series1.values))

print("series1.index: {}\n".format(series1.index))

series2 = pd.Series([1, 2, 3, 4, 5, 6, 7],
    index=["C", "D", "E", "F", "G", "A", "B"])
print("series2:\n{}\n".format(series2))
print("E is {}\n".format(series2["E"]))

df1 = pd.DataFrame(np.arange(16).reshape(4,4))
print("df1:\n{}\n".format(df1))

df2 = pd.DataFrame(np.arange(16).reshape(4,4),
    columns=["column1", "column2", "column3", "column4"],
    index=["a", "b", "c", "d"])
print("df2:\n{}\n".format(df2))

df3 = pd.DataFrame({"note" : ["C", "D", "E", "F", "G", "A", "B"],
    "weekday": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]})
print("df3:\n{}\n".format(df3))

noteSeries = pd.Series(["C", "D", "E", "F", "G", "A", "B"],
    index=[1, 2, 3, 4, 5, 6, 7])
weekdaySeries = pd.Series(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    index=[1, 2, 3, 4, 5, 6, 7])
df4 = pd.DataFrame([noteSeries, weekdaySeries])
print("df4:\n{}\n".format(df4))

df3["No."] = pd.Series([1, 2, 3, 4, 5, 6, 7])
print("df3:\n{}\n".format(df3))

del df3["weekday"]
print("df3:\n{}\n".format(df3))

print("df3.columns\n{}\n".format(df3.columns))
print("df3.index\n{}\n".format(df3.index))

print("Note C, D is:\n{}\n".format(df3.loc[[0, 1], "note"]))
print("Note C, D is:\n{}\n".format(df3.iloc[[0, 1], 0]))