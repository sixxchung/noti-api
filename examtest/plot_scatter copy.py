import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
#from sklearn.preprocessing import MinMaxScaler

tips = px.data.tips()
df = tips.sort_values(by="total_bill")


#-----------
fig = px.scatter(df, x="total_bill", y="tip")
fig.show()

#-----------
trace1 = go.Scatter(
    x=df['total_bill'], y=df['tip'],
    mode='lines+markers',
    marker=dict(size=5, color='red'),
    line=dict(color='blue')
)
layout = go.Layout(title= "Scatter,line plot")
fig = go.Figure([trace1], layout)
fig.show()

### 성별,요일별 총액에 따른 팁 
df_g = df.loc[:, ['total_bill','tip', 'sex','day']].groupby(by=['sex','day'], as_index=False).sum()
custom_order = dict(Thur=0, Fri=1, Sat=2, Sun=3)
df_g.sort_values(['day'], key=lambda x:x.map(custom_order))

sex = list( df_g['sex'].unique())
sex.sort()

traces=[]
for gender in sex:
    tmp = df_g[df_g['sex']==gender]
    traces.append(
        go.Scatter(x=tmp['day'], y=tmp['tip'],
            mode='lines+markers',
            name = gender,
            
        )
    )
layout = go.Layout(title='Scatter Line plots',
                   category_orders=custom_order
)
fig =  go.Figure(traces, layout)
fig.show()

### 성별,요일별 총액에 따른 팁
df_g = df.loc[:, ['total_bill', 'tip', 'sex', 'day']].groupby(
    by=['sex', 'total_bill'], as_index=False).sum()
#custom_order = dict(Thur=0, Fri=1, Sat=2, Sun=3)
df_g.sort_values(['day'], key=lambda x: x.map(custom_order))

sex = list(df_g['sex'].unique())
sex.sort()

traces = []
for gender in sex:
    tmp = df_g[df_g['sex'] == gender]
    traces.append(
        go.Scatter(x=tmp['total_bill'], y=tmp['tip'],
                   mode='lines+markers',
                   name=gender,

                   )
    )
layout = go.Layout(title='Scatter Line plots',
                   #category_orders=custom_order
                   )
fig = go.Figure(traces, layout)
fig.show()
