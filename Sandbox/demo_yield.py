import random
import time

def willekeurig(s, n = 10):
    """return n random characters from the provided string"""
    characters = []
    for _ in range(n):
        characters.append(random.choice(s))
    return characters


def willekeurig(s, n = 10):
    """return n random characters from the provided string"""
    for _ in range(n):
        yield random.choice(s)


t0 = time.time_ns()

for c in willekeurig('abcdefg', n = 30000000):
    print(c)

t1 = time.time_ns()

print(f'Duration: {t1 - t0}ns')




