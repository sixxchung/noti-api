import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
#from sklearn.preprocessing import MinMaxScaler

url = 'https://raw.githubusercontent.com/sixxchung/pythondash/6236fbca647de6562c5685de724a08362bd1afea/data/Sales%20data/Data.csv'
df_o = pd.read_csv(url)
df = df_o.copy()
df['year']=df['OrderDate'].str.slice(0,4)
df['month']=df['OrderDate'].str.slice(5,7)
df = df.sort_values(by=['Region', 'Channel', 'Category', 'Item Type', 'year', 'month', 'Gender'])
df['Margin'] = df['Revenue'] - df['Cost']
df.info()

df20 = df[ df['year']=='2020' ]
df_g0 = df20.loc[:, ['Region','Channel','Category','Revenue']]
df_g = df_g0.sort_values(by=['Region', 'Channel', 'Category'])

value1 = df_g.groupby(by=['Region', 'Channel'], as_index=False).sum()
value2 = df_g.groupby(by=['Channel', 'Category'], as_index=False).sum()
# label(이동시키고 싶은) source(시작위치), target(끝위치), value(이동량)

trace = go.Sankey(
    node = dict( label=['Africa', 'Offline', 'Online'], x=[0,1,1], y=[0, 0.1, 0.7]),
    link = dict(
        source = [0,0], 
        target = [1,2],
        value=[100, 200]
    )
)
layout = go.Layout(title="ch2.2", yaxis=dict(title='Revenue'))
fig = go.Figure(data=trace, layout=layout)
fig.show()


trace = go.Sankey(
    node=dict(
        label=["A1", "A2", "B1", "B2", "C1", "C2"],
        # pad=15,
        # thickness=20,
        # line=dict(color="black", width=0.5),
        # color="blue"
    ),
    link=dict(
        # indices correspond to labels, eg A1, A2, A1, B1, ...
        source=[0, 1, 
                0, 2, 
                3, 3],
        target=[2, 3, 
                3, 4, 
                4, 5],

        value=[8, 4, 2, 8, 4, 2]
    ))
fig = go.Figure(trace)
fig.show()

fig.update_layout(title_text="Basic Sankey Diagram", font_size=15)

trace = go.Sankey(
    node = dict(
        label=["남자", "여자", 
              "미성년자", "20대", "30대", "40대", "50대", "60대", "70대", "80세이상"],
        color=["blue", "red", "green", "green",
                "green", "green", "green", "green", "green", "green"],
        pad=5,
        thickness=30,
        line=dict(color="black", width=0.5)
    ),
    link = dict(
        #line=list(color="black", width=0.2),
        source=[0, 0, 0, 0, 0, 0, 0, 0, 
                1, 1, 1, 1, 1, 1, 1, 1],
        target=[2, 3, 4, 5, 6, 7, 8, 9, 
                2, 3, 4, 5, 6, 7, 8, 9],
        value=[27623, 542781, 637042, 545819, 543074, 366564, 172025, 71392,
                30531, 477163, 355695, 318402, 431370, 503340, 498872, 326901]
    )
)