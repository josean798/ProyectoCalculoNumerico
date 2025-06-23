from Error import Error

class RelativeError(Error):
    __aproxValue = None
    def __init__(self, value, aproxValue):
        if not isinstance(value, (int, float)) or not isinstance(aproxValue, (int, float)):
            raise TypeError("Error: Los valores deben ser números.")
        super().__init__(value)
        self.__aproxValue = aproxValue

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Error: El valor debe ser un número.")
        self._value = value
    
    @property
    def aproxValue(self):
        return self.__aproxValue
    
    @aproxValue.setter
    def aproxValue(self, aproxValue):
        if not isinstance(aproxValue, (int, float)):
            raise TypeError("Error: El valor aproximado debe ser un número.")
        self.__aproxValue = aproxValue
    
    def calculateError(self):
        relError = abs(self._value - self.__aproxValue) / abs(self._value)
        return relError