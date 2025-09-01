import os
from pprint import pprint

path = os.environ["PATH"]

paths = path.split(':')
pprint(paths)


# os.environ['DB_PASSWORD'] = 'Welkom!123'

print('Environment Variables')
for k, v in os.environ.items():
    print(f'{k:25}: {v}')