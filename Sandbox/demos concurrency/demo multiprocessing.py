import time
from multiprocessing import Process

data = []


def doe_iets(i):
    print(f'{i} - Doing it ...')
    data.append(i)
    time.sleep(1)
    data.append(i)
    print(f'{i} - Done')


if __name__ == '__main__':

    processes = []
    for i in range(5):
        p = Process(target=doe_iets, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(data)