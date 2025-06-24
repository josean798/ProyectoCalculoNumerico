from Repositories.OperationsMethods.operation import Operation

class Decimal(Operation):
    def __init__(self):
        pass
    
    def addition(self, value1):
        self.validateDecimal(value1)
        return value1 + 1
    
    def substraction(self, value1):
        self.validateDecimal(value1)
        return value1 - 1
    
    
    def product(self, value1):
        self.validateDecimal(value1)
        multiplicador=1
        resultado = 0
        negativo = (multiplicador < 0)
        for _ in range(abs(multiplicador)):
            resultado += value1
        return -resultado if negativo else resultado

    def division(self, value1):
        if isinstance(value1, float) and not value1.is_integer():
            value1 = round(value1)
        divisor = 1
        self.validateDecimal(value1)
        digits = '0123456789'
        if isinstance(divisor, str):
            divisor = int(divisor)
        if divisor == 0:
            raise ValueError("Divisor no puede ser cero.")

        value_str = str(abs(value1))
        quotient = ''
        remainder = 0

        for d in value_str:
            remainder = remainder * 10 + digits.find(d)
            qDigit = remainder // divisor
            remainder = remainder % divisor
            quotient += digits[qDigit]

        quotient = quotient.lstrip('0') or '0'
        if value1 < 0:
            quotient = '-' + quotient

        return int(quotient)