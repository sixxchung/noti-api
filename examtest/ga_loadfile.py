#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import time
from datetime import datetime

import plotly.graph_objects as go
import plotly.express as px
#import chart_studio.plotly as py
#import cufflinks as cf

import json
from pandas import json_normalize
# from tarfile import PAX_FIELDS

import math
#from defs import poolcontext, mywork

# from multiprocessing.dummy import Process
# import multiprocessing as mp
# mp.cpu_count()  # 2

# # pd.option
# # pd.set_option('display.max_row', 500)
# # pd.set_option('display.max_columns', 100)
# # pd.options.plotting.backend = "plotly"    # matplotlib
# # pd.options.display.float_format = '{:.2f}'.format
# # pd.options.display.float_format = '{:.5f}'.format
# pd.set_option('display.max_seq_items', None)


# # for test -----------
# # i = 6
# # jdict = jdata[i]
# # print(json.dumps(jdict, indent=4))

# # gpsDD = json_normalize(jdict['gps'])
# # batteryDD = json_normalize(jdict['battery'])

# data = pd.DataFrame()


# def mywork(i):
#     print(i, end=" ")  # i=0
#     jdict0 = jdata[i]
#     # print(json.dumps(dict0, indent = 4))
#     gpsDD = json_normalize(jdict0['gps'])
#     batteryDD = json_normalize(jdict0['battery'])

#     result = {k: v for k, v in jdict0.items() if k in key_remain}
#     resultDD = pd.DataFrame.from_dict(data=[result])

#     if (int(gpsDD.Created) == int(batteryDD.Created)) & (int(batteryDD.Created) == int(resultDD.created)):
#         pass
#     else:
#         print("불일치")

#     data00 = pd.concat(
#         [batteryDD.iloc[:, 1:], gpsDD.iloc[:, 1:], resultDD], axis=1)
#     #data00.index = pd.Index(batteryDD.Created)
#     data = pd.concat([data, data00])


import defs


def divideList(someList, n):
    return [someList[i: i+n] for i in range(0, len(someList), n)]


# DATA Folder ------------
# ~/git/noti-api/app/data, # /raid/templates/mobi_data
BasePath = '../app/data/'
# for j in range(1, 7):
j = 1
# -------------------------------------------------------
jdata = []
#filePath = BasePath + f'mobi_data/mobi1/mobility1_0{j}.json'
filePath = BasePath + f'mobi-ex1-single_quote.json'
with open(filePath) as multiLines:
    data =  multiLines.readlines()
data


with open(filePath) as multiLines:
    for line in multiLines:
        jdata.append(json.loads(line))





# key_remain = list(jdata[0].keys())
# [key_remain.remove(i) for i in {'_id', 'gps', 'battery', '_class'}]
# key_remain = ['mobiId', 'mobiTypCd', 'mobiTypNm', 'userId', 'userNm',  # 'interfaceDate',
#               'created', 'ctrlServId', 'mobiRegiNum', 'battId', 'eventName',
#               'eventCode', 'rentalState', 'rentalStateName']


def main(args):
    if args[1].lower == 'single':
        _timeStart = time.time()  # ---
        result = mywork(jdata)
        _timeEnd = time.time()  # ---
        return result, _timeEnd - _timeStart
    elif args[1].lower == 'multi':
        aProcess = int(mp.cpu_count()*0.25)  # 에러처리필요.
        d = math.ceil(len(jdata)/aProcess)
        jdata_d = list(defs.divideList(jdata, d))
        # aProcess == len(jdata_d)
        # [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j']]

        queue = mp.Queue()
        tasks = []

        for i in range(len(jdata_d)):
            # i=0
            thrd = mp.Process(mywork, args=(jdata_d[i],queue))
            tasks.append(thrd)
            thrd.start()
        for task in tasks:
            task.join()

        queue.put("END")
        result = pd.DataFrame()
        while True:
            mid = queue.get()
            if mid == "END":
                return result
            result.append(mid)




        data = pd.DataFrame()
        with mp.Pool(aProcess) as p:
            p.map(mywork, jdata_d)

        print(data)
        data.shape
        # data.drop(['interfaceDate'])

        parquetPath = BasePath + f'mobility1_0{j}.parquet'
        data.to_parquet(parquetPath)
