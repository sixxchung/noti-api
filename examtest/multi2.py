from multiprocessing import Process, Queue


def cube(x, q):
    q.put(x * x * x)


def add(x, q):
    q.put(x + 1)


if __name__ == "__main__":
    q = Queue()
    proce = []
    for i in range(10):
        p = Process(target=cube, args=(i, q,))
        proce.append(p)
        p.start()

    for p in proce:
        p.join()

    proce = []
    print("INITIAL VALUES: ")
    while not q.empty():
        val = q.get()
        print(val)
        p = Process(target=add, args=(val, q,))
        proce.append(p)
        p.start()

    for p in proce:
        p.join()

    print("FINAL VALUES: ")
    while not q.empty():
        print(q.get())
