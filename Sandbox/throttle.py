from datetime import datetime
import time
import pickle
from functools import wraps


def throttle(seconds = 60 * 60, persistent = False, pickle_filename = 'throttle.pickle'):
    """Decorator to memorize function result for a specified periode."""
    def decorator(f):
        duration = seconds
        cache = {}
        @wraps(f)
        def wrapper(*args, **kwargs):
            nonlocal cache
            if not cache:
                if persistent:
                    try:
                        with open(pickle_filename, 'rb') as fh:
                            cache = pickle.load(fh)
                    except FileNotFoundError:
                        cache = {}
                else:
                    cache = {}

            key = (f.__name__,) + args + tuple(kwargs.items())

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

            if persistent:
                with open(pickle_filename, 'wb') as fh:
                    pickle.dump(cache, fh)

            return return_value
        return wrapper
    return decorator


if __name__ == '__main__':

    @throttle()
    def telop(a, b):
        return a + b


    print(telop(10, 20))
    print(telop(67, 43))
    print(telop(10, 20))
    print(telop(10, 20))
    time.sleep(4)
    print(telop(10, 20))
