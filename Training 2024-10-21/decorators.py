import logging
import time

logging.basicConfig(
    filename = None,   # None for stderr or to a file 'example.log',
    level = logging.DEBUG,
    format = '%(asctime)s.%(msecs)03d - %(message)s',
    datefmt = '%Y-%m-%dT%H:%M:%S')


def repeater(n):
    def decorator(f):
        def wrapper(*args, **kwargs):
            return_value = None
            for _ in range(n):
                return_value = f(*args, **kwargs)
            return return_value
        return wrapper
    return decorator


def timer(f):
    def wrapper(*args, **kwargs):
        t0 = time.time_ns()
        return_value = f(*args, **kwargs)
        t1 = time.time_ns()
        duration = t1 - t0
        print(f'Function "{f.__name__}" took {duration}ns to execute.')
        return return_value
    return wrapper


def logger(f):
    def wrapper(*args, **kwargs):
        t0 = time.time_ns()
        return_value = f(*args, **kwargs)
        t1 = time.time_ns()
        duration = t1 - t0
        message = f'function: {f.__name__} - args: {args} - kwargs: {kwargs} - duration: {duration}ns'
        logging.info(message)
        return return_value
    return wrapper



def cache(f):
    d = {}
    def wrapper(*args, **kwargs):
        key = tuple(args) + tuple(sorted(kwargs.items()))
        if key in d:
            return_value = d.get(key)
        else:
            return_value = f(*args, **kwargs)
            d[key] = return_value
        return return_value
    return wrapper

