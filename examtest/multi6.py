from multiprocessing import cpu_count, Pool
import numpy as np
import pandas as pd
import defs
import time

def main():
    pool = Pool(4)
    result = pool.map(defs.mywork1, range(1,12))

    #result = list(map(defs.mywork1, range(0,12)))
    print(f"result : {result} ")

if __name__ == '__main__':
    main()


    # Pool.map
    # Pool 객체 초기화
    p = Pool(processes=1)
    # Pool.map
    result = p.map(defs.mywork1, range(10))
    print(f"Pool.map : {result} ")

    # Pool_map_async
    result_async = p.map_async(defs.mywork1, range(10))
    result = result_async.get()
    print(f"Pool.map_async : {result} ")

    # Pool.apply_async
    results_async = [p.apply_async(defs.mywork1, [i]) for i in range(10)]
    results = [r.get() for r in results_async]
    print(results)
