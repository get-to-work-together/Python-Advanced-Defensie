from datetime import date, datetime
import time
import logging


logging.basicConfig(
    filename = None,                # or 'example.log',
    level = logging.DEBUG,
    format = '%(asctime)s.%(msecs)03d - %(message)s',
    datefmt = '%Y-%m-%dT%H:%M:%S')


def duration(f):
    def wrapper(*args, **kwargs):
        t0 = time.time_ns()
        return_value = f(*args, **kwargs)
        t1 = time.time_ns()
        logging.info(f'Duration: {t1 - t0}ns')
        return return_value
    return wrapper


def logger(f):
    def wrapper(*args, **kwargs):
        logging.info(f'In function: {f.__name__} - args: {args} - kwargs: {kwargs}')
        return_value = f(*args, **kwargs)
        return return_value
    return wrapper



def cache(f):
    cache_data = {}
    def wrapper(*args, **kwargs):
        key = tuple(args) + tuple(kwargs.items())
        if key not in cache_data:
            return_value = f(*args, **kwargs)
            cache_data[key] = return_value
        else:
            return_value = cache_data[key]
        return return_value
    return wrapper


def to_date(date_arg=None, date_format='%Y-%m-%d'):
    if date_arg is None:
        return date.today()
    if isinstance(date_arg, date):
        return date_arg
    elif isinstance(date_arg, str):
        return datetime.strptime(date_arg, date_format).date()


@duration
@cache
def bereken(a, b, c, d):
    time.sleep(1)
    return a ** 2 + b ** 3 + c ** 4 + d ** 5


if __name__ == '__main__':

    print(bereken(3,6,5,7))
    print(bereken(6,9,5,7))
    print(bereken(6,9,5,7))
    print(bereken(6,9,50,7))
    print(bereken(6,9,50,7))
    print(bereken(6,9,50,7))
