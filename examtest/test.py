import pandas as pd
import plotly.express as px
iris0 = px.data.iris()
iris = pd.concat( [iris0.iloc[31:38], iris0.iloc[142:143,:]])



# unique 행들
iris_distict = iris.drop_duplicates()

iris.duplicated()
iris.duplicated(subset=['sepal_length'])
# 중복 행 갯수
iris.duplicated().sum()
# 중복 행 찾기 
iris[iris.duplicated()]

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
import numpy as np
# 원하는 값은
# 1 2 3 4 5 1 2 3  또는  1 1 2 2 3 4 4 5 5 1 1 2 2 3
df = pd.DataFrame.from_dict(
        {'measurement_id': np.repeat([1, 2], [6, 6]),
         'min': np.concatenate([np.repeat([1, 2, 3], [2, 2, 2]), 
                                np.repeat([1, 2, 3], [2, 2, 2])]),
         'obj': list('AB' * 6),
         'var': [1, 2, 2, 2, 1, 1, 2, 1, 2, 1, 1, 1]})
df['rleid_output'] = [1, 1, 2, 1, 3, 2, 4, 3, 4, 3, 5, 3]
df['expected_output'] = [1, 2, 1, 2, 1, 1, 2, 3, 2, 3, 1, 3]


#-----

df['grouper'] = (df.groupby(['measurement_id', 'obj', 'var'])['min']
                 .apply(lambda x: x.diff().fillna(1).eq(1))
                 )

df['expected_output'] = (
    df.groupby(['measurement_id', 'obj', 'var'])[
        'grouper'].transform('sum').astype(int)
)

df = df.drop(columns='grouper')

#     measurement_id  min obj  var  expected_output
# 0                1    1   A    1                1
# 1                1    1   B    2                2
# 2                1    2   A    2                1
# 3                1    2   B    2                2
# 4                1    3   A    1                1
# 5                1    3   B    1                1
# 6                2    1   A    2                2
# 7                2    1   B    1                3
# 8                2    2   A    2                2
# 9                2    2   B    1                3
# 10               2    3   A    1                1
# 11               2    3   B    1                3
