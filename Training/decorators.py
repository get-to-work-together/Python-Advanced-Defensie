import time
import pickle


def measure_time(f):
    def inner(*args):
        t0 = time.time_ns()
        result = f(*args)
        t1 = time.time_ns()
        print(f'This function was excuted in {t1 - t0} ns')
        return result
    return inner

def debug_info(f):
    def inner(*args, **kwargs):
        print(80*'-')
        print(f'Entering function: {f.__name__}')
        print(f'Positional arguments: {args}')
        print(f'Keyword arguments: {kwargs}')
        t0 = time.time_ns()
        result = f(*args, **kwargs)
        t1 = time.time_ns()
        print(f'Return value: {result}')
        print(f'This function was excuted in {t1 - t0} ns')
        print(80*'-')
        return result
    return inner


def cache(f):
    d = {}
    def inner(*args, **kwargs):
        nonlocal d
        try:
            with open('saved_pickle.pkl', 'rb') as fh:
                d = pickle.load(fh)
        except FileNotFoundError:
            pass
        if args in d:
            result = d[args]
        else:
            result = f(*args, **kwargs)
            d[args] = result
            with open('saved_pickle.pkl', 'wb') as fh:
                pickle.dump(d, fh)
        return result
    return inner


@measure_time
@cache
def berekening(a, b, c):
    time.sleep(0.3)
    result = (a ** b) * c
    return result


if __name__ == '__main__':
    print(berekening(23, 45, 7))
    print(berekening(23, 45, 7))
    print(berekening(1, 2, 3))
    print(berekening(1, 2, 3))
    print(berekening(1, 2, 3))