from multiprocessing import cpu_count, Pool
import numpy as np
import pandas as pd
import defs
import time

precess = int(cpu_count() *0.5)

def main():
    start = int(time.time())
    pool = Pool(precess)
    result = pool.map(defs.mywork1, range(1, 12))

    #result = list(map(defs.mywork1, range(0,12)))
    print(f"result : {result} ")


if __name__ == '__main__':
    main()
