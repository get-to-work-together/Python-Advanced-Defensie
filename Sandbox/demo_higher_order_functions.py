# from functools import partial
#
#
# def my_adder(getal1: (int, float), getal2: (int, float)) -> (int, float):
#     """Add to numbers (int or float)"""
#     sum = getal1 + getal2
#     return sum
#
# result = my_adder(20, 100)
# print(result)


# def my_add_100():
#     fn = partial(my_adder, getal2 = 100)
#     return fn
#
#
# f = my_add_100()
# result = f(20)
# print(result)


from time import time_ns, sleep


def my_decorator(fn):
    history = {}
    def wrapper(*args, **kwargs):
        name = fn.__name__
        t0 = time_ns()
        if args in history:
            result = history[args]
        else:
            result = fn(*args, **kwargs)
            history[args] = result
        t1 = time_ns()
        duration = t1 - t0
        print(f'Function: {name}, duration: {duration} ns')
        print('args', args)
        print('kwargs', kwargs)
        return result
    return wrapper


@my_decorator
def say_hello():
    return 'Hello'

print( say_hello() )

@my_decorator
def say_something(something):
    sleep(1)
    return something.upper()

print( say_something('abacadabra') )
print( say_something('abacadabra') )
print( say_something('abacadabra') )
print( say_something('o jee') )
print( say_something('o jee') )
