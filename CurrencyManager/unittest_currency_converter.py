from unittest.case import TestCase
from currency_converter import CurrencyConverter as Cc
import unittest


# Notice: currency rates constantly change; the test were written in March 2021
class TestResult(TestCase):
    def test_conversion_result(self):
        self.assertAlmostEqual(28, Cc.convert(1, 'USD', 'UAH'), 0)
        self.assertAlmostEqual(2, Cc.convert('2', 'EUR', 'EUR'), 0)

    # check that errors are raised when necessary
    def test_errors_rising(self):
        with self.assertRaises(ValueError):
            Cc.convert(1, 'USD', 'Dragon Currency')
        with self.assertRaises(ValueError):
            Cc.convert(1, 'Elf Currency', 'USD')
        with self.assertRaises(ValueError):
            Cc.convert('impostor', 'EUR', 'EUR')


if __name__ == '__main__':
    unittest.main()
