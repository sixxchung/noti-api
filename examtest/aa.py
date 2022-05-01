
import multiprocessing as mp

q = mp.Queue()
q.put(1)
print(q.queue)

q.put(2)
print(q.queue)

q.get()

q.qsize()

q.empty()

q.get_nowait()

q.close()