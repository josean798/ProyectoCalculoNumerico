class translator:
    """
    Clase para validar y traducir números hexadecimales a decimales.

    Atributos:
        __num (str): Número en formato string (puede ser hexadecimal o decimal).

    Métodos:
        validateNum(): Valida que el número solo contenga caracteres hexadecimales válidos.
        isHexadecimal(): Determina si el número contiene caracteres hexadecimales (A-F).
        translate(): Convierte el número hexadecimal a decimal si corresponde.
        getNumber(): Devuelve el número actual (como string).
    """

    __num=""

    def __init__(self, number):
        """
        Inicializa la clase translator.

        Args:
            number (str): Número a validar y traducir.

        Raises:
            ValueError: Si el input no es un string o contiene caracteres inválidos.
        """
        if not isinstance(number, str):
            raise ValueError("El input debe ser un string")
        self.__num = number
        self.validateNum()

    def validateNum(self):
        """
        Valida que el número solo contenga caracteres válidos para hexadecimal.

        Raises:
            ValueError: Si el número contiene caracteres no permitidos.
        """
        valid_chars = set("0123456789abcdefABCDEF,.")
        if not all(char in valid_chars for char in self.__num):
            raise ValueError("El input debe ser un número hexadecimal válido")

    def isHexadecimal(self):
        """
        Determina si el número contiene letras hexadecimales (A-F).

        Returns:
            bool: True si el número es hexadecimal, False si es solo decimal.
        """
        return any(c in "abcdefABCDEF" for c in self.__num)

    def translate(self):
        """
        Convierte el número hexadecimal a decimal si contiene letras hexadecimales.
        Si el número ya es decimal, no realiza ninguna acción.
        """
        if not self.isHexadecimal():
            return
        conter = 0
        newNum = 0
        for number in self.__num[::-1]:
            if number == "A" or number == "a":
                number = 10
            elif number == "B" or number == "b":
                number = 11
            elif number == "C" or number == "c":
                number = 12
            elif number == "D" or number == "d":
                number = 13
            elif number == "E" or number == "e":
                number = 14
            elif number == "F" or number == "f":
                number = 15
            newNum += int(number) * (16 ** conter)
            conter += 1
        self.__num = str(newNum)

    def getNumber(self):
        """
        Devuelve el número actual (como string).

        Returns:
            str: Número actual (puede ser decimal o hexadecimal).
        """
        return self.__num