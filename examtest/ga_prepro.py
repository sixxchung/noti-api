#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np
import time
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px

# pd.option
# pd.set_option('display.max_row', 500)
# pd.set_option('display.max_columns', 500)
# pd.options.plotting.backend = "plotly"    # matplotlib
# pd.options.display.float_format = '{:.2f}'.format
# pd.options.display.float_format = '{:.5f}'.format

# DATA Folder ------------
# ~/git/noti-api/app/data
# /raid/templates/mobi_data

# iris = px.data.iris()
# carshare = px.data.carshare()
# stocks = px.data.stocks()
# tips = px.data.tips()


def read_ParquetData(srcPath):
    _time_s = time.time()
    df = pd.read_parquet(srcPath)
    _time_e = time.time()
    print(f'elapse time: {_time_e-_time_s}')
    print(df.info())
    return df


df_o = read_ParquetData('../app/data/mobility1.parquet')
df = df_o.copy()
df = df.sort_values(by=['Created'], ascending=True)
#df_s = df.sort_index(ascending=True)
# sum(df['Created']-df['created']) == 0
df.drop(['Created'], axis=1)
df = df.reset_index(drop=True)
# 167

# -------------------------------------------------------
#  칼럼별 결측값 개수 구하기
col_null = [col for col in df.columns if df[col].isnull().sum() > 0]
col_unique = [col for col in df.columns if df[col].nunique() < 2]
df[col_unique].drop_duplicates()
# 41
col_cate0 = [col for col in df.columns if df[col].nunique() < 20]
# 53
# df[col_cate0].drop_duplicates()
col_category = list(set(col_cate0)-set(col_unique))
# 12


cols = sorted(list(set(df.columns)-set(col_unique) -
              set(col_null)-set(col_cate0)))
# 114
df = df[cols]
# [
#  'Created',
#  'Cell01', 'Cell02', 'Cell03'~  'Cell64',
#  'Temp01', 'Temp02', 'Temp03', ~ 'Temp24',
#  'ModVol01', 'ModVol02', 'ModVol03', 'ModVol04', 'ModVol05', 'ModVol06',
#  'AvailCapa',  'AvgCellVol',  'AvgTemp',
#  'InvVol',
#  'Latitude', 'Longitude',
#  'MaxCellNo', 'MaxCellVol', 'MaxChgPwr', 'MaxDChgPwr', 'MaxTemp',
#  'MinCellNo', 'MinCellVol', 'MinTemp',
#  'PackCurr', 'PackSOC', 'PackVol', 'RealPwr']
# ----------time
{col: sorted(list(df[col].unique())) for col in col_category}
col_nn =['Created',
    'Cell01', 'MaxCellNo', 'MaxCellVol', 'MinCellNo', 'MinCellVol',
    'ModVol01',
    'Temp01', 'AvgTemp', 'MaxTemp', 'MinTemp',
    'PackCurr', 'PackSOC', 'PackVol', 'RealPwr',
    'AvgCellVol', 'InvVol',
    'AvailCapa', 'MaxChgPwr', 'MaxDChgPwr',
    'Latitude', 'Longitude']
dft = df[col_nn + col_category]

dft['Created'].diff(periods=1)
dft.dtypes
# datetime.fromtimestamp(dft['Created'][0]/1000)


dft['Created'].apply(lambda x: datetime.datetime.strptime(x, '%m/%d/%Y %I:%M:%S') if type(x) == str else np.NaN)
[ i for i in dft['Created']]
[pd.to_datetime(i, format='%Y%m%d%H%M%S%f').timestamp() for i in dft['Created']]


pd.to_datetime(1641 2 6 2 6 6 3546, format='%Y%m%d%H%M%S%f').timestamp()

dt_time = datetime(2022, 6, 13)
10000*dt_time.year + 100*dt_time.month + dt_time.day

df_time['iff_diff'] = df_time.iff_eph.diff()
df_time['iff_dt'] = pd.to_datetime(df_time.iff, format='%Y%m%d%H%M%S%f')

