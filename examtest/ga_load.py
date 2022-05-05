from memory_profiler import profile
import multiprocessing as mp

import sys
import time
import string
import math
import re
from datetime import datetime

import json
import ijson
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# pd.set_option('display.max_row', 500)
# pd.set_option('display.max_columns', 100)
# pd.set_option('display.max_seq_items', None)

# pd.options.plotting.backend = "plotly"    # matplotlib
# pd.options.display.float_format = '{:.2f}'.format
# pd.options.display.float_format = '{:.5f}'.format

BasePath = '../app/data/'
filePath = BasePath + f'mobi_data/mobi1/mobility1_01.json'
key_remain = ['mobiId', 'mobiTypCd', 'mobiTypNm', 'userId', 'userNm',  # 'interfaceDate',
              'created', 'ctrlServId', 'mobiRegiNum', 'battId', 'eventName',
              'eventCode', 'rentalState', 'rentalStateName']

alist = []
with open(filePath, "r") as multiline:
    for line in multiline:
        jdict = json.loads(line)        
        jdata = {}
        jdata.update({k: v for k, v in jdict.items() if k in key_remain})
        jdata.update(jdict['gps'])
        jdata.update(jdict['battery']) 
        alist.append(jdata)

print(len(alist))
data = pd.DataFrame(alist)
# data.memory_usage()
j=1
parquetPath = BasePath + f'mobility1_0{j}.parquet'
data.to_parquet(parquetPath)

if __name__ == "__main__":
    args = sys.argv
    _time_s = time.time()
    result = main(args)
    _time_e = time.time()

    print(_time_e-_time_s)
    print(result)
    result.shape

    parquetPath = BasePath + f'mobility1_0{j}.parquet'
    result.to_parquet(parquetPath)

    