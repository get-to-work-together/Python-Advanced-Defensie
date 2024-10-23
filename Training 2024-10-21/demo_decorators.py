from datetime import datetime
import time

from decorators import logger, cache, repeater


# def repeater(f):
#     def wrapper():
#         for _ in range(3):
#             f()
#     return wrapper


def debugger(f):
    def wrapper():
        print(f'Entered function "{f.__name__}" at {datetime.now()}.')
        f()
    return wrapper


def timer(f):
    def wrapper(*args, **kwargs):
        t0 = time.time_ns()
        f(*args, **kwargs)
        t1 = time.time_ns()
        duration = t1 - t0
        print(f'Function "{f.__name__}" took {duration}ns to execute.')
    return wrapper



@repeater(5)
@logger
@cache
def say_hi(name = 'Stranger'):
    print(f'Hi {name}. How do you do?')


@logger
@cache
def calculate_pythagoras(x, y):
    time.sleep(0.2)
    return (x ** 2 +  y ** 2) ** 0.5


say_hi('Peter')
# say_hi('Dave')
# say_hi('Stefan')
# time.sleep(1)
# say_hi(name='Peter')

result = calculate_pythagoras(23, 4)
result = calculate_pythagoras(23, 4)
result = calculate_pythagoras(23, 5)
result = calculate_pythagoras(23, 4)
result = calculate_pythagoras(23, 4)
result = calculate_pythagoras(23, 5)