import pandas as pd
import plotly.express as px
iris0 = px.data.iris()
iris = pd.concat([iris0.loc[[9]],  iris0.iloc[31:38],
                 iris0.loc[[101]], iris0.iloc[142:143, :]])

iris.duplicated(keep='first', subset=None)
iris.duplicated(keep=False)  # 중복값 모두 
iris.duplicated(keep='last', subset=['petal_length', 'species'])

iris.drop_duplicates()

# 중복 행 갯수
iris.duplicated().sum()
# 중복 행 찾기 
iris[iris.duplicated(keep=False)]

iris.loc[[9,   34, 37]]
iris.loc[[101, 142]]

# list를 Series로 만들고..
a = pd.Series([1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5, 1, 1, 1, 2, 2, 3])
a.drop_duplicates()
# 0     1
# 3     2
# 5     3
# 6     4
# 10    5

# 원하는 값은
# 1 2 3 4 5 1 2 3  또는  
# 1 1 2 2 3 4 4 5 5 1 1 2 2 3
def rleid(seq):
    char = "sixx"
    group = 0
    result = []
    for i in range(0, len(seq)):
        if seq[i] == char:
            result.append(group)
        else:
            group = group + 1
            result.append(group)
            char = seq[i]
    return result

rleid(a)

seq = 'KACCCBBBBBAAAAFFFFFFFF'
seq= [1,1,1,2,3,3,1,2,2,2]
rleid(seq)

df = pd.DataFrame({
    'grp' : ["a","a","c","c","c","b","b","a","a"],
    'value' : range(1,10)
})
df['group_id'] = rleid(df['grp'])
df.groupby(['group_id']).sum()
# 	    grp	value	group_id
# 0	    a	1	    1
# 1	    a	2	    1
# 2	    c	3	    2
# 3	    c	4	    2
# 4	    c	5	    2
# 5	    b	6	    3
# 6	    b	7	    3
# 7	    a	8	    4
# 8	    a	9	    4


#   df['group_id'].duplicated()
# ~(df['group_id'].duplicated())
df[~(df['group_id'].duplicated())]
df[~(df['group_id'].duplicated(keep='first'))]
df[~(df['group_id'].duplicated(keep='last'))]

dfdup = df[~(df['group_id'].duplicated(keep='first')) | ~(df['group_id'].duplicated(keep='last'))]

import plotly.graph_objects as go

trace1 = go.Scatter(x=df.index, y=df.group_id, text=df.grp)
layout = go.Layout(title="Before")
fig = go.Figure(data=trace1, layout=layout)
fig.show()

trace2 = go.Scatter(x=dfdup.index, y=dfdup.group_id)
layout = go.Layout(title="After")
fig = go.Figure(data=trace2, layout=layout)
fig.show()


