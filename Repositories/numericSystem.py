import numpy as np

class numericSystem:
    """
    Clase para identificar y validar sistemas numéricos (Decimal, Binario, Hexadecimal).

    Atributos:
        __number (str): El número a analizar.
        __systems (np.ndarray): Sistemas numéricos posibles para el número.
        __isNegative (bool): Indica si el número es negativo.
    """

    __number = 0
    __systems = (np.array([]))
    __isNegative = False

    def __init__(self, number):
        """
        Inicializa un objeto numericSystem.

        Args:
            number (str): El número a analizar.

        Raises:
            ValueError: Si el input no es un string o no es válido.
        """
        if not isinstance(number, str):
            raise ValueError("El input debe ser un string")
        self.__number = number
        self.__isNegative = False
        self.__systems
        self.validateNumber()
        self.whichSystemIs()

    def validateNumber(self):
        """
        Valida que el número sea un string válido para los sistemas numéricos.

        Raises:
            ValueError: Si el número es vacío, tiene caracteres inválidos, o formato incorrecto.
        """
        if self.__number.strip() is None or self.__number.strip() == "":
            raise ValueError("El número no puede ser vacio.")

        if len(self.__number) > 0 and self.__number[0] == "-":
            self.__number = self.__number[1:]
            self.__isNegative = True

        chars = np.array(list(self.__number))
        validChars = np.array(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", ".", ",", "-"])
        validPontingCont = 0
        contMinus = 0
        for char in chars:
            if char == "." or char == ",":
                validPontingCont += 1
            if char == "-":
                contMinus += 1
            if char not in validChars:
                raise ValueError("Caracteres no válidos. Use dígitos 0-9 y/o letras A-F")
        if validPontingCont > 1 or contMinus > 0:
            raise ValueError("El número no puede tener más de un punto decimal, coma o negativo.")

        if len(self.__number) > 0 and (self.__number[0] == "," or self.__number[0] == "."):
            raise ValueError("El número no puede empezar con un punto decimal o coma.")

        if len(self.__number) > 0 and (self.__number[-1] == "," or self.__number[-1] == "."):
            raise ValueError("El número no puede terminar con un punto decimal o coma.")

    def whichSystemIs(self):
        """
        Determina los sistemas numéricos posibles para el número.

        Returns:
            np.ndarray: Arreglo con los sistemas posibles ("Decimal", "Binario", "Hexadecimal").
        """
        chars = np.array(list(self.__number))
        letters = np.array(["A", "B", "C", "D", "E", "F"])
        for char in chars:
            if char in letters:
                self.__systems = np.array(["Hexadecimal"])
                return self.__systems

        for char in chars:
            if char not in ["0", "1", ",", "."]:
                self.__systems = np.array(["Decimal", "Hexadecimal"])
                return self.__systems

        self.__systems = np.array(["Decimal", "Binario", "Hexadecimal"])
        return self.__systems

    def getNumber(self):
        """
        Devuelve el número almacenado, incluyendo el signo negativo si corresponde.

        Returns:
            str: El número.
        """
        if self.__isNegative == True:
            self.__number = "-" + self.__number
        return self.__number

    def setNumber(self, number):
        """
        Asigna un nuevo número y lo valida.

        Args:
            number (str): El nuevo número.

        Raises:
            ValueError: Si el número no es un string válido.
        """
        if not isinstance(number, str):
            raise ValueError("El numero debe ser un string")
        self.__number = number
        self.validateNumber()

    def getSystems(self):
        """
        Devuelve los sistemas numéricos posibles.

        Returns:
            np.ndarray: Sistemas numéricos posibles.
        """
        return self.__systems

    def setSystems(self, systems):
        """
        Asigna los sistemas numéricos posibles.

        Args:
            systems (list o np.ndarray): Sistemas a asignar.

        Raises:
            ValueError: Si el argumento no es un arreglo numpy o lista.
        """
        if not isinstance(systems, np.ndarray) and not isinstance(systems, list):
            raise ValueError("Los sistemas deben ser un arreglo numpy")
        self.__systems = np.array(systems)