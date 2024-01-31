import random
import time
from threading import Thread


def myfunc(i):
    t = random.randint(2, 6)
    print(f'sleeping {t} sec from thread {i}')
    time.sleep(t)
    print(f'finished sleeping from thread {i}')


for i in range(10):
    t = Thread(target=myfunc, args=(i,))
    t.start()
