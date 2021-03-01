-- How to download --
If pull request was not merged yet, download from develop brach:
git clone https://github.com/VKasaraba/Incora_CodingCamp2021.git --branch develop
Otherwise,
git clone https://github.com/VKasaraba/Incora_CodingCamp2021.git
Or download the zip archive and unpack it.

-- Running the tests --
1. Open the directory containing unittets_ccy.py file in a terminal and run the command 
"python3 unittets_ccy.py" or run the file explicitly in your IDE.

2. Open the directory containing unittets_currency_converter.py file in a terminal and run the command 
"python3 unittets_currency_converter.py" or run the file explicitly in your IDE.

-- Project Structure and Classes Explanation --
1. File ccy.py contains class Ccy, which represents a banknote, as it takes a numeric
value and a currency as inputs. The class includes all needed logic to support arithmetical
operations between any amount of Ccy objects (banknotes), even if they have different currencies,
and between Ccy objects and numeric objects like integer, float, and string if it contains a number.
While executing arithmetical operations with different currencies, the result will display the
calculated value in all currencies that are present in the operation as they appear in order from left to right.

Example: 
bgn1 = Ccy(1, 'BGN')
eur1 = Ccy(1, 'EUR')
usd1 = Ccy(1, "USD")
print(bgn1 + eur1 - usd1)

Output:
1.33 BGN  or  0.68 EUR  or  0.83 USD

The private classmethod __ariphmetic_helper(*args) is used by all arithmetical magic method to avoid code 
redundancy. 
The method __sts__(self, *args) is overridden to display the result value in all used currencies using the
private queue __currencies_to_display.

2. File currency_converter.py contains class CurrencyConverter which converts currencies using an online banking
service called Fixer. The class only has one method convert(cls, *args) to convert a banknote value from
one currency to another.  

3. File config.py contains an URL to Fixer service and an access_key which is used by CurrencyConverter class 
to gain actual info for today's currencies' rates.

4. File unittest_ccy.py contains tests for the Ccy class. The instructions on how to run the test are included
in a corresponding topic above.