df_time['cr_eph'] = df_time.index.to_series()/1000
df_time['cr_diff'] = df_time.cr_eph.diff()
df_time['cr_dt'] = [(datetime.fromtimestamp(i)).strftime(format='%Y-%m-%d %H:%M:%S.%f')[:-3]
                    for i in df_time.cr_eph]
df_time['cr_dt'] = pd.to_datetime(df_time.cr_dt)

df_time = df_time.drop(['iff'], axis=1)
df_time.info()

# ----------------------------------------------------------------


key_gps = ['Latitude', 'Longitude']  # gpsDD.columns

key_cell = [f"Cell{i:02d}" for i in range(1, 65)]   # 64
key_temp = [f"Temp{i:02d}" for i in range(1, 25)]
key_modVol = [f"ModVol{i:02d}" for i in range(1, 9)]  # 8

key_wrn = [s for s in df_s.columns if "Wrn" in s]
key_fault = [s for s in df_s.columns if re.match("Flt", s)]
key_pack = [s for s in df_s.columns if re.match("Pack", s)] + ['InvVol']
key_bms = [s for s in df_s.columns if re.match("Bms", s)]
key_max = [s for s in df_s.columns if re.match("Max", s)]
key_min = [s for s in df_s.columns if re.match("Min", s)]

key_id = [
    'mobiId',
    'battId',
    'mobiTypCd', 'mobiTypNm',
    'userId', 'userNm',
    'ctrlServId', 'mobiRegiNum',
    'eventCode', 'eventName',
    'rentalState', 'rentalStateName'
]
key_others = ['RealPwr', 'AvailCapa', 'RlyStat', 'AvgCellVol', 'AvgTemp']

# df_cell = df_s.loc[:, df_s.columns.isin(key_cell)]
# df_temp = df_s.loc[:, df_s.columns.isin(key_temp)]
# df_modVol = df_s.loc[:, df_s.columns.isin(key_modVol)]

df_tmp = df_s.loc[:, ~df_s.columns.isin(
    key_cell+key_temp+key_modVol+key_gps+key_wrn+key_fault+key_pack+key_bms+key_max+key_min+key_id+key_id+key_others)]


# df_time['aa'] = df_time.cr_dt.diff()
# TypeError: unsupported operand type(s) for -: 'str' and 'str'

df_time['iff_dt'] = pd.to_datetime(df_time.iff, format='%Y%m%d%H%M%S%f')
df_time['cr_dt'] = [(datetime.fromtimestamp(i)).strftime(format='%Y-%m-%d %H:%M:%S.%f')[:-3]
                    for i in df_time.cr_eph]
df_time['cr_dt'] = pd.to_datetime(df_time.cr_dt)


df_time['aa'] = df_time.cr_dt.diff()
TypeError: unsupported operand type(s) for -: 'str' and 'str'

datetime.fromtimestamp(164126)
datetime(2022, 1, 4, 11, 17, 45, 810000).timestamp()
1641262665810
1641262663.546
df_time.head(3)

test = pd.Series([1641262663.546, 1641262667.546])

test.map(datetime.fromtimestamp)
test.apply(datetime.fromtimestamp)

df_time['aa'] = datetime.fromtimestamp(df_time['epochtime']/1000)


df_time['epochtime'].values


[type(i) for i in test]

type(test)


# df_s.index
# df_s['rank'] = list(range(1, df_s.shape[0]+1))
df_s.head()
df_s.loc[:, df_s.columns.difference(btyDD_key_cell)]
df_s.loc[:, ~df_s.columns.isin(btyDD_key_cell)]

df_cell_max = df_s.loc[:, btyDD_key_cell].fillna(0).max(axis=0)

trace1 = go.Bar(
    x=btyDD_key_cell,  # x축
    y=df_cell_max,  # y축 - 매출액
    # text=round(df_g1['Revenue'], 2),  # text 내용(소수점 2자리 반올림)
)
data = [trace1]  # data 객체에 리스트로 저장
layout = go.Layout(title=' Bar Chart',
                   width=1000, height=600)  # 제목 지정
fig = go.Figure(data, layout)
fig.show()


