import math
import random
from fractions import Fraction

class Breuk:
    """My Breuk class to work with fractions

    >> b1 = Breuk(1, 2)
    >> b1.vereenvoudig()

    """

    division_character = '÷'

    @staticmethod
    def change_division_character(c):
        Breuk.division_character = c

    def __init__(self, teller, noemer):
        self._teller = teller
        self._noemer = noemer

    def __str__(self):
        return f'{self._teller}{Breuk.division_character}{self._noemer}'

    def __mul__(self, other):
        return Breuk(self._teller * other._teller,
                     self._noemer * other._noemer)

    def __add__(self, other):
        noemer = self._noemer * other._noemer
        teller = self._teller * other._noemer + \
                 other._teller * self._noemer
        return Breuk(teller, noemer)

    @property
    def teller(self):
        return self._teller

    @property
    def noemer(self):
        return self._noemer

    @teller.setter
    def teller(self, value):
        if value > 0:
            self._teller = value

    def vereenvoudig(self):
        """Simplify the fraction by dividing nominator by
        the greatest common divisor."""
        gcd = math.gcd(self._teller, self._noemer)
        return Breuk(self._teller // gcd, self._noemer // gcd)


# -------------------------

if __name__ == '__main__':

    breuk1 = Breuk(1, 2)
    breuk2 = Breuk(1, 3)

    Breuk.change_division_character('|')

    print(breuk1)
    print(breuk2)
    print( breuk1 * breuk2 )
    print( breuk1 + breuk2 )
    print( Breuk(6, 12).vereenvoudig() )
    print( Breuk(4, 12).vereenvoudig() )

    print(breuk2.teller)
    print(breuk2.noemer)

    breuk2.teller = 2

    breuk1 = Fraction(1, 2)
    breuk2 = Fraction(1, 3)

    print( breuk1 * breuk2 )
    print( breuk1 + breuk2 )

