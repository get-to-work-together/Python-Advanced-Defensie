import time
import pickle

cache = {}  # global !!!
def throtle(f):

    def wrapper(*args, **kwargs):
        global cache

        print(f.__name__, args, kwargs)

        if not cache:
            try:
                with open('cache.pickle', 'rb') as fh:
                    cache = pickle.load(fh)
            except FileNotFoundError:
                cache = {}

        key = (f.__name__,) + args
        return_value = cache.get(key, f(*args, **kwargs))

        cache[key] = return_value

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