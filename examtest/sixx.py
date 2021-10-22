#!/usr/bin/env python
# -*- coding: utf-8 -*-
### Required libraries ------------------------------------------
def initial():
    import numpy as np
    import os
    import pandas as pd
    from pandas import Series

# column 다 보이기
pd.set_option('display.max_columns', None)
#(참고) warning 제거를 위한 코드
#np.seterr(divide='ignore', invalid='ignore')

### Visualization libraries -------------------------------------
import seaborn as sns
color = sns.color_palette()
sns.set_style('darkgrid')

import matplotlib.pyplot as plt
# % matplotlib inline
get_ipython().run_line_magic('matplotlib', 'inline')

plt.rcParams["figure.figsize"] = (7,6)  # 크기 (inch)
plt.rcParams['axes.grid'] = True        # 격자선 여부
plt.rcParams['lines.linewidth'] = 2     # 선의 두께
plt.rcParams['lines.color'] = 'red'     # 선의 색깔

### Etc. libraries ---------------------------------------------- 
from datetime import datetime    # To access datetime 
# To print multiple output in a cell --------------------------
from IPython.display import clear_output, Image, display, HTML
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

### *************************************************************
import sklearn

# sample data load
from sklearn.datasets import load_iris 
iris = load_iris() 
irisdf = pd.DataFrame(data=iris.data, columns=iris.feature_names)