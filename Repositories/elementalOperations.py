import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Repositories.OperationsMethods.decimal import Decimal
from Repositories.OperationsMethods.Hexadecimal import Hexadecimal
from Repositories.OperationsMethods.binary import Binary
from Repositories.OperationsMethods.convertor import Convertor
from Structure.myReplace import myReplace

class ElementalOperations:
    __value = None
    __System = None

    def __init__(self, value, system):
        validSystems = np.array(['Binario', 'Hexadecimal', 'Decimal'])
        if not isinstance(system, str) or system not in validSystems:
            raise ValueError("El sistema debe ser 'Decimal', 'Hexadecimal' o 'Binario'.")
        if not isinstance(value, str):
            raise TypeError("Valor debe ser una cadena de texto")
        
        self.__decimal = Decimal()
        self.__binary = Binary()
        self.__hexadecimal = Hexadecimal()
        self.__convertor = Convertor()
        self.__value = value
        self.__System = system
        self.validateNumber()
    
    def validateNumber(self):
        if self.__value.strip() is None or self.__value.strip() == "":
            raise ValueError("El número no puede ser vacio.")
        
        chars = self.__value
        validChars = chars = self.__value
        validChars = "0123456789ABCDEF.,-"
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
            raise ValueError("El número no puede tener más de un punto decimal, coma o signo negativo.")
        
        if len(self.__value) > 0 and (self.__value[0] == "," or self.__value[0] == "."):
            raise ValueError("El número no puede empezar con un punto decimal o coma.")
        
        if len(self.__value) > 0 and (self.__value[-1] == "," or self.__value[-1] == "."):
            raise ValueError("El número no puede terminar con un punto decimal o coma.")
    
    # GETTERS & SETTERS
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if not isinstance(value, str):
            raise TypeError("Valor debe ser una cadena de texto")
        self.__value = value

    @property
    def system(self):
        return self.__System
    
    @system.setter
    def system(self, system):
        validSystems = ('Binario', 'Hexadecimal', 'Decimal')
        if not isinstance(system, str) or system not in validSystems:
            raise ValueError("System debe ser 'Decimal', 'Hexadecimal' o 'Binario'")
        self.__System = system

    @staticmethod
    def cleanValue(value):
        replace = myReplace(value)
        return replace.getReplace('-', '') if '-' in value else value
    
    def binary(self):
        results = ''
        testValue = 1
        mainValue = self.cleanValue(self.__value)
        
        additionResult = self.__binary.addition(mainValue)
        substractResult = self.__binary.substraction(mainValue)
        productResult = self.__binary.product(mainValue)
        divisionResult = self.__binary.division(mainValue)

        mainValueDec = self.__convertor.binaryToDecimal(mainValue)
    
        if abs(self.__convertor.binaryToDecimal(additionResult) - (mainValueDec + testValue)) < 1e-6:
            results += '+'
        else:
            results += ' '
        
        if abs(self.__convertor.binaryToDecimal(substractResult) - (mainValueDec - testValue)) < 1e-6:
            results += '-'
        else:
            results += ' '

        if abs(self.__convertor.binaryToDecimal(productResult) - (mainValueDec * testValue)) < 1e-6:
            results += '*'
        else:
            results += ' '
        
        if abs(self.__convertor.binaryToDecimal(divisionResult) - (mainValueDec // testValue)) < 1e-6:
            results += '/'
        else:
            results += ' '
        
        return results
    
    def hexadecimal(self):
        results = ''
        testValue = 1
        mainValue = self.cleanValue(self.__value)
        mainValue = str(mainValue).split('.')[0].split(',')[0]

        additionResult = self.__hexadecimal.addition(mainValue)
        substractResult = self.__hexadecimal.substraction(mainValue)
        productResult = self.__hexadecimal.product(mainValue)
        divisionResult = self.__hexadecimal.division(mainValue)

        mainValueDec = self.__convertor.hexadecimalToDecimal(mainValue)


        if abs(self.__convertor.hexadecimalToDecimal(additionResult) - (mainValueDec + testValue)) < 1e-6:
            results += '+'
        else:
            results += ' '
        
        if abs(self.__convertor.hexadecimalToDecimal(substractResult) - (mainValueDec - testValue)) < 1e-6:
            results += '-'
        else:
            results += ' '

        if abs(self.__convertor.hexadecimalToDecimal(productResult) - (mainValueDec * testValue)) < 1e-6:
            results += '*'
        else:
            results += ' '
        
        if abs(self.__convertor.hexadecimalToDecimal(divisionResult) - (mainValueDec // testValue)) < 1e-6:
            results += '/'
        else:
            results += ' '
        
        return results
    
    def decimal(self):
        
        results = ''
        testValue = 1
        if ',' in self.__value:
            replace = myReplace(self.__value)
            mainValue = replace.getReplace(',','.')
            mainValue = float(mainValue)
        else:
            mainValue = float(self.__value)

        if mainValue == int(mainValue):
            mainValue = int(mainValue)

        additionResult = self.__decimal.addition(mainValue)
        substractResult = self.__decimal.substraction(mainValue)
        productResult = self.__decimal.product(mainValue)
        divisionResult = self.__decimal.division(mainValue)

        

        if abs(additionResult - (mainValue + testValue)) < 1e-6:
            results += '+'
        else:
            results += ' '

        if abs(substractResult - (mainValue - testValue)) < 1e-6:
            results += '-'
        else:
            results += ' '

        if abs(productResult - (mainValue * testValue)) < 1e-6:
            results += '*'
        else:
            results += ' '

        if round(divisionResult) == round(mainValue / testValue):
            results += '/'
        else:
            results += ' '
        
        return results
    
    def finalResult(self):
        if self.__System == 'Binario':
            return self.binary()
        elif self.__System == 'Hexadecimal':
            return self.hexadecimal()
        elif self.__System == 'Decimal':
            return self.decimal()



