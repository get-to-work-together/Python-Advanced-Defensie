import os
import time
import threading
import random


def task(nr):
    id = threading.get_ident()
    print(f'Task {nr} started with id={id} in process id={os.getpid()}')
    t = 0.5 * random.random()
    sum = 0
    for i in range(10_000_000):
        sum += i ** 3
        if i % 1000000 == 0:
            time.sleep(t)
            print(f'Task {nr} ... {i}')
    print(f'Task {nr} done')


def main():
    n = 5
    threads = []
    for nr in range(n):
        t = threading.Thread(target=task, args=(nr,))
        threads.append(t)
        t.start()

    for nr, t in enumerate(threads):
        print(f'Waiting for thread {nr} to end')
        t.join()

    print('All threads finished.')


if __name__ == "__main__":
    print(f'Main thread: id={threading.get_ident()} in process id={os.getpid()}')
    t0 = time.perf_counter()

    main()

    elapsed = time.perf_counter() - t0
    print(f"Executed in {elapsed:0.2f} seconds.")
