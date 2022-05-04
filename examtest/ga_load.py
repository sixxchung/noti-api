import ijson
from memory_profiler import profile

import sys
import time
import string
import math
from datetime import datetime

import json
import pandas as pd
import numpy as np

# pd.set_option('display.max_row', 500)
# pd.set_option('display.max_columns', 100)
# pd.set_option('display.max_seq_items', None)

# pd.options.plotting.backend = "plotly"    # matplotlib
# pd.options.display.float_format = '{:.2f}'.format
# pd.options.display.float_format = '{:.5f}'.format

import plotly.graph_objects as go
import plotly.express as px

import multiprocessing as mp


import json

BasePath = '../app/data/'
filePath = BasePath + f'/mobi.json.txt'

with open (filePath) as f:


superH=json.load(*f)



    dictjson = json.load(f)








filePath = '../app/data/' + f'/large-file.json'
with open(filePath, "r") as f:
    data = json.load(f)

user_to_repos = {}
for record in data:
    #record = data[0]
    user = record["actor"]["login"]
    repo = record["repo"]["name"]
    if user not in user_to_repos:
        user_to_repos[user] = set()
    user_to_repos[user].add(repo)



jdatas = []
j = 1
i = 0
filePath = BasePath + f'mobi_data/mobi1/mobility1_0{j}.json'
filePath = BasePath + f'mobi.json.txt'
with open(filePath) as file_obj:
    f =list(file_obj)

pd.read_json(f)

    for line in file_obj:
        print('------')
        print(line.rstrip('\n'))
        jdata = json.load(line.rstrip('\n'))
        type(jdata)

    ijson_generator = ijson.items(file_obj)
    key2_value = next(ijson_generator)
    print(key2_value)

    
    filedata = list(multiLines)
    jdata = [json.loads(filedata[i].rstrip('\n'))
             for i in range(len(filedata))]

for line in ijson.items(jdata, "item"):
    print(line)
    i = i +1
    print(i)
    jdatas.append(json.loads(line) )



with open(filePath, 'r') as f:
    filedata = list(f)
jdata = [json.loads(filedata[i].rstrip('\n')) for i in range(len(filedata))]



user_to_repos = {}
with open(filePath, "r") as f:
    for record in ijson.items(f, "item"):
        user = record["actor"]["login"]
        repo = record["repo"]["name"]
        if user not in user_to_repos:
            user_to_repos[user] = set()
        user_to_repos[user].add(repo)

user_to_repos = {}
with open(filePath, "r") as f:
    for record in ijson.items(f, "item"):
        print(type(record))


def divideList(someList, n):
    return [someList[i: i+n] for i in range(0, len(someList), n)]


BasePath = '../app/data/'
jdatas = []

j = 1
#filePath = BasePath + f'mobi_data/mobi1/mobility1_0{j}.json'
#grp = int(mp.cpu_count()*.50)  # num_cores = num_process

filePath = BasePath + f'/mobi.json.txt'
grp = 3

# with open(filePath) as multiLines:
#     for line in multiLines:
#         jdatas.append(json.loads(line))

#jdatas = jdatas[:100]
filePath = BasePath + f'/mobi.json.txt'
with open(filePath, 'r') as f:
    filedata = list(f)
jdata = [json.loads(filedata[i].rstrip('\n')) for i in range(len(filedata))]
# with open(filePath) as multiLines:
#     for line in multiLines:
#         jdatas.append(json.loads(line))
user_to_repos = {}
with open(filePath, "r") as f:
    for 

    for record in ijson.items(list(f), "item"):
        record 


        user = record["actor"]["login"]
        repo = record["repo"]["name"]
        if user not in user_to_repos:
            user_to_repos[user] = set()
        user_to_repos[user].add(repo)




print(jdata)

n = math.ceil(len(jdatas) / grp)
jdata_divided = [jdatas[i*n: (i+1)*n] for i in range((len(jdatas)+n-1)//n)]
#[['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j']]

key_remain = ['mobiId', 'mobiTypCd', 'mobiTypNm', 'userId', 'userNm',  # 'interfaceDate',
              'created', 'ctrlServId', 'mobiRegiNum', 'battId', 'eventName',
              'eventCode', 'rentalState', 'rentalStateName']


@profile
def dict2df(jdata, q=None):
    data = pd.DataFrame()

    for i in range(0, len(jdata)):
        #i=1
        jdict0 = jdata[i]
        gpsDD = pd.json_normalize(jdict0['gps'])
        batteryDD = pd.json_normalize(jdict0['battery'])
        remainDD = {k: v for k, v in jdict0.items() if k in key_remain}
        remainDD = pd.DataFrame.from_dict(data=[remainDD])
        data00 = pd.concat(
            [batteryDD.iloc[:, 1:], gpsDD.iloc[:, 1:], remainDD], axis=1
        )
        gpsDD.clear()
        batteryDD.clear()
        remainDD.clear()        

        data = pd.concat([data, data00])
    if q == None :
        return data
    else:
        q.put(data)
    # return(data)


@profile
def main(args):
    # if args[1].lower == 'single':
    #     print('------Single------')
    #     _timeStart = time.time()  # ---
    #     result = dict2df(jdatas)
    #     _timeEnd = time.time()  # ---
    #     return result, _timeEnd - _timeStart
    # else:   
        print('------Multi------') 
        tasks = []
        q = mp.Queue()

        for i in range(grp):
            # i=0
            p = mp.Process(target=dict2df, args=(jdata_divided[i], q))
            tasks.append(p)
            p.start()

        for task in tasks:
            task.join()

        result = pd.DataFrame()
        while not q.empty(): 
            q_data = q.get()
            result = pd.concat([result, q_data])
        return result 


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

    