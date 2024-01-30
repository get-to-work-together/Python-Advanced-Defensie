
class NoemerIsNullError(Exception):
    pass


class Breuk:

    def __init__(self, teller, noemer):
        if noemer == 0:
            raise NoemerIsNullError('Delen door 0 is flauwekul.')
        self._teller = teller
        self._noemer = noemer

    def __str__(self):
        return f'{self._teller}/{self._noemer}'

    def __add__(self, other):
        noemer = self._noemer * other._noemer
        teller1 = self._teller * other._noemer
        teller2 = other._teller * self._noemer
        return Breuk(teller1 + teller2, noemer)

    def __mul__(self, other):
        teller = self._teller * other._teller
        noemer = self._noemer * other._noemer
        return Breuk(teller, noemer)

    def __neg__(self):
        return Breuk(-self._teller, self._noemer)

    def __sub__(self, other):
        return self + -other

    def inverse(self):
        return Breuk(self._noemer, self._teller)

    def __truediv__(self, other):
        return self * other.inverse()

    def __float__(self):
        return self._teller / self._noemer

    # getters

    @property
    def teller(self):
        return self._teller

    @property
    def noemer(self):
        return self._noemer

    # setters

    @teller.setter
    def teller(self, value):
        self._teller = value

    @noemer.setter
    def noemer(self, value):
        if value == 0:
            raise NoemerIsNullError('Delen door 0 is flauwekul.')
        self._noemer = value


# ----------------------------------------------------------------------

if __name__ == '__main__':

    b1 = Breuk(1, 2)
    b2 = Breuk(1, 3)

    print(b1)
    print(b2)

    b3 = b1 + b2
    print('opgeteld', b3)

    print('vermenigvuldigd', b1 * b2)

    print('afgetrokken', b1 - b2)

    print('gedeeld door', b1 / b2)

    print('float b1', float(b1))
    print('float b2', float(b2))

    print('teller b1', b1.teller)
    print('noemer b1', b1.noemer)

    b1.noemer = 10

    print(b1)

    b3 = Breuk(12, 0)
    print(b3)