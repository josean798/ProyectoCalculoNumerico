class Hexadecimal:
    """
    Clase para realizar operaciones elementales en números hexadecimales.

    Métodos:
        addition(value1): Suma 1 al número hexadecimal dado.
        substraction(value1): Resta 1 al número hexadecimal dado.
        product(value1): Multiplica el número hexadecimal por 1.
        division(value1): Divide el número hexadecimal entre 1.
        hexAdd(a, b): Suma dos números hexadecimales.
        hexMultiplyDigit(value1, digit): Multiplica un número hexadecimal por un dígito hexadecimal.
    """

    def __init__(self):
        """Inicializa la clase Hexadecimal."""
        pass

    def addition(self, value1):
        """
        Suma 1 al número hexadecimal dado.

        Args:
            value1 (str): Número hexadecimal como cadena.

        Returns:
            str: Resultado de la suma en hexadecimal.
        """
        if not value1:
            return '1'
        digits = '0123456789ABCDEF'
        carry = 1
        result = ''
        for i in range(len(value1)-1, -1, -1):
            d = value1[i].upper()
            idx = digits.find(d)
            newIdx = idx + carry
            if newIdx < 16:
                result = digits[newIdx] + result
                carry = 0
            else:
                result = '0' + result
                carry = 1
        if carry == 1:
            result = '1' + result
        return result.lstrip('0') or '0'

    def substraction(self, value1):
        """
        Resta 1 al número hexadecimal dado.

        Args:
            value1 (str): Número hexadecimal como cadena.

        Returns:
            str: Resultado de la resta en hexadecimal.
        """
        if value1 == '0':
            return '-1'
        digits = '0123456789ABCDEF'
        borrow = 1
        result = ''
        for i in range(len(value1)-1, -1, -1):
            d = value1[i].upper()
            idx = digits.find(d)
            newIdx = idx - borrow
            if newIdx >= 0:
                result = digits[newIdx] + result
                borrow = 0
            else:
                result = 'F' + result
                borrow = 1
        result = result.lstrip('0')
        return result if result else '0'

        
    def product(self, value1):
        """
        Multiplica el número hexadecimal por 1.

        Args:
            value1 (str): Número hexadecimal como cadena.

        Returns:
            str: Resultado de la multiplicación en hexadecimal.

        Raises:
            ValueError: Si el valor no es una cadena hexadecimal válida.
        """
        value2 = '1'
        digits = '0123456789ABCDEF'
        if not all(c.upper() in digits for c in value1) or not all(c.upper() in digits for c in value2):
            raise ValueError("Solo se aceptan cadenas hexadecimales.")

        if value2.strip('0') == '':
            return '0'

        result = '0'
        for i, digit in enumerate(reversed(value2.upper())):
            if digit != '0':
                parc = self.hexMultiplyDigit(value1, digit)
                parc += '0' * i
                result = self.hexAdd(result, parc)
        return result.lstrip('0') or '0'

    def hexAdd(self, a, b):
        """
        Suma dos números hexadecimales.

        Args:
            a (str): Primer número hexadecimal.
            b (str): Segundo número hexadecimal.

        Returns:
            str: Resultado de la suma en hexadecimal.
        """
        digits = '0123456789ABCDEF'
        maxLen = max(len(a), len(b))
        a = a.zfill(maxLen)
        b = b.zfill(maxLen)
        carry = 0
        result = ''
        for i in range(maxLen - 1, -1, -1):
            total = digits.find(a[i].upper()) + digits.find(b[i].upper()) + carry
            result = digits[total % 16] + result
            carry = total // 16
        if carry:
            result = digits[carry] + result
        return result.lstrip('0') or '0'

    def hexMultiplyDigit(self, value1, digit):
        """
        Multiplica un número hexadecimal por un dígito hexadecimal.

        Args:
            value1 (str): Número hexadecimal como cadena.
            digit (str): Dígito hexadecimal.

        Returns:
            str: Resultado de la multiplicación en hexadecimal.
        """
        digits = '0123456789ABCDEF'
        d = digits.find(digit.upper())
        if d == 0:
            return '0'
        carry = 0
        result = ''
        for v in reversed(value1.upper()):
            prod = digits.find(v) * d + carry
            result = digits[prod % 16] + result
            carry = prod // 16
        if carry:
            result = digits[carry] + result
        return result.lstrip('0') or '0'
    
    def division(self, value1):
        """
        Divide el número hexadecimal entre 1.

        Args:
            value1 (str): Número hexadecimal como cadena.

        Returns:
            str: Cociente de la división en hexadecimal.

        Raises:
            ValueError: Si el divisor es cero.
        """
        digits = '0123456789ABCDEF'
        divisorHex = '1'  
        divisor = 0
        for c in divisorHex.upper():
            divisor = divisor * 16 + digits.find(c)
        if divisor == 0:
            raise ValueError("Divisor no puede ser cero.")

        quotient = ''
        remainder = 0

        for d in value1.upper():
            num = remainder * 16 + digits.find(d)
            qDigit = num // divisor
            remainder = num % divisor
            quotient += digits[qDigit]

        quotient = quotient.lstrip('0') or '0'
        return quotient