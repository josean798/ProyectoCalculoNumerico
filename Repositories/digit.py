import numpy as np
from Structure.myReplace import myReplace

class Digit:
    """
    Clase para representar y validar un número en diferentes sistemas numéricos,
    y calcular sus cifras significativas.

    Atributos:
        __number (str): El número a analizar, como cadena.
        __System (str): El sistema numérico ("Decimal", "Hexadecimal" o "Binario").
        __significantFigures (str): Las cifras significativas calculadas.
    """

    __number = ""
    __System = ""
    __significantFigures = ""

    def __init__(self, num, System):
        """
        Inicializa un objeto Digit.

        Args:
            num (str): El número a analizar.
            System (str): El sistema numérico ("Decimal", "Hexadecimal" o "Binario").

        Raises:
            ValueError: Si el número o el sistema no son válidos.
        """
        self.__number = num
        self.__System = System
        self.__significantFigures
        self.validateString()
        self.validateSystem()
        self.countSigFigs()

    def validateString(self):
        """
        Valida que el número sea una cadena válida para el sistema numérico.

        Raises:
            ValueError: Si el número no es válido (caracteres inválidos, formato incorrecto, etc.).
        """
        if not isinstance(self.__number, (str)):
            raise ValueError("El número debe ser un entero, flotante o cadena de texto.")
        if self.__number == "" or self.__number is None:
            raise ValueError("El número no puede ser una cadena vacía.")
        chars = np.array(list(self.__number))
        validChars = np.array(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "a", "b", "c", "d", "e", "f", ".", "-", ","])
        validPontingCont = 0
        contMinus = 0
        for char in chars:
            if char == "." or char == ",":
                validPontingCont += 1
            if char == "-":
                contMinus += 1
            if char not in validChars:
                raise ValueError("Caracteres no válidos. Use dígitos 0-9 y/o letras A-F")
        if validPontingCont > 1 or contMinus > 1:
            raise ValueError("El número no puede tener más de un punto decimal, coma o negativo.")
        if len(self.__number) > 0 and self.__number[0] != "-" and contMinus > 0:
            raise ValueError("El signo negativo debe ir al inicio del número.")
        if len(self.__number) > 0 and (self.__number[0] == "," or self.__number[0] == "."):
            raise ValueError("El número no puede empezar con un punto decimal o coma.")
        if len(self.__number) > 0 and (self.__number[-1] == "," or self.__number[-1] == "."):
            raise ValueError("El número no puede terminar con un punto decimal o coma.")

    def validateSystem(self):
        """
        Valida que el sistema numérico sea correcto y que el número sea válido para ese sistema.

        Raises:
            ValueError: Si el sistema o el número no son válidos para el sistema especificado.
        """
        if not isinstance(self.__System, str):
            raise ValueError("El sistema debe ser un string.")
        if self.__System == "" or self.__System is None:
            raise ValueError("El sistema no puede ser una cadena vacía.")
        validSystems = np.array(["Decimal", "Hexadecimal", "Binario"])
        if self.__System not in validSystems:
            raise ValueError("El sistema debe ser Decimal, Hexadecimal o Binario.")
        if self.__System == "Decimal":
            chars = np.array(list(self.__number))
            for char in chars:
                if char not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ",", "-"]:
                    raise ValueError("El número no es válido en el sistema Decimal.")
        if self.__System == "Hexadecimal":
            if "-" in self.__number:
                raise ValueError("No se permiten números negativos en el sistema Hexadecimal.")        
        if self.__System == "Binario":
            chars = np.array(list(self.__number))
            for char in chars:
                if char not in ["0", "1", ".", ","]:
                    raise ValueError("El número no es válido en el sistema Binario.")

    def countSigFigs(self):
        """
        Calcula las cifras significativas del número según el sistema numérico.
        """
        if self.__System == "Hexadecimal":
            self.__significantFigures = "NP"
        elif self.__System == "Decimal":
            if "," in self.__number:
                replacer = myReplace(self.__number)
                self.__number = replacer.getReplace(",", ".")
            self.ifIsDecimal()
        elif self.__System == "Binario":
            if "," in self.__number:
                replacer = myReplace(self.__number)
                self.__number = replacer.getReplace(",", ".")
            self.ifIsBinario()

    def ifIsDecimal(self):
        """
        Calcula las cifras significativas si el número es decimal.
        """
        if len(self.__number) > 0 and self.__number[0] == "-":
            self.__number = self.__number[1:]
        if float(self.__number) == 0:
            self.__significantFigures = "1"
            return
        if "." in self.__number:
            parts = np.array(self.__number.split("."))
            integerPart = parts[0].lstrip("0")
            decimalPart = parts[1]
            if integerPart == "":
                contAux = len(parts[1].lstrip("0"))
                decimalPart = parts[1].lstrip("0").rstrip("0")
                self.__significantFigures = str(len(decimalPart)) +" o " + str(contAux)
            elif integerPart != "":
                decimalPart = parts[1].lstrip("0").rstrip("0")
                if decimalPart=="":
                    if len(integerPart.rstrip("0")) == len(integerPart):
                        self.__significantFigures = str(len(integerPart))
                    else:
                        self.__significantFigures = str(len(integerPart.rstrip("0"))) + " o " + str(len(integerPart))
                elif decimalPart != "":
                    self.__significantFigures = str(len(integerPart) + len(decimalPart))
        else:
            integerPart = self.__number.lstrip("0")
            if integerPart=="":
                self.__significantFigures = "1"
                return
            else:
                if (len(integerPart.rstrip("0")) == len(integerPart)):
                    self.__significantFigures = str(len(integerPart))
                else:
                    self.__significantFigures = str(len(integerPart.rstrip("0"))) + " o " + str(len(integerPart))

    def ifIsBinario(self):
        """
        Calcula las cifras significativas si el número es binario.
        """
        if len(self.__number) > 0 and self.__number[0] == "-":
            self.__number = self.__number[1:]
        if float(self.__number) == 0:
            self.__significantFigures = "1"
            return
        if "." in self.__number:
            parts = np.array(self.__number.split("."))
            integerPart = parts[0].lstrip("0")
            if integerPart == "":
                decimalPart = parts[1].lstrip("0")
                if decimalPart == "":
                    self.__significantFigures = "1"
                    return
                self.__significantFigures = str(len(decimalPart))
            elif integerPart != "":
                decimalPart = parts[1]
                if decimalPart=="":
                    self.__significantFigures = str(len(integerPart.rstrip("0")))
                elif decimalPart != "":
                    self.__significantFigures = str(len(integerPart.rstrip("0"))+ len(decimalPart))
        else:
            integerPart = self.__number.lstrip("0").rstrip("0")
            if integerPart == "":
                self.__significantFigures = "1"
                return
            else:
                self.__significantFigures = str(len(integerPart))

    def getNumber(self):
        """
        Devuelve el número almacenado.

        Returns:
            str: El número.
        """
        return self.__number

    def setNumber(self, num):
        """
        Asigna un nuevo número y lo valida.

        Args:
            num (str): El nuevo número.

        Raises:
            ValueError: Si el número no es un string válido.
        """
        if not isinstance(num, str):
            raise ValueError("El número debe ser un string")
        self.__number = num
        self.validateString()

    def getSystem(self):
        """
        Devuelve el sistema numérico.

        Returns:
            str: El sistema numérico.
        """
        return self.__System

    def setSystem(self, System):
        """
        Asigna un nuevo sistema numérico.

        Args:
            System (str): El sistema numérico ("Decimal", "Hexadecimal" o "Binario").

        Raises:
            ValueError: Si el sistema no es válido.
        """
        validSystems = np.array(["Decimal", "Hexadecimal", "Binario"])
        if System not in validSystems:
            raise ValueError("El sistema debe ser Decimal, Hexadecimal o Binario.")
        self.__System = System

    def getSignificantFigures(self):
        """
        Devuelve las cifras significativas calculadas.

        Returns:
            str: Las cifras significativas.
        """
        return self.__significantFigures

    def setSignificantFigures(self, sig_figs):
        """
        Asigna las cifras significativas.

        Args:
            sig_figs (str): Las cifras significativas.

        Raises:
            ValueError: Si las cifras no son válidas.
        """
        if not isinstance(sig_figs, str):
            raise ValueError("Las cifras significativas deben ser un string")
        validSigFigures = np.array(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        for char in sig_figs:
            if char not in validSigFigures:
                raise ValueError("Las cifras significativas deben ser un número entre 0 y 9.")
        self.__significantFigures = sig_figs