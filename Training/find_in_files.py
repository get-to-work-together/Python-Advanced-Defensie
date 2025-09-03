import os
import pathlib
import time

print(os.getcwd())

def find_in_files(filenames, keyword):
    filenames_with_keyword = []
    for filename in filenames:
        with open(filename) as f:
            for line in f:
                if keyword in line:
                    filenames_with_keyword.append(filename)
                    break
    return filenames_with_keyword


directory = '/'
glob = '**/*.py'
keyword = 'class'

print(f'Searching in directory {pathlib.Path(directory).resolve()}')

filenames = [str(filename.resolve()) for filename in pathlib.Path(directory).glob(glob)]
# print(filenames)

t0 = time.time()
for filename in find_in_files(filenames, keyword):
    print(filename)
t1 = time.time()
print(f'Execution time {t1 - t0} s.')


# def find_in_files_generator(filenames, keyword):
#     for filename in filenames:
#         with open(filename) as f:
#             for line in f:
#                 if keyword in line:
#                     yield filename
#                     break
#
# print(list(find_in_files_generator(filenames, keyword)))
