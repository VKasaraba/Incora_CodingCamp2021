from unittest.case import TestCase
from ccy import Ccy
from currency_converter import CurrencyConverter
import unittest

usd1 = Ccy(1, 'USD')  # $1
eur1 = Ccy('1', 'EUR')  # $1.21
bgn1 = Ccy(1, 'BGN')  # $0.62


class TestResult(TestCase):
    def test_addition_result_values(self):
        # the .value will display result in the currecy that appeared the first
        self.assertEqual(3, (bgn1 + 2).value)
        self.assertEqual(3, ('2' + bgn1).value)
        # use assertAlmostEqual with round to int, as rates constantly change
        self.assertAlmostEqual(2, (usd1 + eur1).value, 0)
        self.assertAlmostEqual(3, (usd1 + eur1 + bgn1).value, 0)

    def test_substraction_result_values(self):
        self.assertEqual(-1, (bgn1 - 2).value)
        self.assertEqual(1, ('2' - bgn1).value)
        self.assertAlmostEqual(0, (usd1 - eur1).value, 0)
        self.assertAlmostEqual(-1, (usd1 - eur1 - bgn1).value, 0)

    def test_miltiplication_result_values(self):
        self.assertEqual(2, (bgn1 * 2).value)
        self.assertEqual(2, ('2' * bgn1).value)
        self.assertAlmostEqual(1, (usd1 * eur1).value, 0)
        self.assertAlmostEqual(1, (usd1 * eur1 * bgn1).value, 0)
        self.assertAlmostEqual(6, (2*usd1 * 2*eur1 * 2*bgn1).value, 0)

    def test_division_result_values(self):
        self.assertEqual(0.5, (bgn1 / 2).value)
        self.assertAlmostEqual(1, usd1 / eur1, 0)
        self.assertAlmostEqual(2, usd1 / bgn1, 0)
        self.assertAlmostEqual(1, (usd1 / eur1) / (bgn1 / usd1), 0)
        self.assertAlmostEqual(3, usd1 / (eur1 / 2) / (bgn1/usd1), 0)

    def test_combined_arithmetical_result_values(self):
        self.assertAlmostEqual(1, (bgn1 + eur1 - usd1).value, 0)
        self.assertAlmostEqual(4, (3 * (bgn1 + eur1 - usd1)).value, 0)
        self.assertAlmostEqual(2, (3 * (bgn1 + eur1 - usd1) / eur1), 0)
        self.assertAlmostEqual(
            0, ((2 * usd1 - eur1 / 2) * (1 - usd1)).value, 0)
        self.assertAlmostEqual(9, ('1.1' + bgn1 * usd1) / (eur1 - bgn1) * 3, 0)
        self.assertAlmostEqual(7, 2*bgn1*usd1/eur1*3.5 + ('1.2'*eur1)/usd1, 0)

    # test that results are printed in all needed currencies
    def test_result_print(self):
        str(eur1)
        self.assertEqual('1 EUR', str(eur1))
        self.assertEqual('1.12 USD', str(usd1 + 0.12))
        self.assertEqual('3 USD', str(usd1 + 2*usd1))
        self.assertEqual('{:.2f} BGN  or  {:.2f} USD'.format(
            (bgn1+usd1).value, CurrencyConverter
            .convert((bgn1 + usd1).value, 'BGN', 'USD')), str(bgn1 + usd1))
        self.assertEqual('{:.2f} EUR  or  {:.2f} USD  or  {:.2f} BGN'.format(
            (4 * (eur1 - usd1) + bgn1/2).value, CurrencyConverter.convert(
                (4 * (eur1 - usd1) + bgn1/2).value, 'EUR', 'USD'
            ), CurrencyConverter.convert((4*(eur1-usd1)+bgn1/2
                                          ).value, 'EUR', 'BGN')),
            str(4*(eur1-usd1)+bgn1/2))


if __name__ == '__main__':
    unittest.main()
