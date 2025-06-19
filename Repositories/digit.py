import numpy as np

class Digit:

    __number = ""
    __System = ""
    __significantFigures = ""

    def __init__(self, num, System):
        self.__number = num
        self.__System = System
        self.__significantFigures
        self.validateString()
        self.validateSystem()
        self.count_sig_figs()

    def validateString(self):

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
        
        if (not self.__number.startswith("-")) and contMinus > 0:
            raise ValueError("El signo negativo debe ir al inicio del número.")
        
        if self.__number.startswith(",") or self.__number.startswith("."):
            raise ValueError("El número no puede empezar con un punto decimal o coma.")
        
        if self.__number.endswith(",") or self.__number.endswith("."):
            raise ValueError("El número no puede terminar con un punto decimal o coma.")

        
    def validateSystem(self):

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
            
        if self.__System == "Binario":
            chars = np.array(list(self.__number))
            for char in chars:
                if char not in ["0", "1", ".", ",", "-"]:
                    raise ValueError("El número no es válido en el sistema Binario.")


    def count_sig_figs(self):

        if self.__System == "Hexadecimal":
            self.__significantFigures = "NP"
        elif self.__System == "Decimal":
            if "," in self.__number:
                self.__number = self.__number.replace(",", ".")
            self.ifIsDecimal()
        elif self.__System == "Binario":
            if "," in self.__number:
                self.__number = self.__number.replace(",", ".")
            self.ifIsBinario()
    

    def ifIsDecimal(self):

        if self.__number.startswith("-"):
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

        if self.__number.startswith("-"):
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
        return self.__number
    
    def setNumber(self, num):
        if not isinstance(num, str):
            raise ValueError("El número debe ser un string")
        self.__number = num
        self.validateString()

    def getSystem(self):
        return self.__System
    
    def setSystem(self, System):
        validSystems = np.array(["Decimal", "Hexadecimal", "Binario"])
        if System not in validSystems:
            raise ValueError("El sistema debe ser Decimal, Hexadecimal o Binario.")
        self.__System = System

    def getSignificantFigures(self):
        return self.__significantFigures
    
    def setSignificantFigures(self, sig_figs):
        if not isinstance(sig_figs, str):
            raise ValueError("Las cifras significativas deben ser un string")
        validSigFigures = np.array(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        for char in sig_figs:
            if char not in validSigFigures:
                raise ValueError("Las cifras significativas deben ser un número entre 0 y 9.")
        self.__significantFigures = sig_figs


