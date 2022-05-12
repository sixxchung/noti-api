import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import MinMaxScaler

from datetime import date
import time


# DataFrames example
iris = px.data.iris()
carshare = px.data.carshare()
stocks = px.data.stocks()
tips = px.data.tips()
wind = px.data.wind()
px.data.experiment()
gapminder = px.data.gapminder()

# Bar
temp = gapminder[['country', 'iso_alpha', 'iso_num']]
temp.drop_duplicates().shape[0] == temp.country.unique().shape[0]

gminder = gapminder[gapminder.columns.difference(['iso_alpha', 'iso_num'])]
ggminder = gminder.groupby(['continent', 'country', 'year'], as_index=False)
ggminder = ggminder.agg('mean')
#ggminder = ggminder.reset_index()

d2007 = ggminder[ggminder.year == 2007].copy()
d2007 = d2007.sort_values(by=['lifeExp'], ascending=False)
d2007['rank'] = list(range(1, len(d2007.country)+1))
df = pd.concat([d2007.loc[d2007['rank'].isin(range(1, 6))],
                d2007.loc[d2007['rank'].isin(range(138, 143))]])

trace1 = go.Bar(x=df.country, y=df.lifeExp,
                text=round(df.lifeExp, 0))
layout = go.Layout(title="Bar Chart")
fig = go.Figure([trace1], layout)
fig.show()

d2007.columns
scaler = MinMaxScaler()
scaler.fit(df[['lifeExp', 'pop']])
df[['zlifeExp', 'zpop']] = scaler.transform(df[['lifeExp', 'pop']])


trace1 = go.Bar(x=df['zlifeExp'], y=df['country'],
                text=round(df.lifeExp, 0), name='평균수명',
                orientation='h'
                )
trace2 = go.Bar(x=df['zpop'], y=df['country'],
                text=df['pop'], name='인구수',
                orientation='h'
                )
layout = go.Layout(title="Bar Chart",
                   # barmode='group',
                   yaxis=dict(autorange='reversed')
                   )
fig = go.Figure([trace1, trace2], layout)
fig.show()


fig = px.scatter(tips,
                 x="total_bill", y="tip",
                 color="smoker",
                 facet_col="sex", facet_row="time")
fig.show()


trace = go.Scatter(
    x=tips['total_bill'],
    y=tips['tip'],
    mode='markers',
    marker_color=tips['smoker'],
)
layout = go.Layout()
fig = go.Figure([trace], layout)
fig.show()

scaler = MinMaxScaler()
scaler.fit(d2007.pop)
iris_scaled = scaler.transform(irisDF)

# transform()시 스케일 변환된 데이터 세트가 Numpy ndarry로 반환돼 이를 DataFrame으로 변환
irisDF_scaled = pd.DataFrame(data=iris_scaled, columns=iris_set.feature_names)
print(irisDF_scaled.min())
print(irisDF_scaled.max())


smoker = ['No', 'Yes']
traces = []
for smoke in smoker:
    df = tips[tips.smoker == smoke]
    traces.append(
        go.Scatter(
            x=df.total_bill,
            y=df.tip,
            mode='markers',
            name=smoke
        )
    )
layout = go.Layout()
fig = go.Figure(traces, layout)
fig.show()


gminder = gapminder[gapminder.columns.difference(['iso_alpha', 'iso_num'])]
ggminder = gminder.groupby(['continent', 'country', 'year'])

ggminder.first()
ggminder.agg(lambda g: len(g))
ggminder.filter(lambda g: g.country == 'Algeria')
