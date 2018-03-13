# .py

import pandas as pd
import numpy as np

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})


print("\n{}\n".format(df))

print("\n{}\n".format(df.groupby('A').sum()))

print("\n{}\n".format(df.groupby(['A', 'B']).sum()))