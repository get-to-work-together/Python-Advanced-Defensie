import os
import pathlib
import time
import threading

print(f'Current working directory: {os.getcwd()}')

directory = '../Sandbox'
glob = '**/*.*'
keyword = 'asyncio'

print(f'Searching in directory {pathlib.Path(directory).resolve()}')

filenames = [str(filename.resolve()) for filename in pathlib.Path(directory).glob(glob)]

all_filenames_with_keyword = []

def find_in_file(filename, keyword):
    try:
        if os.path.isfile(filename):
            with open(filename) as f:
                for line in f:
                    if keyword in line:
                        return True
            return False
    except UnicodeDecodeError: # Probably not a text file
        return False
    return False # Not a file

def find_in_files(filenames, keyword):
    for filename in filenames:
        if find_in_file(filename, keyword):
            all_filenames_with_keyword.append(filename)

def task(filename, keyword):
    if find_in_file(filename, keyword):
        all_filenames_with_keyword.append(filename)

def find_in_files_with_threads(filenames, keyword):
    threads = []
    for filename in filenames:
        thread = threading.Thread(target=task, args=(filename, keyword))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':

    print()
    print('Sequential -----------------------------------------')

    all_filenames_with_keyword = []

    t0 = time.time()
    find_in_files(filenames, keyword)
    t1 = time.time()

    for filename in all_filenames_with_keyword:
        print(filename)

    print(f'Execution time {t1 - t0} s.')

    print()
    print('With threading -----------------------------------------')

    all_filenames_with_keyword = []

    t0 = time.time()
    find_in_files_with_threads(filenames, keyword)
    t1 = time.time()

    for filename in all_filenames_with_keyword:
        print(filename)

    print(f'Execution time {t1 - t0} s.')
