from datetime import date
import numpy as np
import plotly.express as px
iris = px.data.iris()
carshare = px.data.carshare()
stocks = px.data.stocks()
tips = px.data.tips()
wind = px.data.wind()
px.data.experiment()
gapminder = px.data.gapminder()


## Bar


temp = gapminder[['country', 'iso_alpha', 'iso_num']]
temp.drop_duplicates().shape[0] == temp.country.unique().shape[0]
gminder= gapminder[gapminder.columns.difference(['iso_alpha', 'iso_num'])]
ggminder = gminder.groupby(['continent', 'country', 'year'])
ggminder = gminder.groupby(['continent', 'country', 'year'], as_index=False)
ggminder = ggminder.agg('mean')
#ggminder = ggminder.reset_index()

d20 = ggminder[ggminder.year==2002].copy()
d20 = d20.sort_values(by=['lifeExp'], ascending=False)
d20['rank'] = list(range(1, len(d20.country)+1))


trace1 = go.Bar(x=d20.country, y=d20.lifeExp,
            text=round(d20.lifeExp,0) )
layout = go.Layout(title="Bar Chart")
fig = go.Figure([trace1], layout)
fig.show()

trace1 = go.Bar(x=d20.country, y=d20.lifeExp,
            text=round(d20.lifeExp,0) )
trace2 = go.
layout = go.Layout(title="Bar Chart")
fig = go.Figure([trace1], layout)
fig.show()



fig = px.scatter(tips, 
    x="total_bill", y="tip", 
    color="smoker", 
    facet_col="sex", facet_row="time")
fig.show()

import plotly.graph_objects as go

trace = go.Scatter(
    x=tips['total_bill'],
    y=tips['tip'],
    mode = 'markers',
    marker_color=tips['smoker'],
)
layout = go.Layout()
fig = go.Figure([trace], layout)
fig.show()


smoker = ['No', 'Yes']
traces = []
for smoke in smoker:
    df = tips[tips.smoker==smoke]
    traces.append( 
        go.Scatter(
            x=df.total_bill,
            y=df.tip,
            mode='markers',
            name = smoke
        )
    )
layout = go.Layout()
fig = go.Figure(traces, layout)
fig.show()


gminder= gapminder[gapminder.columns.difference(['iso_alpha', 'iso_num'])]
ggminder = gminder.groupby(['continent', 'country', 'year'])

ggminder.first()
ggminder.agg(lambda g:len(g))
ggminder.filter(lambda g: g.country=='Algeria')



