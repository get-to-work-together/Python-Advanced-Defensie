from dataclasses import dataclass
from typing import Self

@dataclass
class Person:

    _name: str
    _residence: str
    _age: int = None

    # __slots__ = ('_name', '_residence', '_age')

    # def __init__(self, name, residence = 'unknown'):
    #     self._name = name
    #     self._residence = residence
    #
    # def __repr__(self):
    #     return f'Person("{self._name}", "{self._residence}")'

    def __str__(self):
        return f'Person object: {self._name}, {self._residence}'

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, Person):
            raise Exception('other is not a Person object')
        return self._name == other._name

    def __ne__(self, other: Self) -> bool:
        return self._name != other._name

    def __gt__(self, other: Self) -> bool:
        return self._name > other._name

    def __ge__(self, other: Self) -> bool:
        return self._name >= other._name

    def __lt__(self, other: Self) -> bool:
        return self._name < other._name

    def __le__(self, other: Self) -> bool:
        return self._name <= other._name

    def tell(self) -> str:
        return f'I am {self._name} and I live in {self._residence}'

    def move(self, new_residence: str):
        self._residence = new_residence.upper()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == '':
            print('name cannot be empty!')
        else:
            self._name = value.upper()

    @classmethod
    def default(cls):
        return cls('Anoniem', 'Nowhere')

    @staticmethod
    def default2():
        return Person('Anoniem', 'Nowhere')

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: (int, float)):
        self._age = value

# --------------------------------------------------------------------

p1 = Person('Albert', 'Amsterdam')
p2 = Person('Albert', 'Amsterdam')

print(repr(p1))
print(repr(p2))

print(p1 == p2)

print(p1.name)
p1.name = 'Peter'
print(p1)

p1.move('Soesterberg')

p1.tell()

p1.age = 45.0
print(repr(p1))

print(p1 == p2)
