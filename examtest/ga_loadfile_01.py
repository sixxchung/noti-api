#!/usr/bin/env python
# coding: utf-8
import plotly.graph_objects as go
import plotly.express as px
from tarfile import PAX_FIELDS
import time

import pandas as pd
import numpy as np
#import chart_studio.plotly as py
#import cufflinks as cf
import json
from pandas import json_normalize

from datetime import datetime


import multiprocessing as mp
mp.cpu_count()  # 2
# pd.option
# pd.set_option('display.max_row', 500)
# pd.set_option('display.max_columns', 100)
# pd.options.plotting.backend = "plotly"    # matplotlib
# pd.options.display.float_format = '{:.2f}'.format
# pd.options.display.float_format = '{:.5f}'.format
pd.set_option('display.max_seq_items', None)

# DATA Folder ------------
# ~/git/noti-api/app/data
# /raid/templates/mobi_data
BasePath = '../app/data/'
for j in range(1, 7):
    # -------------------------------------------------------
    # j=1
    jdata = []  # list(dict, dict...)
    filePath = BasePath + f'mobi_data/mobi1/mobility1_0{j}.json'
    with open(filePath) as multiLines:
        for line in multiLines:
            jdata.append(json.loads(line))

    key_remain = list(jdata[0].keys())
    [key_remain.remove(i) for i in {'_id', 'gps', 'battery', '_class'}]

    # for test -----------
    # i = 6
    # jdict = jdata[i]
    # print(json.dumps(jdict, indent=4))

    # gpsDD = json_normalize(jdict['gps'])
    # batteryDD = json_normalize(jdict['battery'])

    data = pd.DataFrame()
    for i in range(0, len(jdata)):
        print(i, end=" ")  # i=0
        jdict0 = jdata[i]
        # print(json.dumps(dict0, indent = 4))
        gpsDD = json_normalize(jdict0['gps'])
        batteryDD = json_normalize(jdict0['battery'])

        result = {k: v for k, v in jdict0.items() if k in key_remain}
        resultDD = pd.DataFrame.from_dict(data=[result])

        if (int(gpsDD.Created) == int(batteryDD.Created)) & (int(batteryDD.Created) == int(resultDD.created)):
            pass
        else:
            print("불일치")

        data00 = pd.concat(
            [batteryDD.iloc[:, 1:], gpsDD.iloc[:, 1:], resultDD], axis=1)
        #data00.index = pd.Index(batteryDD.Created)
        data = pd.concat([data, data00])

    print(data)
    data.shape
    data.drop(['interfaceDate'])

    parquetPath = BasePath + f'mobility1_0{j}.parquet'
    data.to_parquet(parquetPath)
