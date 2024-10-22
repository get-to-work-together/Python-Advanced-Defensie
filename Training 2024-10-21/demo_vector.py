
class Vector:
    """A class for vector"""

    def __init__(self, x: int|float, y: int|float):
        self.x = x
        self.y = y

    def __str__(self):
        return f'[{self.x}, {self.y}]'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

# ----------------------

if __name__ == '__main__':

    v1 = Vector(5, 5)
    v2 = Vector(4, -3)

    print(v1)
    print(v2)

    v3 = v1 + v2

    print(v3)

    print(v1.length())
    print(v2.length())
    print(v3.length())