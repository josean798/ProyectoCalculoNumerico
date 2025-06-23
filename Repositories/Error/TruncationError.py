from Error import Error
import math

class TruncationError(Error):
    __n = None
    def __init__(self, value, n):
        if not isinstance(value, (int, float)) or not isinstance(n, int) or n <= 0:
            raise TypeError("Error: El valor debe ser un número y n debe ser un entero positivo.")
        super().__init__(value)
        self.__n = n

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Error: El valor debe ser un número.")
        self._value = value

    @property
    def n(self):
        return self.__n
    
    @n.setter
    def n(self, n):
        if not isinstance(n, int) or n <= 0:
            raise TypeError("Error: n debe ser un entero positivo.")
        self.__n = n
    
    @staticmethod
    def _aproxFunction(n, value):
        if n <= 0 or not isinstance(n, int):
            raise ValueError("Error: n debe ser un entero positivo.")
        if not isinstance(value, (int, float)):
            raise TypeError("Error: El valor debe ser un número.")
        sum = 0
        for i in range(n):
            sum += (-1)**i * (value**(2*i)) / math.factorial(2*i)
        return sum
    
    def calculateError(self):
        exValue = math.cos(self._value)
        truncValue = self._aproxFunction(self.__n, self._value)
        truncError = abs(exValue - truncValue)
        return truncError