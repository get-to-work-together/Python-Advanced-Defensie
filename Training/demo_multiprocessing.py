# from multiprocessing import Process
#
#
# def f(name):
#     print('hello', name)
#
# if __name__ == '__main__':
#     processes = []
#     for i in range(5):
#         p = Process(target=f, args=(i,))
#         processes.append(p)
#         p.start()
#
#     for p in processes:
#         p.join()


import time
import multiprocessing
import threading
import os
import random


def myfunc(i):
    id = threading.get_ident()
    print(f'Main process {os.getpid()} thread {id} sleeping 5 sec from thread {i}')

    t_sleep = 0.5 + random.random()
    for n in range(random.randint(3, 8)):
        time.sleep(t_sleep)

    print(f"finished sleeping from thread {i}")


if __name__ == '__main__':

    id = threading.get_ident()
    print(f'Main process {os.getpid()} thread {id}')

    processes = []
    for i in range(10):
        p = multiprocessing.Process(target=myfunc, args=(i,))
        processes.append(p)
        p.start()

    print(f'Nr of active threads {threading.active_count()}')

    for p in processes:
        p.join()

    print('Main thread done')
