# groupby.py

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['A','A','A','B','B','B','C','C','C'],
    'Data': np.random.randint(0, 100, 9)})
print('df=\n{}\n'.format(df))

groupby = df.groupby('Name')

print("Print GroupBy:")
for name, group in groupby:
    print("Name: {}\nGroup:\n{}\n".format(name, group))

print('Sum: \n{}\n'.format(groupby.sum()))
print('Agg Sum: \n{}\n'.format(groupby.agg(['sum'])))
print('Agg Map: \n{}\n'.format(
    groupby.agg([('Total', 'sum'), ('Min', 'min')])))

print('Describe: \n{}\n'.format(groupby.describe()))

def sort(df):
    return df.sort_values(by='Data', ascending=False)

print("Sort Group: \n{}\n".format(groupby.apply(sort)))