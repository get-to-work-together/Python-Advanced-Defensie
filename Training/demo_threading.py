import time
import threading
import random
import os
import logging

logging.basicConfig(level=logging.INFO)


def myfunc(i):
    id = threading.get_ident()
    # print(f'Main process {os.getpid()} thread {id} sleeping from thread {i}')
    logging.info(f'Main process {os.getpid()} thread {id} sleeping from thread {i}')

    t_sleep = 0.5   # + random.random()
    for n in range(random.randint(3, 8)):
        time.sleep(t_sleep)

    # print(f"finished sleeping from thread {i}")
    logging.info(f"finished sleeping from thread {i}")


id = threading.get_ident()
print(f'Main process {os.getpid()} thread {id}')

threads = []
for i in range(10):
    t = threading.Thread(target=myfunc, args=(i,))
    threads.append(t)
    t.start()

print(f'Nr of active threads {threading.active_count()}')

for t in threads:
    t.join()

print('Main thread done')
