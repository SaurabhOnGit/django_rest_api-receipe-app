"""perform sample test cases"""

from django.test import SimpleTestCase
import calc


class CalculatorTestCases(SimpleTestCase):

    def test_addition(self):
        res = calc.add(2, 4)

        self.assertEqual(res, 6)

