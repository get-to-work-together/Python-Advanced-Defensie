import re
import unittest


def validate_postcode(postcode):
    match = re.match(r'^\d{4} ?[a-zA-Z]{2}$', postcode)
    return bool(match)


class TestValidatePostcode(unittest.TestCase):

    def test_valid_postcodes(self):
        postcodes = ['1234AB', '3445 CX', '1238ab']
        results = [validate_postcode(postcode) for postcode in postcodes]
        self.assertTrue(all(results))

    def test_invalid_postcodes(self):
        postcodes = ['123AB', '3445  CX', '1238abc']
        results = [not validate_postcode(postcode) for postcode in postcodes]
        self.assertTrue(all(results))


if __name__ == '__main__':

    pass
