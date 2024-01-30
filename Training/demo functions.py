from breuken import Breuk


def book_flight(from_airport: str,
                to_airport: str,
                num_adults: int = 1,
                num_children: int = 0) -> None:
    print(f'Flight booked from {from_airport} to {to_airport}')
    print(f'Number of adults: {num_adults}')
    print(f'Number of children: {num_children}')


def cancel_flight(*args, **kwargs):
    print(args)
    print(kwargs)


book_flight('AMS', 'CDG', 2, 2)

args = ('AMS', 'CDG', 2, 2)
book_flight(*args)

book_flight('AMS', 'CDG', 2)
book_flight('AMS', 'CDG')
book_flight('AMS', 'CDG', num_children=2, num_adults=10)
book_flight(from_airport='AMS', to_airport='CDG', num_children=2, num_adults=10)

kwargs = {
    'from_airport': 'AMS',
    'to_airport': 'CDG',
    'num_children': 2,
    'num_adults': 10
}

book_flight(**kwargs)

cancel_flight('AMS', 'CDG', booked_by='Peter')


def count_character(word: str, c) -> int:
    return word.lower().count(c)

# Partial
from functools import partial
count_a = partial(count_character, {'c':'a'})

# Closure
def count_a(word):
    c = 'a'
    def count_character(word, c):
        return word.count(c)
    return count_character



print(word := 'abacadabraaaa', count_character(word, 'a'))

words = 'de aap krabt de krullen van de wenteltrap'.split()

print(words)
print(sorted(words))
print(sorted(words, reverse=True))
print(sorted(words, key=len))
print(sorted(words, key=lambda word: count_character(word, 'a')))
print(sorted(words, key=lambda word: word.lower().count('e')))
print(sorted(words, key=partial(count_character, c='e')))

import time

# decorator
def log(f):
    def wrapper():
        print('Entering', f.__name__)
        t0 = time.time_ns()
        f()
        t1 = time.time_ns()
        print('Duration:', t1 - t0)
        print('Done')

    return wrapper


@log
def say_hello():
    print('Hello')
    time.sleep(3)
    print('Awake')

from functools import cache

@cache
def telop(a, b):
    time.sleep(2)
    return a + b


print('Start 1')
print(telop(4, 5))
print('Start 1')
print(telop(4, 5))
print('Done')