trace1 = go.Bar(
    x=df_s['Country'],  # x축 - 국가별
    y=df_g1['Revenue'],  # y축 - 매출액
    text=round(df_g1['Revenue'], 2),  # text 내용(소수점 2자리 반올림)
)

data = [trace1]  # data 객체에 리스트로 저장
layout = go.Layout(title='Chapter 2.1 - Bar Chart',
                   width=1000, height=600)  # 제목 지정
fig = go.Figure(data, layout)
fig.show()

# 참고) 입력방식 비교
# Data 객체 입력 방식1. add_trace( ) 함수 이용
fig = go.Figure()
fig.add_trace(go.Bar(x=df_g1['Country'],  # x축
                     y=df_g1['Revenue'],  # y축
                     text=df_g1['Revenue'],  # 값
                     ))
fig.update_layout(title='Chapter 2.1 - Bar Chart')
fig.show()

# Data 객체 입력 방식2. Figure( )에 직접적으로 data 객체를 정의
fig = go.Figure(data=[
    go.Bar(x=df_g1['Country'],  # x축
           y=df_g1['Revenue'],  # y축
           text=round(df_g1['Revenue'], 2),  # 값
           )
])
fig.update_layout(title='Chapter 2.1 - Bar Chart')
fig.show()

# Data 객체 입력 방식3. data 객체를 정의한 뒤 Figure( )에 입력
trace = go.Bar(x=df_g1['Country'],  # x축
               y=df_g1['Revenue'],  # y축
               text=round(df_g1['Revenue'], 2),  # 값
               )
data = [trace]  # data 객체에 리스트로 저장
layout = go.Layout(title='Chapter 2.1 - Bar Chart')  # 제목 지정
fig = go.Figure(data, layout)
fig.show()

# 참고) 그래프 중첩 입력방법 비교
# Data 객체 입력 방식1.
fig = go.Figure()
fig.add_trace(go.Bar(y=df_g1['Country'],  # y축
                     x=df_g1['Revenue'],  # x축
                     name='Revenues',
                     orientation='h'
                     ))
fig.add_trace(go.Bar(y=df_g1['Country'],  # y축
                     x=df_g1['Margin'],  # x축
                     name='Margins',
                     orientation='h'
                     ))
# Change the bar mode
fig.update_layout(title='Chapter 2.1 - Bar Chart',
                  barmode='group',
                  yaxis=dict(autorange='reversed'))
fig.show()

# Data 객체 입력 방식2.
fig = go.Figure(data=[
    go.Bar(y=df_g1['Country'],  # y축
           x=df_g1['Revenue'],  # x축
           name='Revenues',
           orientation='h'
           ),
    go.Bar(y=df_g1['Country'],  # y축
           x=df_g1['Margin'],  # x축
           name='Margins',
           orientation='h'
           )
])
# Change the bar mode
fig.update_layout(title='Chapter 2.1 - Bar Chart',
                  barmode='group',
                  yaxis=dict(autorange='reversed'))
fig.show()

# Data 객체 입력 방식3.
trace1 = go.Bar(y=df_g1['Country'],  # y축
                x=df_g1['Revenue'],  # x축
                name='Revenues',
                orientation='h'
                )
trace2 = go.Bar(y=df_g1['Country'],  # y축
                x=df_g1['Margin'],  # x축
                name='Margins',
                orientation='h'
                )
data = [trace1, trace2]
# Change the bar mode
layout = go.Layout()
layout = go.Layout(title='Chapter 2.1 - Bar Chart',
                   # barmode = 'group',
                   # yaxis = dict(autorange='reversed'),
                   #                    yaxis = {'autorange':'reversed'}
                   )
fig = go.Figure(data, layout)
fig.show()

trace = go.Bar(
    x=df_g1['Country'],  # x축 - 국가별
    y=df_g1['Revenue'],  # y축 - 매출액
    text=round(df_g1['Revenue'], 2),  # text 내용(소수점 2자리 반올림)
)
layout = go.Layout(
    title='Chapter 2.1 - Bar Chart',
    width=1000, height=600
)
fig = go.Figure(data=[trace], layout=layout)
fig.show()
