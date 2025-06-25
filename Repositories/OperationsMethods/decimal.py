class Decimal():
    """
    Clase para realizar operaciones elementales en números decimales.

    Métodos:
        addition(value1): Suma 1 al número decimal dado.
        substraction(value1): Resta 1 al número decimal dado.
        product(value1): Multiplica el número decimal por 1.
        division(value1): Divide el número decimal entre 1.
    """
    
    def __init__(self):
        """Inicializa la clase Decimal."""
        pass

    def addition(self, value1):
        """
        Suma 1 al número decimal dado.

        Args:
            value1 (int|float): Número decimal.

        Returns:
            int|float: Resultado de la suma.

        Raises:
            TypeError: Si el valor no es numérico.
        """
        if not isinstance(value1, (int, float)):
            raise TypeError("El valor decimal debe ser numérico")
        return value1 + 1
    
    def substraction(self, value1):
        """
        Resta 1 al número decimal dado.

        Args:
            value1 (int|float): Número decimal.

        Returns:
            int|float: Resultado de la resta.

        Raises:
            TypeError: Si el valor no es numérico.
        """
        if not isinstance(value1, (int, float)):
            raise TypeError("El valor decimal debe ser numérico")
        return value1 - 1
    
    
    def product(self, value1):
        """
        Multiplica el número decimal por 1.

        Args:
            value1 (int|float): Número decimal.

        Returns:
            int|float: Resultado de la multiplicación.

        Raises:
            TypeError: Si el valor no es numérico.
        """
        if not isinstance(value1, (int, float)):
            raise TypeError("El valor decimal debe ser numérico")
        multiplicador=1
        resultado = 0
        negativo = (multiplicador < 0)
        for _ in range(abs(multiplicador)):
            resultado += value1
        return -resultado if negativo else resultado

    def division(self, value1):
        """
        Divide el número decimal entre 1.

        Args:
            value1 (int|float): Número decimal.

        Returns:
            int: Cociente de la división.

        Raises:
            ValueError: Si el divisor es cero.
        """
        if isinstance(value1, float) and not value1.is_integer():
            value1 = round(value1)
        divisor = 1
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