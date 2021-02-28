import requests
from config import rates_url


class CurrencyConverter():
    ''' Converts currencies with "convert" method using Fixer service '''
    __currencies_info = requests.get(rates_url).json()
    __rates = __currencies_info['rates']

    @classmethod
    def convert(cls, value: float, from_curr: str, to_curr: str):
        if from_curr not in cls.__rates or to_curr not in cls.__rates:
            raise ValueError('Invalid currency')
        # Fixer service uses EUR as its base currency, so for conversion
        # we devide value by coefficient relatively to EUR
        value_in_eur = value/cls.__rates[from_curr] if from_curr != 'EUR' \
            else value
        converted = value_in_eur*cls.__rates[to_curr]
        return converted
