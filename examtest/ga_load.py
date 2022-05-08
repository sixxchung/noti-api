from memory_profiler import profile
import multiprocessing as mp

import sys
import os
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

basePath = '../app/'
# basePath = 'app/'
dataPath = basePath+'data/'
#dataPath = basePath+'data/mobi_data/mobi1/'

key_remain = ['mobiId', 'mobiTypCd', 'mobiTypNm', 'userId', 'userNm',  # 'interfaceDate',
              'created', 'ctrlServId', 'mobiRegiNum', 'battId', 'eventName',
              'eventCode', 'rentalState', 'rentalStateName']


def json2dict(dataFile):
    blist = []
    # dataFile = '../app/data/mobi.json.txt'
    # dataFile = '../app/data/mobility1_01_part1.json'
    with open(dataFile, "r") as multiline:
        for line in multiline:
            jdict = json.loads(line)
            jdata = {}
            jdata.update(
                {k: v for k, v in jdict.items() if k in key_remain})
            jdata.update(jdict['gps'])
            jdata.update(jdict['battery'])
            blist.append(jdata)  # dictionary append to list
        return blist


def json2list(json_list):
    alist = []

    for dataFile in json_list:
        # print(f"--------{dataFile}")
        blist = json2dict(dataFile)
        alist.extend(blist)          # list extend list
    return alist

# print(len(alist))


def main():
    file_list = os.listdir(dataPath)
    json_list = [file for file in file_list if file.startswith(
        "mobility1_01_part") & file.endswith(".json")]
    json_list.sort()
    json_list = [dataPath+json for json in json_list]

    alist = json2list(json_list)
    data = pd.DataFrame(alist)
    # data.memory_usage()

    pqFilePath = dataPath + 'mobility1.parquet'
    data.to_parquet(pqFilePath)
    print(pqFilePath)


if __name__ == "__main__":
    args = sys.argv
    _time_s = time.time()
    main()
    _time_e = time.time()
    print(_time_e-_time_s)

#-------------------------------
def test():
    _time_s = time.time()
    df = pd.read_parquet('../app/data/mobility1.parquet') #, engine='pyarrow')
    _time_e = time.time() 
    print(_time_e-_time_s)
    print(df.shape)
    print(df.size)
    print(df.memory_usage())
test()


