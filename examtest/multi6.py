
import sklearn
from multiprocessing import cpu_count, Pool
import numpy as np
import pandas as pd
import defs

import time


if __name__ == '__main__':
    pool = Pool(processes=1)
    pool.map(defs.mywork1, range(10))

    pool.map_async(defs.mywork1, range(10))
    print('First print')
    print('Second print')
    r.wait()
    print('Third print')
