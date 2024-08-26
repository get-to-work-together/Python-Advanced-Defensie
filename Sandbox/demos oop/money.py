from dataclasses import dataclass
from typing import Self


@dataclass
class Money:
    """Dit is mijn Money class with different currencies

    >>> Money(30)
    Money(_amount=30, _currency='EUR', _symbol='€')

    >>> str(Money(30))
    '€30.00'

    >>> str(Money(30, '$'))
    '$30.00'

    """

    _amount: float
    _currency: str = 'EUR'
    _symbol: str = '€'

    rates_from_euro = {
        'EUR': 1.00,
        'USD': 1.12
    }

    symbols = {
        'EUR': '€',
        'USD': '$'
    }

    def __str__(self) -> str:
        amount = float(abs(self._amount))
        if self.currency in self.symbols:
            f = self.symbols[self.currency] + '{:.2f}'
            s = f.format(amount)
            if self._amount < 0:
                s = '-' + s
        else:
            s = f'{self.currency} {self.amount}'
        return s

    @staticmethod
    def exception_if_currency_not_equal(currency1, currency2):
        if currency1 != currency2:
            raise Exception('Can only compare amounts of same currency.')

    def __eq__(self, other) -> bool:
        self.exception_if_currency_not_equal(self.currency, other.currency)
        return self.amount == other.amount

    def __ne__(self, other) -> bool:
        self.exception_if_currency_not_equal(self.currency, other.currency)
        return self.amount != other.amount

    def __gt__(self, other) -> bool:
        self.exception_if_currency_not_equal(self.currency, other.currency)
        return self.amount > other.amount

    def __ge__(self, other) -> bool:
        self.exception_if_currency_not_equal(self.currency, other.currency)
        return self.amount >= other.amount

    def __lt__(self, other) -> bool:
        self.exception_if_currency_not_equal(self.currency, other.currency)
        return self.amount < other.amount

    def __le__(self, other) -> bool:
        self.exception_if_currency_not_equal(self.currency, other.currency)
        return self.amount <= other.amount

    def __add__(self, other) -> Self:
        self.exception_if_currency_not_equal(self.currency, other.currency)
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other) -> Self:
        self.exception_if_currency_not_equal(self.currency, other.currency)
        return Money(self.amount - other.amount, self.currency)

    def __neg__(self) -> Self:
        return Money(-self.amount, self.currency)

    @property
    def currency(self) -> str:
        """Setter for the currency"""
        return self._currency

    @property
    def amount(self) -> float:
        return round(self._amount, 2)

    def convert(self,
                target_currency: str,
                rate: float = None,
                target_symbol: str = None) -> Self:
        """Convert from one currency to another"""

        if rate is not None:
            self.rates_from_euro[target_currency] = rate
        else:
            try:
                rate = self.rates_from_euro[target_currency]
            except KeyError:
                raise Exception(f'Unknown rate for {target_currency}')

        if target_symbol is not None:
            self.symbols[target_currency] = target_symbol

        return Money(self.amount * rate, target_currency)


# ----------------------------------------------------


if __name__ == '__main__':

    bedrag1 = Money(100)
    bedrag2 = Money(200)

    print(bedrag1)
    print(bedrag2)

    print(bedrag1.currency)
    print(bedrag1.amount)

    print('equal:', bedrag1 == bedrag2)
    print('not equal:', bedrag1 != bedrag2)
    print('greater:', bedrag1 > bedrag2)
    print('greater or equal:', bedrag1 >= bedrag2)
    print('less:', bedrag1 < bedrag2)
    print('less or equal:', bedrag1 <= bedrag2)

    print(bedrag1 + bedrag2)
    print(bedrag1 - bedrag2)
    print(-bedrag1)

    print(bedrag1.convert('EUR'))
    print(bedrag1.convert('USD'))
    print(bedrag1.convert('GBP', 0.8473, '£'))
    print(bedrag1.convert('GBP'))

    actual = bedrag1 == bedrag2
    expected = False
    if actual == expected:
        print('Test OK')
    else:
        print('Test error')

    assert bedrag1 == bedrag2, 'Assert Error'

