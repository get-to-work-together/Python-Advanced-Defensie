import re
# import doctest
import unittest


def get_email_addresses(text):
    """Search and return e-mail adresses from a provided string

    >> get_email_addresses("abc@def.nl en other email@tip.com")
    ['abc@def.nl', 'email@tip.com']

    """
    matches = re.findall(r'\w+@\w+\.\w{2,3}', text)
    return matches


def cube(x):
    """Calculate power 3 of x

    >> cube(2)
    8

    >> cube(3)
    27

    """
    return x ** 3


def divide(a, b):
    if b == 0:
        raise Exception('Invalid argument value')
    result = a / b
    return result

def calculate_area(width, height):
    if width < 0 or height < 0:
        raise Exception('Invalid argument value')
    area = width * height
    return area

# --------------------------------------------


# class MyTests(unittest.TestCase):
#
#     def test_simple(self):
#         actual = get_email_addresses("abc@def.nl en other email@tip.com")
#         expected = ['abc@def.nl', 'email@tip.com']
#         self.assertEqual(actual, expected)
#
#     def test_divide(self):
#         actual = divide(12, 3)
#         expected = 4
#         self.assertEqual(actual, expected)
#
#     def test_divide_by_zero(self):
#         actual = divide(12, 0)
#         expected = None
#         self.assertEqual(actual, expected)

if __name__ == '__main__':

    # doctest.testmod(verbose=True)

    # text = """This is tekst with a lot of bla bla peter@tip.nl or kars@mindef.nl and patrick@gmail.com"""
    #
    # email_addresses = get_email_addresses(text)
    #
    # print('E-mail addresses found in string:')
    # for email_address in email_addresses:
    #     print(email_address)

    # actual = get_email_addresses("abc@def.nl en other email@tip.com")
    # expected = ['abc@def.nl', 'email@tip.com']
    #
    # assert actual == expected, 'Test failed'
    #
    # actual = get_email_addresses("")
    #
    #
    #
    # unittest.main()


    a = int(input('Geef een getal: '))
    while True:
        b = int(input('Geef nog een getal: '))

        try:
            resultaat = divide(a, b)
            break
        except Exception:
            print('Het tweede getal mag niet 0 zijn!')

    print(resultaat)


