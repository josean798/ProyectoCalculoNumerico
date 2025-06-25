class Convertor:
    """
    Clase para convertir números entre sistemas binario, decimal y hexadecimal.
    
    Métodos:
        binaryToDecimal(iniValue): Convierte un número binario a decimal.
        hexadecimalToDecimal(iniValue): Convierte un número hexadecimal a decimal.
        decimalToBinary(iniValue): Convierte un número decimal a binario.
        decimalToHexadecimal(iniValue): Convierte un número decimal a hexadecimal.
    """
    
    def __init__(self):
        """Inicializa la clase Convertor."""
        pass

    @staticmethod
    def binaryToDecimal(iniValue):
        """
        Convierte un número binario a decimal.

        Args:
            iniValue (str): Número binario como cadena (puede tener signo negativo).

        Returns:
            int: Valor decimal correspondiente.
        """
        sign = 1
        if iniValue.startswith('-'):
            sign = -1
            iniValue = iniValue[1:]

        length = len(iniValue)
        value = 0
        for i in range(length):
            if iniValue[i] == '1':
                value += 2 ** (length - i - 1)
        return value * sign
    
    @staticmethod
    def hexadecimalToDecimal(iniValue):
        """
        Convierte un número hexadecimal a decimal.

        Args:
            iniValue (str): Número hexadecimal como cadena (puede tener signo negativo).

        Returns:
            int: Valor decimal correspondiente.
        """
        sign = 1
        if iniValue.startswith('-'):
            sign = -1
            iniValue = iniValue[1:]
    
        length = len(iniValue)
        value = 0
        pos = 0
    
        for i in iniValue:
            power = length - pos - 1 
            if i.isdigit():
                value += int(i) * (16 ** power)
            else:
                upperi = i.upper() 
                if upperi == 'A':
                    value += 10 * (16 ** power)
                elif upperi == 'B':
                    value += 11 * (16 ** power)
                elif upperi == 'C':
                    value += 12 * (16 ** power)
                elif upperi == 'D':
                    value += 13 * (16 ** power)
                elif upperi == 'E':
                    value += 14 * (16 ** power)
                elif upperi == 'F':
                    value += 15 * (16 ** power)
            pos += 1
    
        return value * sign
    
    @staticmethod
    def decimalToBinary(iniValue):
        """
        Convierte un número decimal a binario.

        Args:
            iniValue (str|int): Número decimal como cadena o entero (puede tener signo negativo).

        Returns:
            str: Representación binaria del número.
        """
        sign = ''
        value = iniValue
        if isinstance(value, str):
            if value.startswith('-'):
                sign = '-'
                value = value[1:]
            value = int(value)
        elif isinstance(value, int) and value < 0:
            sign = '-'
            value = abs(value)
        binary = ''
        while value > 0:
            binary = str(value % 2) + binary
            value //= 2
        return sign + binary if binary else '0'

    @staticmethod
    def decimalToHexadecimal(iniValue):
        """
        Convierte un número decimal a hexadecimal.

        Args:
            iniValue (str|int): Número decimal como cadena o entero (puede tener signo negativo).

        Returns:
            str: Representación hexadecimal del número.
        """
        sign = ''
        value = iniValue
        if isinstance(value, str):
            if value.startswith('-'):
                sign = '-'
                value = value[1:]
            value = int(value)
        elif isinstance(value, int) and value < 0:
            sign = '-'
            value = abs(value)
        hexadecimal = ''
        while value > 0:
            remainder = value % 16
            if remainder < 10:
                hexadecimal = str(remainder) + hexadecimal
            else:
                if remainder == 10:
                    hexadecimal = 'A' + hexadecimal
                elif remainder == 11:
                    hexadecimal = 'B' + hexadecimal
                elif remainder == 12:
                    hexadecimal = 'C' + hexadecimal
                elif remainder == 13:
                    hexadecimal = 'D' + hexadecimal
                elif remainder == 14:
                    hexadecimal = 'E' + hexadecimal
                elif remainder == 15:
                    hexadecimal = 'F' + hexadecimal
            value //= 16
        return sign + hexadecimal if hexadecimal else sign + '0'