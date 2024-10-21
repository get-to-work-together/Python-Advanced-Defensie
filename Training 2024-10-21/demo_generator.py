"""A module with experimental functions

Written by: Peter
Date: 2024-10-21"""

from typing import List
import unittest


def geef_even_getallen(bovengrens: int, f = None) -> List[int]:
    """Geef getallen terug filtered by the specified function

    >> geef_even_getallen(10, lambda i: i % 2 == 0)
    [0, 2, 4, 6, 8]

    >> geef_even_getallen(12, lambda i: i > 5)
    [6, 7, 8, 9, 10, 11]

    >> geef_even_getallen(5)
    [0, 1, 2, 3, 4]

    """
    if not f:
        f = lambda getal: True
    getallen = []
    for getal in range(1, int(bovengrens)):
        if f(getal):
            getallen.append(getal)
    return getallen



class TestGenerator(unittest.TestCase):

    def test_simple1(self):
        actual = geef_even_getallen(10, lambda i: i % 2 == 0)
        expected = [0, 2, 4, 6, 8]
        self.assertEqual(expected, actual)

    def test_simple2(self):
        actual = geef_even_getallen(12, lambda i: i > 5)
        expected = [6, 7, 8, 9, 10, 11]
        self.assertEqual(expected, actual)



def test_simple1():
    actual = geef_even_getallen(12, lambda i: i > 6)
    expected = [6, 7, 8, 9, 10, 11]
    assert expected == actual, 'Lists are different'


# -----------------------------------------------------------------

if __name__ == '__main__':
    # unittest.main()

    test_simple1()