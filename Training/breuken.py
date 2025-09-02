import doctest
from typing import Self
import math


class Breuk:
    """Een klasse om met breuken te werken.
    Operaties optellen, aftrekken, vermenigvuldigen en deling zijn geïmplementeerd

    Examples:
    >>> print(Breuk(1, 2))
    1/2
    >>> print(Breuk(1, 2) + Breuk(3, 7))
    13/14


    """

    def __init__(self, teller: int, noemer: int):
        if noemer == 0:
            raise ArithmeticError('Noemer mag niet 0 zijn.')
        self._teller = int(teller)
        self._noemer = int(noemer)

    def __repr__(self):
        return f'Breuk({self._teller}, {self._noemer})'

    def __str__(self):
        if self._noemer == 1:
            return f'{self._teller}'
        elif self._teller > self._noemer:
            return f'{self._teller // self._noemer} {self._teller % self._noemer}/{self._noemer}'
        else:
            return f'{self._teller}/{self._noemer}'

    def __add__(self, other: Self):
        """Implementeert optelling"""
        teller = self._teller * other._noemer + other._teller * self._noemer
        noemer = self._noemer * other._noemer
        return Breuk(teller, noemer).simplify()

    def __sub__(self, other: Self):
        """Implementeert aftrekken"""
        teller = self._teller * other._noemer - other._teller * self._noemer
        noemer = self._noemer * other._noemer
        return Breuk(teller, noemer).simplify()

    def __mul__(self, other: Self):
        """Implementeert vermenigvuldiging"""
        teller = self._teller * other._teller
        noemer = self._noemer * other._noemer
        return Breuk(teller, noemer).simplify()

    def __truediv__(self, other: Self):
        """Implementeert deling

        :param self Een breuk als eerste operand
        :param other Een breuk als tweede operand

        :return Een resulterend breuk"""
        teller = self._teller * other._noemer
        noemer = self._noemer * other._teller
        return Breuk(teller, noemer).simplify()

    def __eq__(self, other):
        return self._teller == other._teller and self._noemer == other._noemer

    def inverse(self):
        """Geeft inverse terug"""
        return Breuk(self._noemer, self._teller).simplify()

    def simplify(self):
        """Vereenvoudigt de breuk"""
        gcd = math.gcd(abs(self._teller), abs(self._noemer))
        if self._noemer < 0:
            self._teller = -self._teller
            self._noemer = -self._noemer
        return Breuk(self._teller // gcd, self._noemer // gcd)


if __name__ == '__main__':

    f1 = Breuk(1, 2)
    f2 = Breuk(2, 3)

    print(f1)
    print(f2)

    print(f1 + f2)
    print(f1 - f2)
    print(f1 * f2)
    print(f1 / f2)

    # f0 = Breuk(10, 0)
    # f0.simplify()

    # DIY test
    f1 = Breuk(1, 2)
    f2 = Breuk(1, 3)
    actual_result = f1 + f2
    expected_result = Breuk(7, 6)
    print(actual_result == expected_result)

    # testing with assert
    assert actual_result == expected_result
