from typing import List
import random


class InvalidArgumentException(ValueError):
    pass


def calculate_area(width, height):
    if width < 0 or height < 0:
        raise InvalidArgumentException('Measurements can not be negative.')
    return width * height


def telop(*numbers: List[int], factor: int = 1) -> int:
    try:
        total = 0
        for number in numbers:
            if number >= 0:
                total += number
            else:
                raise InvalidArgumentException('Measurements can not be negative.')
        return factor * total
    except TypeError:
        raise InvalidArgumentException('Not all arguments are numeric.')


random_numbers = [random.randint(1, 100) for _ in range(20)] + [-2]

# try:
#     print( 'Resultaat:', telop(*random_numbers, factor = 2) )
# except InvalidArgumentException as ex:
#     print('Error:', ex)

# try:
#     print( 'Resultaat:', telop('aap', 'noot', factor = 3) )
# except InvalidArgumentException as ex:
#     print('Error:', ex)



# print( calculate_area(-2, 3) )


def telop(a, b):
    return a + b

telop = lambda a, b: a + b

print( telop(34, 67) )

s = 'dit is een stukje tekst met hele lange woorden abacadabra tent'



words = sorted( s.split(), key = lambda word: word.count('o') )

print(words)

print( list(filter(lambda word: len(word) >= 4, words)) )

print( list(map(lambda word: (word[0] + word[-1]).upper(), words)) )

print( [(word[0] + word[-1]).upper() for word in words if len(word) >= 4] )

print( {(word[0] + word[-1]).upper() for word in words if len(word) >= 4} )

print( {word:(word[0] + word[-1]).upper() for word in words if len(word) >= 4} )

print( ((word[0] + word[-1]).upper() for word in words if len(word) >= 4) )


