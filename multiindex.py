# multiindex.py

import pandas as pd
import numpy as np

multiIndex = pd.MultiIndex.from_arrays([
    ['Geagle', 'Geagle', 'Geagle', 'Geagle',
     'Epple', 'Epple', 'Epple', 'Epple', 'Macrosoft',
     'Macrosoft', 'Macrosoft', 'Macrosoft', ],
    ['S1', 'S2', 'S3', 'S4', 'S1', 'S2', 'S3', 'S4', 'S1', 'S2', 'S3', 'S4']],
    names=('Company', 'Turnover'))

print("multiIndex = \n{}\n".format(multiIndex));

df = pd.DataFrame(data=np.random.randint(0, 1000, 36).reshape(-1, 12),
                  index=[2016, 2017, 2018],
                  columns=multiIndex)
print("df = \n{}\n".format(df))


print("{}".format(df.loc[2017, 'Geagle']))