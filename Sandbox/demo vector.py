from copy import copy, deepcopy

class Vector:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f'[{self._x}, {self._y}]'

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def __sub__(self, other):
        return 'Ha Ha Ha LOL Dit gaat echt niet!!!'


v1 = Vector(3, 5)
print(v1)

v2 = Vector(6, 1)
print(v2)

v3 = v1 + v2
print(v3)


print(v1 - v2)

v4 = deepcopy(v1)
v1._x = 99

print(v1)
print(v4)