from multiprocessing import Process, Queue
import sys
import time

def work1(num):
    summation = 0
    for i in range(1, num+1):
        summation += i
    return summation

def work2(id, queue, start, end):
    mid = 0
    for i in range(start+1, end+1):
        mid += i
    queue.put(mid)
    return

def main(args):
    if args[1].lower() == "single":
        result = work1(int(args[2]))
        return result

    elif args[1].lower() == "multi":
        queue = Queue()
        tasks = []
        num = int(args[2])

        result = work1(int(args[2]))
        return result

        for i in range(8):
            thrd = Process(target=work2, args=(
                i, queue, (num*i)//8, (num*(i+1))//8))
            # 100000 =>  0~12500, 12500 ~ 25000, ...
            tasks.append(thrd)
            thrd.start()

        for task in tasks:
            task.join()

        queue.put("END")  # To imprint the end sign at last cell
        result = 0

        # Join the results computed by the threads
        while True:
            mid = queue.get()
            if mid == "END":
                _TIME2 = time.time()
                return result, _TIME2 - _TIME1
            result += mid


if __name__ == '__main__':
    args = sys.argv
    result, ex_time = main(args)
    print(f"SUM of 0 ~ {args[2]} : {result} in {ex_time:.5f} sec")
