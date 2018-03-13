# plot.py

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/housing.csv")
data.hist(bins=50, figsize=(15, 12))
plt.show()