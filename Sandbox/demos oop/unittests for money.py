from unittest import TestCase
from money import Money


class TestMoney(TestCase):

    def test_instantiation(self):
        bedrag = Money(30)
        actual = str(bedrag)
        expected = '€30.00'
        self.assertEquals(expected, actual)

    def test_add(self):
        bedrag1 = Money(30)
        bedrag2 = Money(20)
        bedrag = bedrag1 + bedrag2
        actual = str(bedrag)
        expected = '€50.00'
        self.assertEquals(expected, actual)