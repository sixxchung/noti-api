from multiprocessing import Pool
import multiprocessing
import time
import defs

multiprocessing.cpu_count()

if __name__ == '__main__':
    st = time.time()
    pool = multiprocessing.Pool(processes=100)
    pool.map(defs.func, 5, 1,2)
    print(time.time()-st)


ex = [1.2, 2.5, 3.7, 4.6]

result = [0] * len(ex)
for i in range(len(ex)):
    result[i] = int(ex[i])

ex = [1.2, 2.5, 3.7, 4.6]

result = list()
for i in range(len(ex)):
    result.append(int(ex[i]))
result