import time


def sync_task_1():
    print('sync_task_1 시작')
    print('sync_task_1 3초 대기')
    time.sleep(3)
    print('sync_task_1 종료')


def sync_task_2():
    print('sync_task_2 시작')
    print('sync_task_2 2초 대기')
    time.sleep(2)
    print('sync_task_2 종료')


start = time.time()
sync_task_1()
sync_task_2()
end = time.time()
print(end-start)

# sync_task_1 시작
# sync_task_1 3초 대기
# sync_task_1 종료
# sync_task_2 시작
# sync_task_2 2초 대기
# sync_task_2 종료
# 5.00602912902832
