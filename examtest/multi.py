

import pytz
import time
from datetime import datetime

epochtime = 1642314376



datetimeobj1=datetime.fromtimestamp(epochtime)
# datetime to timestamp
timestamp1 = 
timestamp2 = time.mktime(datetimeobj2.timetuple())
datetime(2016, 8, 19).timestamp()




# epoch to DateTime timezone

tz = pytz.timezone('UTC')
tz.localize(datetime.datetime(1970, 1, 1, 0, 0)).timestamp()
# 0

datetime.datetime(1970, 1, 1, 0, 0).timestamp()
# -32400.0

import pandas as pd
import numpy as np
df = pd.DataFrame([
    [ 1,  2,  3,  4,  5],
    [ 6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
], index = ['ridx1', 'ridx2', 'ridx3', 'ridx4'],
   columns=['colNm1', 'colNm2', 'colNm3', 'colNm4', 'colNm5'])

df['행 합'] = df.sum(axis=1)
df.loc['열 합']= df.sum(axis=0)

df.append(df,ignore_index=True)

df.apply(np.cumsum, axis=0)
a = map(np.cumsum, df)

a = [1,2,3,4,5,6,7]
print(map(np.cumsum, a))
