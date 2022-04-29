from multiprocessing import Process, Queue
#from threading import Thread
import time

def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.put(total)
    #result.append(total)
    return


if __name__ == "__main__":
    now = time.time()
    START, END = 0, 1000000

    result = Queue()
    #result = list()

    th1 = Process(target=work, args=(1, START,  END//2, result))
    th2 = Process(target=work, args=(2, END//2, END,    result))
    # th1 = Thread(target=work, args=(1, START,  END//2, result))
    # th2 = Thread(target=work, args=(2, END//2, END,    result))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    result.put('STOP')

    print(f"Result: {time.time()-now}")
from multiprocessing import Pool 

def day_diff(i):
    temp = mt_rt[mt_rt['clientId']==mt_cid[i]]['date']  
    return (temp.values[-1] - temp.values[0]).days + 1

if __name__=='__main__':
    start_time = time.time()
    pool = Pool(processes=12)
    result = pool.map(day_diff, range(0, len(mt_cid)))
    print("- %s seconds -" % (time.time() - start_time))