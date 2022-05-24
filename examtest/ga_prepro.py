#!/usr/bin/env python
# coding: utf-8
import re
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
# pd.set_option('display.float_format', lambda x: '%.f'%x)

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
print(col_null)

col_unique = [col for col in df.columns if df[col].nunique() < 2]
df[col_unique].drop_duplicates()
# 41

col_cate0 = [col for col in df.columns if df[col].nunique() < 20]
# 53
# df[col_cate0].drop_duplicates()
col_category = list(set(col_cate0)-set(col_unique))
# 12
col_gps = ['Latitude', 'Longitude']  # gpsDD.columns

col_numeric0 = sorted(list(
    set(df.columns) - set(col_unique) - set(col_null)- set(col_cate0) -set(col_gps))
)
# 114

col_cell = [f"Cell{i:02d}" for i in range(1, 65)]     # 64
col_temper = [f"Temp{i:02d}" for i in range(1, 25)]   # 24
col_modVol = [f"ModVol{i:02d}" for i in range(1, 9)]  #  8
col_wrn   = [s for s in df.columns if "Wrn" in s]     # 12

col_fault= [s for s in df.columns if re.match("Flt", s)] # 21
col_pack = [s for s in df.columns if re.match("Pack", s)] + ['InvVol'] # 5
col_bms  = [s for s in df.columns if re.match("Bms", s)] #   2
col_max  = [s for s in df.columns if re.match("Max", s)] #   6
col_min  = [s for s in df.columns if re.match("Min", s)] #   4

col_numeric = sorted(list(
    set(col_numeric0) - set(col_cell)- set(col_temper) - set(col_modVol) -
    set(col_wrn) - set(col_fault) - set(col_pack) - set(col_bms) - 
    set(col_max) - set(col_min))
)  # 6

{col: sorted(list(df[col].unique())) for col in col_category}

# for observe
col_nn =['Created',
    'Cell01', 'MaxCellNo', 'MaxCellVol', 'MinCellNo', 'MinCellVol',
    'ModVol01',
    'Temp01', 'AvgTemp', 'MaxTemp', 'MinTemp',
    'PackCurr', 'PackSOC', 'PackVol', 'RealPwr',
    'AvgCellVol', 'InvVol',
    'AvailCapa', 'MaxChgPwr', 'MaxDChgPwr',
    'Latitude', 'Longitude']
dft0 = df[col_nn + col_category]
dft = dft0.copy()
dft['created_diff'] = dft['Created'].diff(periods=1)
# datetime.fromtimestamp(dft['Created'][0]/1000)

dft.loc[:, ['Created_dt']] = [datetime.fromtimestamp(created/1000) for created in dft['Created'] ]
dft['Cdate'] = dft['Created_dt']





#dft.set_index(df['Created_dt'], inplace=True)

#dft['Created_dt'].dt.year
dft['Created_dt'].dt.to_period(freq='S')  # A M D T S

dft['created_dt_diff'] = dft['Created_dt'].diff(periods=1)
#dft.dtypes
df_f= dft[dft.columns[dft.columns.str.endswith('_diff')]]
#------------------------------------------------------

dfg = dft[(df['created'] > 1641696000000) & (df['created'] < 1641700000000)]
dfg[col_pack]
#dfg = dft[(df_f['created_diff'] < 995) | (df_f['created_diff'] > 1005)]
trace = go.Scatter( x=dfg['Created'],  y=dfg['InvVol'] , 
        mode='markers+lines', 
        marker=dict(size=3, color='red'),
        line=dict(width=0.1, color='grey')) #, text=dfg['created_dt_diff'])
layout = go.Layout(title="AAA")
fig = go.Figure(data=trace, layout=layout)
fig.show()


# ----------------------------------------------------------------
cols = ['Created_dt'] + col_pack 
df0 = dft[cols]