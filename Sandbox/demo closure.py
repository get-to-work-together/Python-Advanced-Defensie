import pickle
from pprint import pprint
from operator import itemgetter
import random


def closure(message):

    def display():
        print(message)

    return display

f1 = closure('Hi there')
f2 = closure('Howdy')

print(f1)
f1()
f2()

s = r'''The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.
In particular, secrets should be used in preference to the default pseudo-random number generator in the random module, which is designed for modelling and simulation, not security or cryptography.
See also PEP 506'''

words = s.lower().translate(str.maketrans('','','.,')).split()

d = {word: words.count(word) for word in set(words)}

for word, n in sorted(d.items(), key = itemgetter(1)):
    print(f'{word:20}: {n:3} {"*" * n}')


getallen = [random.randint(1, 100) for _ in range(20)]

print(getallen)

print(getallen[5:7])

sl = slice(5, 7)
print(getallen[sl])

print( [getal%10 for getal in getallen[sl]] )
