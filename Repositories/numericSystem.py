import numpy as np

class numericSystem: 

    __number = 0
    __systems = (np.array([]))
    __isNegative = False

    
    def __init__(self, number):

        if not isinstance(number, str):
            raise ValueError("El input debe ser un string")
        self.__number = number
        self.__isNegative = False
        self.__systems
        self.validateNumber()
        self.whichSystemIs()

    def validateNumber(self):
        
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
        if self.__isNegative == True:
            self.__number = "-" + self.__number
        return self.__number

    def setNumber(self, number):
        if not isinstance(number, str):
            raise ValueError("El numero debe ser un string")
        self.__number = number
        self.validateNumber()

    def getSystems(self):
        return self.__systems
    
    def setSystems(self, systems):
        if not isinstance(systems, np.ndarray) and not isinstance(systems, list):
            raise ValueError("Los sistemas deben ser un arreglo numpy")
        self.__systems = np.array(systems)