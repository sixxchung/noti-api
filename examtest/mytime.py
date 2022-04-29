import seaborn as sns
import numpy as np
import pandas as pd
import time
from datetime import datetime
import pytz

# epoch to DateTime
epochtime = 30256871
datetime.fromtimestamp(epochtime)
# datetime.datetime(1970, 12, 17, 13, 41, 11)

# DateTime to epoch
datetime(2022, 4, 27, 14, 42, 21).timestamp()
# 1651038141.0
tz = pytz.timezone('Asia/Seoul')
tz.localize(datetime(1970, 1, 1, 0, 0))
# atetime.datetime(1970, 1, 1, 0, 0, tzinfo= < DstTzInfo 'Asia/Seoul' KST+9: 00: 00 STD > )

tz = pytz.timezone('UTC')
datetime(1970, 1, 1, 0, 0).timestamp()
tz.localize(datetime(1970, 1, 1, 0, 0)).timestamp()
# 0

# epoch to datetime string
seconds = 800025
datetime.fromtimestamp(seconds)
# datetime.datetime(1970, 1, 10, 15, 13, 45)
(datetime.fromtimestamp(800025)).strftime('%Y-%m-%d %H:%M:%S')
# '1970-01-10 15:13:45'

millseconds = 1.224325    # DateTime milliseconds
datetime.fromtimestamp(millseconds)
# datetime.datetime(1970, 1, 1, 9, 0, 1, 224325)

# epoch to DateTime timezone

# Universal Time Coordinated (UTC) = 예전에는 그리니치 mean time (GMT)
# Central Time (CT)
# - Central Standard Time (CST) 6        => UTC-6
# - Central Daylight saving Time (CDT)   => UTC-5
tz = pytz.timezone('CST6CDT')
datetz = tz.localize(datetime(2020, 11, 17, 1, 37, 50), is_dst=None)
print(datetz)

pytz.all_timezones
tz = pytz.timezone('Asia/Seoul')
tz.localize(datetime(1970, 1, 1, 0, 0, 1), is_dst=None)   # 지역시간생성
# datetime.datetime(1970, 1, 1, 0, 0, 1, tzinfo=<DstTzInfo 'Asia/Seoul' KST+9:00:00 STD>)

datetime(1970, 1, 1, 0, 0, 1).timestamp()

datetime.fromtimestamp(int("258741369")).strftime('%Y-%m-%d %H:%M:%S')

# https://ponyozzang.tistory.com/291

# https://steadiness-193.tistory.com/42
titanic_o = sns.load_dataset("titanic")
titanic = titanic_o.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
# titanic['class'].unique()
# ['Third', 'First', 'Second']
df = titanic.head(20)
df_filtered = df.loc[:, ['age', 'fare']]
gp = df.groupby('class')
gp_filtered = df.loc[:, ['age', 'fare', 'class']].groupby('class')

def uf_ex(x):
    return x-1

# 컬럼명이 메서드밖  ==> apply와 transform의 결과는 동일
df.age.apply(uf_ex)
df.age.transform(uf_ex)  

gp.age.apply(uf_ex)
gp.age.transform(uf_ex) 

# 컬럼명이 메서드안  ==> apply 가능
df.apply(lambda x: print(x))              # X에러
df.transform(lambda x: uf_ex(x['age']))   # X에러

gp.apply(lambda x: uf_ex(x['age']))          
gp.transform(lambda x: uf_ex(x['age']))   # 에러  

df_filtered.apply(lambda x: uf_ex(x['age']))        # X에러
df_filtered.transform(lambda x: uf_ex(x['age']))    # X에러

gp_filtered.apply(lambda x: uf_ex(x['age']))
gp_filtered.transform(lambda x: uf_ex(x['age']))    # X에러

# 컬럼명이 명시안함  ==>   transform은 골라서 사용..
df.apply(uf_ex)               # X에러
df.transform(uf_ex)           # X에러

gp.apply(uf_ex)               # X에러
gp.transform(uf_ex)

df_filtered.apply(uf_ex)
df_filtered.transform(uf_ex)

gp_filtered.apply(uf_ex)
gp_filtered.transform(uf_ex)


datetime(1970, 1, 1, 0, 0) - datetime(1970, 1, 1, 0, 0)


datetime.


grouped.first()  # 각 그룹의 첫번째 행
grouped.get_group('Second')  # 해당 그룹의 데이터 확인
grouped.size()               # 각 그룹별 행 갯수

# aggregation
grouped.agg(np.mean)
grouped.mean()            # same above
grouped.agg({'age': np.mean})
grouped.agg({'age': np.mean, 'fare': np.sum})

df.agg({'age': np.mean})
grouped.apply(lambda x: (x.fare * x.survived).sum())


def uf_total_series(x):
    return x.fare * x.survived


def uf_total_keepidx(x):
    return pd.DataFrame({'total': x.fare * x.survived})


grouped.apply(uf_total_series)
