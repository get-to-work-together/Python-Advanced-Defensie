import time
import threading
import random
import logging

logging.basicConfig(level=logging.DEBUG)

lock = threading.Lock()

data = []


def task(i, lock):
    t = random.randint(3, 10)

    with lock:
        data.append(t)

    logging.info(f"Thread {i} - sleeping {t} sec")
    time.sleep(t)
    logging.info(f"Thread {i} - finished sleeping {t} sec")


threads = []
for i in range(10):
    thread = threading.Thread(target=task, args=(i, lock))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(data)