class Error:
    _value = None
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Error: El valor debe ser un número.")
        self._value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Error: El valor debe ser un número.")
        self._value = value

    def calculateError(self):
        pass