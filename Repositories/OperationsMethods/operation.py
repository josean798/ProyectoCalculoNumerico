from abc import ABC, abstractmethod

class Operation(ABC):    
    def __init__(self):
        pass
    
    @staticmethod
    def validateDecimal(decInt):
        if not isinstance(decInt, (int, float)):
            raise TypeError("El valor decimal debe ser numérico")
            
    @staticmethod
    def validateBinary(binaryStr):
        if not isinstance(binaryStr, str):
            raise TypeError("El valor binario debe ser una cadena de texto")
        if not all(c in '01-' for c in binaryStr):
            raise ValueError("El valor binario solo puede contener 0 y 1")
    
    @staticmethod
    def validateHexadecimal(hexStr):
        if not isinstance(hexStr, str):
            raise TypeError("El valor hexadecimal debe ser una cadena de texto")
        if not all(c.upper() in '0123456789ABCDEF-' for c in hexStr):
            raise ValueError("El valor hexadecimal contiene caracteres no válidos")
    
    @abstractmethod
    def addition(self, value1, value2):
        pass
    
    @abstractmethod
    def substraction(self, value1, value2):
        pass
    
    @abstractmethod
    def product(self, value1, value2):
        pass

    @abstractmethod
    def division(self, value1, value2):
        pass