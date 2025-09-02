import time
import logging


logging.basicConfig(
    filename = None,   # or to a file 'example.log',
    level = logging.DEBUG,
    format = '%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S')


def show_execution_time(f):
    def wrapper(*arg, **kwargs):
        t0 = time.time()
        return_value = f(*arg, **kwargs)
        t1 = time.time()
        print(f'Executed {f.__name__} in {t1 - t0}s')
        return return_value
    return wrapper


memory = {}
def cache(f):
    def wrapper(*args, **kwargs):
        if args in memory:
            return_value = memory[args]
        else:
            return_value = f(*args, **kwargs)
            memory[args] = return_value
        return return_value
    return wrapper


def log_function_calls(f):
    def wrapper(*args, **kwargs):
        logging.debug(f'Calling {f.__name__} with {args} and {kwargs} ... ')
        return_value = f(*args, **kwargs)
        logging.debug(f'Result  {f.__name__} with {args} and {kwargs} => {return_value}')
        return return_value
    return wrapper



@show_execution_time
def print_repeat(s, n):
    for _ in range(n):
        time.sleep(0.3)
        print(s)


@cache
def bereken(a, b):
    time.sleep(2)
    return a + b


@log_function_calls
def f1(a, b, c):
    return a + b + c

@log_function_calls
def f2(a, b, c):
    return a - b + c

@log_function_calls
def f3(a, b, c):
    time.sleep(0.1)
    return a + b - c

@log_function_calls
def f4(a, b, c):
    return a * b * c

@log_function_calls
def f5(a, b, c):
    return (a + b) * c

@log_function_calls
def f6(a, b, c):
    return a * (b + c)


# -------------------------------------------------------------

# print_repeat('abc', 10)

# print(bereken(23, 45))
# print(bereken(23, 45))
# print(bereken(23, 45))
# print(bereken(23, 45))
# print(bereken(23, 45))

f1(3,6,8)
f3(4,7,2)
f4(5,2,4)
f6(f1(3,6,8), f4(5,2,4), f3(4,7,2))
f5(23,4,1)
f2(5,5,f5(23,4,1))
f2(5,f5(23,4,1),5)

