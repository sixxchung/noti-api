
from matplotlib import markers
from matplotlib.pyplot import title
import statsmodels.api as sm
import plotly.graph_objects as go
import plotly.express as px
df = px.data.tips()
df = df.sort_values(by="total_bill")

fig = px.scatter(df, 
    x="total_bill", y="tip", 
#   color='sex',
#   facet_col="day",
#   facet_row="time"
)
fig.show()



model = sm.OLS(df["tip"], sm.add_constant(df["total_bill"])).fit()

#create the trace to be added to all facets
trace1 = go.Scatter(
    x=df.total_bill,
    y=df.tip,
    mode= 'markers'
)
trace2 = go.Scatter(
    x=df["total_bill"],
    y=model.predict(),
    line_color="black",
    name="overall OLS")

# give it a legend group and hide it from the legend
trace2.update(legendgroup="trendline", showlegend=False)

layout = go.Layout(
    title="Tips",
    xaxis=dict(title="total bill"),
    yaxis=dict(title='tip')
)

fig = go.Figure(data=[trace1, trace2], layout=layout)

# add it to all rows/cols, but not to empty subplots
fig.add_trace(trace2, row="all", col="all", exclude_empty_subplots=True)
# set only the last trace added to appear in the legend
# `selector=-1` introduced in plotly v4.13
fig.update_traces(selector=-1, showlegend=True)

fig.show()
