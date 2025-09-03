import os
import threading
import random
import time



def task(nr):
    id = threading.get_ident()
    print(f'Task {nr} started with id={id} in process id={os.getpid()}')
    t = 0.5 * random.random()
    sum = 0
    for i in range(10000000):
        sum += i ** 3
        if i % 1000000 == 0:
            time.sleep(t)
            print(f'Task {nr} ... {i}')
    print(f'Task {nr} done')



def main():
    n = 5
    for nr in range(n):
        task(nr)


if __name__ == "__main__":
    s = time.perf_counter()

    main()

    elapsed = time.perf_counter() - s
    print(f"Executed in {elapsed:0.2f} seconds.")