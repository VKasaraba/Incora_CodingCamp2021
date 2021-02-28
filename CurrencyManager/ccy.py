from currency_converter import CurrencyConverter
import operator


class Ccy:
    # queue to display the result in all currencies used by user
    __currencies_to_display = []

    def __init__(self, value, currency: str):
        if type(value) in [float, int]:
            self.value = value
        else:
            try:
                self.value = float(value)
                self.value = int(
                    self.value) if self.value.is_integer() else self.value
            except ValueError:
                raise ValueError('Please put a number as a money value')
        self.currency = currency

    def __str__(self):
        initial_currency = self.currency
        initial_value = self.value
        result = f'{round(initial_value, 2)} {initial_currency}'
        seen_currs = [initial_currency]
        # checks if the user used values in different currencies
        # and prints the result in all of those currencies. Example:
        # 1 UAH + 1 USD + 1 LTL = 38.41 UAH  or  1.37 USD  or  4.06 LTL
        while self.__currencies_to_display:
            other_currency = self.__currencies_to_display.pop(0)
            if other_currency not in seen_currs:
                other_value = CurrencyConverter.convert(
                    initial_value, initial_currency, other_currency)
                seen_currs.append(other_currency)
                result += f'  or  {round(other_value, 2)} {other_currency}'
        return result

    @classmethod
    def __ariphmetic_helper(cls, param1, param2, operation):
        ''' Is used by magic methods for arithmetical operations '''
        # magic functions make sure param1 is always a Ccy object
        cls.__currencies_to_display.append(param1.currency)
        if isinstance(param2, Ccy):
            cls.__currencies_to_display.append(param2.currency)
            if param1.currency == param2.currency:
                result_value = operation(param1.value, param2.value)
                if operation is operator.truediv:
                    cls.__currencies_to_display = []
                    return result_value
                return Ccy(result_value, param1.currency)
            else:
                value1 = param1.value
                value2 = CurrencyConverter.convert(
                    param2.value, param2.currency, param1.currency)
                result_value = operation(value1, value2)
                if operation is operator.truediv:
                    cls.__currencies_to_display = []
                    return result_value
                return Ccy(result_value, param1.currency)
        elif type(param2) in [float, int]:
            return Ccy(operation(param1.value, param2), param1.currency)
        else:
            try:
                return Ccy(operation(param1.value, float(param2)),
                           param1.currency)
            except ValueError:
                raise ValueError('Args must be numbers or Ccy class objects')

    def __add__(self, other):
        return Ccy.__ariphmetic_helper(self, other, operator.add)

    def __radd__(self, other):
        return Ccy.__ariphmetic_helper(self, other, operator.add)

    def __sub__(self, other):
        return Ccy.__ariphmetic_helper(self, other, operator.sub)

    def __rsub__(self, other):
        return Ccy.__ariphmetic_helper(self, other, operator.sub) * (-1)

    def __mul__(self, other):
        return Ccy.__ariphmetic_helper(self, other, operator.mul)

    def __rmul__(self, other):
        return Ccy.__ariphmetic_helper(self, other, operator.mul)

    def __truediv__(self, other):
        try:
            return Ccy.__ariphmetic_helper(self, other, operator.truediv)
        except ZeroDivisionError:
            raise ValueError('Cannot devide by zero')

    def __rtruediv__(self, other):
        raise ValueError("Doesn't make sense to divide a number by money")

    def __floordiv__(self, other):
        try:
            return Ccy.__ariphmetic_helper(self, other, operator.floordiv)
        except ZeroDivisionError:
            raise ValueError('Cannot devide by zero')

    def __rfloordiv__(self, other):
        raise ValueError("Doesn't make sense to divide a number by money")
