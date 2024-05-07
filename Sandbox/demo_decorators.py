import time
import logging

logging.basicConfig(
    filename = None, # 'example.log',
    level = logging.DEBUG,
    format = '%(asctime)s.%(msecs)03d - %(message)s',
    datefmt = '%Y-%m-%dT%H:%M:%S')




def deco(f):
    def wrapper(*args, **kwargs):
        print(f'---- Calling {f.__name__}')
        t0 = time.time_ns()
        f(*args, **kwargs)
        t1 = time.time_ns()
        print(f'---- duration {t1 - t0}ns')
    return wrapper


def logger(f):
    def wrapper(*args, **kwargs):
        logging.info(f'In function: {f.__name__} - args: {args} - kwargs: {kwargs}')
        return_value = f(*args, **kwargs)
        return return_value
    return wrapper





@logger
def say_hi(name):
    print(f'Hi {name}')


say_hi('Mathijs')
say_hi('Joris')
