import unittest
from Project.src.utils.decorators import throttle

class TestDecorators(unittest.TestCase):

    def test_trottle(self):
        @throttle
        def test(a, b):
            return a + b
        actual1 = test(1, 2)
        actual2 = test(1, 2)
        expected = 3
        self.assertEqual(expected, actual1)
        self.assertEqual(expected, actual2)


if __name__ == '__main__':
    unittest.main()
