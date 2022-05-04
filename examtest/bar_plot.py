from datetime import date
import plotly.express as px
iris = px.data.iris()
carshare = px.data.carshare()
stocks = px.data.stocks()
tips = px.data.tips()

fig = px.scatter(tips, 
    x="total_bill", y="tip", 
    color="smoker")
fig = px.scatter(tips, 
    x="total_bill", y="tip", 
    color="smoker", 
    facet_col="sex", facet_row="time")
fig.show()

import plotly.graph_objects as go
import numpy as np

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