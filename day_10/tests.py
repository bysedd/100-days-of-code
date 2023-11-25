import unittest
from random import randint

from calculator import add, subtract, multiply, divide


class CalculatorTests(unittest.TestCase):
    def test_operations(self):
        operations = [add, subtract, multiply, divide]
        for operation in operations:
            a = randint(-100, 100)
            b = randint(-100, 100)
            expected = operation(a, b)
            self.assertEqual(operation(a, b), expected)

    def test_division_by_zero_raises_exception(self):
        with self.assertRaises(ZeroDivisionError):
            divide(randint(-100, 100), 0)


if __name__ == "__main__":
    unittest.main()
