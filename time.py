# time.py

import datetime as dt
import numpy as np
import pandas as pd

now = dt.datetime.now();
print('Now is {}'.format(now))

yesterday = now - dt.timedelta(1);
print('Yesterday is {}\n'.format(yesterday.strftime('%Y-%m-%d')))

this_year = pd.date_range(dt.datetime(2018, 1, 1),
        dt.datetime(2018, 12, 31), freq='5D')
print('Selected days in 2018: \n{}\n'.format(this_year))

df = pd.DataFrame(np.random.randint(0, 100, this_year.size), index=this_year)
print('Jan: \n{}\n'.format(df['2018-01']))

eight_weeks = pd.Period('2018-01-15', freq='W', periods=8)
print('Start time:{}\nEnd time:{}'.format(
    eight_weeks.start_time, eight_weeks.end_time))

add_5h = eight_weeks + dt.timedelta(days=5)
print('Add 5h end time:{}'.format(add_5h.end_time))
