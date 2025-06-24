from Error import Error

class PropagationError(Error):
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Error: El valor debe ser un número.")
        super().__init__(value)

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Error: El valor debe ser un número.")
        self._value = value
    
    @staticmethod
    def _operation(value):
        return (value + 0.1) * 3 - 0.3

    def calculateError(self):
        realValue = self._value * 3
        errorValue = self._operation(self._value)
        propError = abs(realValue - errorValue)
        return propError