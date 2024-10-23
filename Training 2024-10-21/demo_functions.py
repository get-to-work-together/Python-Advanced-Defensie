


def doe_iets(a, b, c):
    print(a)
    print(b)
    print(c)

def doe_iets(a, *args, factor = 1, **kwargs):
    print(a)
    print(args)
    print(factor)
    print(kwargs)



doe_iets(1,2,3)

doe_iets(1,2,3,4)


doe_iets(1,2,3,4,5)

print('een', 'twee', 'drie', 'vier', 5, sep = '-')

lst = ['een', 'twee', 'drie', 'vier']
print(*lst)

import time
for _ in range(10):
    print('.', end='')
    time.sleep(0.2)
print('\nDone')


doe_iets(1, 2, 3, factor=6, offset=0)

getallen = [3, 4, 5, 6, 7]
doe_iets(*getallen, factor=6, offset=0)

settings = {'factor': 6, 'offset': 0}
doe_iets(*getallen, **settings)