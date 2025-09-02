from decimal import Decimal


class Currency:

    currency_symbol = '€'

    def __init__(self, amount):
        self._amount = Decimal(str(amount))

    def __repr__(self):
        return f'Currency({self._amount:.2f})'

    def __str__(self):
        return f'{Currency.currency_symbol}{self._amount:.2f}'

    def __add__(self, other):
        return Currency(self._amount + other._amount)

    def __sub__(self, other):
        return Currency(self._amount - other._amount)

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, (int, float)):
            self._amount = Decimal(str(value))
        elif isinstance(value, str):
            self._amount = Decimal(str(value))


if __name__ == '__main__':

    currency = Currency(20)

    print(repr(currency))
    print(str(currency))
    print(currency)

    amount = Currency(121.50)
    print(amount)

    total = currency + amount
    print(total)

    total = currency - amount
    print(total)

    total.amount = '1000000'

    print(total.amount)

    print(Currency(0.10) + Currency(0.20))