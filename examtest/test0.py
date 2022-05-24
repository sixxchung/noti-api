import plotly.express as px
import plotly.graph_objects as go
import numpy as np

df = px.data.tips()

ref_line_slope = 0.15  # 15% tip for reference
ref_line_x_range = np.array([df.total_bill.min(), df.total_bill.max()])

fig = px.scatter(df, x="total_bill", y="tip", facet_col="day", trendline='ols')

fig = fig.add_trace(go.Scatter(...), 
        row='all', col='all', exclude_empty_subplots=True)

fig = fig.add_trace(go.Scatter(x=reference_line_x_range,
                    y=ref_line_slope*reference_line_x_range, name='15%'))
fig.show()


