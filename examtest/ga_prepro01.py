#!/usr/bin/env python
# coding: utf-8
import re
import plotly.graph_objects as go
import plotly.express as px
from tarfile import PAX_FIELDS
import time

import pandas as pd
import numpy as np
# import chart_studio.plotly as py
# import cufflinks as cf
import json
from pandas import json_normalize

from datetime import datetime

# pd.option
# pd.set_option('display.max_row', 500)
# pd.set_option('display.max_columns', 100)
# pd.options.plotting.backend = "plotly"    # matplotlib
# pd.options.display.float_format = '{:.2f}'.format
# pd.options.display.float_format = '{:.5f}'.format

# DATA Folder ------------
# ~/git/noti-api/app/data
# /raid/templates/mobi_data
BasePath = '../app/data/'
# -------------------------------------------------------
parquetPath = BasePath + 'mobility1.parquet'
df = pd.read_parquet(parquetPath)
df_s = df.sort_index(ascending=True)
# df_s = df.sort_values(by=['created'], ascending=False)

# df_time = df_tmp.copy()
df_time = df_s.loc[:, ['interfaceDate']]
df_time.columns = ['iff']
df_time['iff_eph'] = [pd.to_datetime(
    i, format='%Y%m%d%H%M%S%f').timestamp() for i in df_time.iff]
df_time['iff_diff'] = df_time.iff_eph.diff()
df_time['iff_dt'] = pd.to_datetime(df_time.iff, format='%Y%m%d%H%M%S%f')

df_time['cr_eph'] = df_time.index.to_series()/1000
df_time['cr_diff'] = df_time.cr_eph.diff()
df_time['cr_dt'] = [(datetime.fromtimestamp(i)).strftime(format='%Y-%m-%d %H:%M:%S.%f')[:-3]
                    for i in df_time.cr_eph]
df_time['cr_dt'] = pd.to_datetime(df_time.cr_dt)

df_time = df_time.drop(['iff'], axis=1)
df_time.info()

#----------------------------------------------------------------
df_s.drop(['interfaceDate', 'created'], axis=1)

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
from datetime import datetime

df_time['aa']= datetime.fromtimestamp(df_time['epochtime']/1000)





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




import pandas as pd


a = [1,2,3,4,5,6,7,8]
b = [1,2,4,8,16,32,64,128]
c = [8,7,6,5,4,3,2,1]
data = {"col1":a,"col2":b,"col3":c}
df = pd.DataFrame(data)
print(df)
print(df.diff(axis=0))

print(df.loc[[a]].diff(axis=0))

df.loc[:,['col1']].diff()