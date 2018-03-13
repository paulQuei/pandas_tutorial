# plot.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randint(0, 100, 4*12).reshape(-1, 4),
                  columns=['A', 'B', 'C', 'D']);
df.plot.bar()
plt.show()
