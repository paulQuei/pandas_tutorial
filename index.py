# index.py

import pandas as pd

index = pd.Index(['C','D','E','F','G','A','B'], name='note')

a = pd.Index([1,2,3,4,5])
b = pd.Index([3,4,5,6,7])

print("a|b = {}\n".format(a|b))
print("a&b = {}\n".format(a&b))
print("a.difference(b) = {}\n".format(a.difference(b)))