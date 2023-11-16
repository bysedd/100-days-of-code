import unittest

from calculator import add, subtract, multiply, divide


class CalculatorTests(unittest.TestCase):
    def test_addition_with_positive_numbers(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtraction_with_positive_numbers(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiplication_with_positive_numbers(self):
        self.assertEqual(multiply(5, 3), 15)

    def test_division_with_positive_numbers(self):
        self.assertEqual(divide(6, 3), 2)

    def test_addition_with_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)

    def test_subtraction_with_negative_numbers(self):
        self.assertEqual(subtract(-5, -3), -2)

    def test_multiplication_with_negative_numbers(self):
        self.assertEqual(multiply(-5, -3), 15)

    def test_division_with_negative_numbers(self):
        self.assertEqual(divide(-6, -3), 2)

    def test_division_by_zero_raises_exception(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)


if __name__ == "__main__":
    unittest.main()
