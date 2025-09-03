import threading
import asyncio
import os
import time
import random


async def task(nr):
    id = threading.get_ident()
    print(f'Task {nr} started with id={id} in process id={os.getpid()}')
    t = 0.5 * random.random()
    sum = 0
    for i in range(10000000):
        sum += i ** 3
        if i % 1000000 == 0:
            await asyncio.sleep(1)
            print(f'Task {nr} ... {i}')
    print(f'Task {nr} done')


async def main():
    n = 5
    await asyncio.gather(*(task(nr) for nr in range(n)))

    print('All coroutines finished.')



if __name__ == '__main__':
    print(f'Main thread: id={threading.get_ident()} in process id={os.getpid()}')
    s = time.perf_counter()

    asyncio.run(main())

    elapsed = time.perf_counter() - s
    print(f"Executed in {elapsed:0.2f} seconds.")
