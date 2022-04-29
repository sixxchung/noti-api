import time
from multiprocessing import Pool
import multiprocessing
from functools import partial
from contextlib import contextmanager
# 필요없는 낭비 없애기 위해 pool terminate도 필요


@contextmanager
def poolcontext(*args, **kwargs):
    pool = multiprocessing.Pool(*args, **kwargs)
    yield pool
    pool.terminate()





if __name__ == '__main__':
    arg1 = ['1', '2', '3']
    arg2 = ['A', 'B', 'C']

    # processes는 cpu 코어 개수
    with poolcontext(processes=16) as pool:
        result = pool.starmap(printname, zip(arg1, arg2))

    print(result)

with open('example.txt', 'r') as f:
    for line in f:
        pass


def f(x):
    print(x*x)


if __name__ == '__main__':
    pool = Pool(processes=1)
    pool.map(f, range(10))
    r = pool.map_async(f, range(10))
    print('First print')
    print('Second print')
    r.wait()
    print ('Third print')
