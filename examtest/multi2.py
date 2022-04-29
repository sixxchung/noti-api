from multiprocessing import Pool
import multiprocessing
#from functools import partial

# 필요없는 낭비 없애기 위해 pool terminate도 필요
from defs import poolcontext, printname

if __name__ == '__main__':
    arg1 = ['1', '2', '3']
    arg2 = ['A', 'B', 'C'] 

    # processes는 cpu 코어 개수
    with poolcontext(processes=16) as p:
        result = p.starmap(printname, [(arg1, arg2)])
        #result = p.starmap(printname, zip(arg1, arg2))
    print(result)


def mywork(x, x2):
    print(f'x:{x2} ')
    return x*x2


if __name__ == '__main__':
    with Pool(5) as p:
        #p.map(mywork, [(1, 2, 3), 2])
        p.map(mywork, [(1, 2), (3, 4)])


ex = [1.2, 2.5, 3.7, 4.6]
with Pool(5) as p:
    result = p.map(int, range(0, 4))
print(result)


def parallel_dataframe(df, func, num_cores):
    df_split = np.array_split(df, num_cores)
    pool = Pool(num_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df
