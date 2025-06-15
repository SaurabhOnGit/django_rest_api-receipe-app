from django.test import SimpleTestCase
import calc

class CalculatorTestCases(SimpleTestCase):
    def test_addition(self):
        self.assertEqual(calc.add(2, 4), 6)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(0, 0), 0)
        self.assertEqual(calc.add(-5, -3), -8)

    def test_subtraction(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(0, 0), 0)
        self.assertEqual(calc.subtract(-3, -7), 4)
        self.assertEqual(calc.subtract(5, 10), -5)

    def test_multiplication(self):
        self.assertEqual(calc.multiply(3, 4), 12)
        self.assertEqual(calc.multiply(-2, 3), -6)
        self.assertEqual(calc.multiply(0, 100), 0)
        self.assertEqual(calc.multiply(-5, -2), 10)

    def test_division(self):
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertEqual(calc.divide(-9, 3), -3)
        self.assertEqual(calc.divide(0, 1), 0)
        with self.assertRaises(ZeroDivisionError):
            calc.divide(5, 0)