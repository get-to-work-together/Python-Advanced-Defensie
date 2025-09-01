from threading import Thread
import time

data = []

def doe_iets(i):
    print(f'{i} - Doing it ...')
    data.append(i)
    time.sleep(1)
    data.append(i)
    print(f'{i} - Done')


threads = []
for i in range(5):
    thread = Thread(target=doe_iets, args=(i,))
    threads.append( thread )
    thread.start()

for thread in threads:
    thread.join()

print(data)