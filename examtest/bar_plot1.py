
import statsmodels.api as sm
import plotly.graph_objects as go
import plotly.express as px
df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color='sex',
                 facet_col="day", facet_row="time")

df = df.sort_values(by="total_bill")


model = sm.OLS(df["tip"], sm.add_constant(df["total_bill"])).fit()

# create the trace to be added to all facets
trace = go.Scatter(
    x=df["total_bill"],
    y=model.predict(),
    line_color="black",
    name="overall OLS")

# give it a legend group and hide it from the legend
trace.update(legendgroup="trendline", showlegend=False)

# add it to all rows/cols, but not to empty subplots
fig.add_trace(trace, row="all", col="all", exclude_empty_subplots=True)

# set only the last trace added to appear in the legend
# `selector=-1` introduced in plotly v4.13
fig.update_traces(selector=-1, showlegend=True)
fig.show()
