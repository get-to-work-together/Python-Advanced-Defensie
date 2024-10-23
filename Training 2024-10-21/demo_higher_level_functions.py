

words = 'de kat abacadabra krabt de krullen van de trap o'.split()

print(words)

print(sorted(words))

print(sorted(words, reverse=True))

print(sorted(words, key = len))

print(sorted(words, key = len, reverse=True))

print(sorted(words, key = len))

def aantal_a(word):
    return word.count('a')

def aantal_b(word):
    return word.count('b')


def aantal(word, c):
    return word.lower().count(c)


def aantal_b(word):
    return aantal(word, 'b')

def aantal_a(word):
    return aantal(word, 'a')

# Closures

def my_closure(c):
    def aantal(word):
        return word.lower().count(c)
    return aantal

aantal_a = my_closure('a')
aantal_b = my_closure('b')

print('aap', aantal_a('aap'))

# Partial

from functools import partial

aantal_a = partial(aantal, c='a')
aantal_b = partial(aantal, c='b')

print('Aap', aantal_a('Aap'))
print('babelaar', aantal_b('babelaar'))


def aantal_klinkers(word):
    return len(word.translate(str.maketrans('', '', ' bcdfghjklmnpqrstvwxyz')))

def aantal_klinkers(word):
    return word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u')

def aantal_klinkers(word):
    aantal = 0
    for klinker in 'aeiou':
        aantal += word.count(klinker)
    return aantal

def aantal_klinkers(word):
    d = {}
    for klinker in 'aeiou':
        d[klinker] = word.count(klinker)
    return sum(d.values())

def aantal_klinkers(word):
    counts = []
    for klinker in 'aeiou':
        counts.append(word.count(klinker))
    return sum(counts)

def aantal_klinkers(word):
    return sum(word.count(klinker) for klinker in 'aeiou')


lambda w: sum(w.count(k) for k in 'aeiou')


print(aantal_a('abracadabra'))

print(sorted(words, key = aantal_a))
print(sorted(words, key = lambda word: word.count('b')))
print(sorted(words, key = lambda word: word.count('e')))

print(sorted(words, key = lambda w: sum(w.lower().count(c) for c in 'aeiou')))

