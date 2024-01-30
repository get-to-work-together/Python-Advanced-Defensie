from datetime import datetime
import time
import pickle

cache = {}  # global !!!
def throtle(f):

    def wrapper(*args, **kwargs):
        hours = 24
        duration = 60 * 60 * hours     # in seconds

        global cache

        print(f.__name__, args, kwargs)

        if not cache:
            try:
                with open('cache.pickle', 'rb') as fh:
                    cache = pickle.load(fh)
            except FileNotFoundError:
                cache = {}

        key = (f.__name__,) + args

        if key in cache.keys():
            timestamp, return_value = cache[key]
            if (datetime.now() - timestamp).seconds > duration:
                timestamp = datetime.now()
                return_value = f(*args, **kwargs)
                cache[key] = (timestamp, return_value)
        else:
            timestamp = datetime.now()
            return_value = f(*args, **kwargs)
            cache[key] = (timestamp, return_value)

        with open('cache.pickle', 'wb') as fh:
            pickle.dump(cache, fh)

        return return_value
    return wrapper


if __name__ == '__main__':

    @throtle
    def telop(a, b):
        return a + b


    print(telop(10, 20))
    print(telop(67, 43))
    print(telop(10, 20))
    print(telop(10, 20))

    print(cache)