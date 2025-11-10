import math
from fractions import Fraction

class Breuk:

    def __init__(self, teller, noemer):
        self._teller = teller
        self._noemer = noemer

    def __str__(self):
        return f'{self._teller}/{self._noemer}'

    def __mul__(self, other):
        return Breuk(self._teller * other._teller,
                     self._noemer * other._noemer)

    def __add__(self, other):
        noemer = self._noemer * other._noemer
        teller = self._teller * other._noemer + \
                 other._teller * self._noemer
        return Breuk(teller, noemer)

    def vereenvoudig(self):
        gcd = math.gcd(self._teller, self._noemer)
        return Breuk(self._teller // gcd, self._noemer // gcd)


# -------------------------

if __name__ == '__main__':

    breuk1 = Breuk(1, 2)
    breuk2 = Breuk(1, 3)

    print(breuk1)
    print(breuk2)
    print( breuk1 * breuk2 )
    print( breuk1 + breuk2 )
    print( Breuk(6, 12).vereenvoudig() )
    print( Breuk(4, 12).vereenvoudig() )

    breuk1 = Fraction(1, 2)
    breuk2 = Fraction(1, 3)

    print( breuk1 * breuk2 )
    print( breuk1 + breuk2 )

