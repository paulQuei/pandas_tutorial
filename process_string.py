# process_string.py

import pandas as pd

s1 = pd.Series([' 1', '2 ', ' 3 ', '4', '5']);
print("s1.str.rstrip():\n{}\n".format(s1.str.lstrip()))
print("s1.str.strip():\n{}\n".format(s1.str.strip()))
print("s1.str.isdigit():\n{}\n".format(s1.str.isdigit()))

s2 = pd.Series(['Stairway to Heaven', 'Eruption', 'Freebird',
                    'Comfortably Numb', 'All Along the Watchtower'])
print("s2.str.lower():\n{}\n".format(s2.str.lower()))
print("s2.str.upper():\n{}\n".format(s2.str.upper()))
print("s2.str.len():\n{}\n".format(s2.str.len()))
