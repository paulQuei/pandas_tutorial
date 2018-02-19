# file_operation.py

import pandas as pd
import numpy as np

df1 = pd.read_excel("data/test.xlsx")
print("df1:\n{}\n".format(df1))

df2 = pd.read_csv("data/test1.csv")
print("df2:\n{}\n".format(df2))

df3 = pd.read_csv("data/test2.csv", sep="|")
print("df3:\n{}\n".format(df3))