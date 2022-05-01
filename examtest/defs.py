# 반복문을 실행할 함수

import multiprocessing
import pandas as pd

from functools import partial
from contextlib import contextmanager

from multiprocessing import Pool
import time
import os


def mywork1(x):
    print(f'value {x} is in PID {os.getpid()}')
    time.sleep(1)
    return x


def mywork2(arg1, arg2):
    print(arg1, arg2)


@contextmanager
def poolcontext(*args, **kwargs):
    pool = Pool(*args, **kwargs)
    yield pool
    pool.terminate()


def mywork(i, jdata):

    print(i, end=" ")  # i=0
    jdict0 = jdata[i]

    # key_remain = list(jdict0[0].keys())
    # [key_remain.remove(i) for i in {'_id', 'gps', 'battery', '_class'}]

    key_remain = ['mobiId', 'mobiTypCd', 'mobiTypNm', 'userId', 'userNm',  # 'interfaceDate',
                  'created', 'ctrlServId', 'mobiRegiNum', 'battId', 'eventName',
                  'eventCode', 'rentalState', 'rentalStateName']

    # print(json.dumps(dict0, indent = 4))
    gpsDD = pd.json_normalize(jdict0['gps'])
    batteryDD = pd.json_normalize(jdict0['battery'])

    result = {k: v for k, v in jdict0.items() if k in key_remain}
    resultDD = pd.DataFrame.from_dict(data=[result])

    if (int(gpsDD.Created) == int(batteryDD.Created)) & (int(batteryDD.Created) == int(resultDD.created)):
        pass
    else:
        print("불일치")

    data00 = pd.concat(
        [batteryDD.iloc[:, 1:], gpsDD.iloc[:, 1:], resultDD], axis=1
    )
    #data00.index = pd.Index(batteryDD.Created)
    data = pd.concat([data, data00])
