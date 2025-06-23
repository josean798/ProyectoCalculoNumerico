from Error import Error

class RoundError(Error):
    __roundValue = None
    def __init__(self, value, roundNum=0):
        if roundNum < 0:
            raise ValueError("Error: El valor de redondeo no puede ser negativo.")
        if not isinstance(roundNum, int):
            raise TypeError("Error: El valor de redondeo debe ser un entero.")
        if not isinstance(value, (int, float)):
            raise TypeError("Error: El valor debe ser un número.")
        super().__init__(value)
        self.__roundNum = roundNum
        self.__roundValue = round(value, roundNum)

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Error: El valor debe ser un número.")
        self._value = value

    @property
    def roundNum(self):
        return self.__roundNum
    
    @roundNum.setter
    def roundNum(self, roundNum):
        if not isinstance(roundNum, int) or roundNum < 0:
            raise TypeError("Error: El valor de redondeo debe ser un entero no negativo.")
        self.__roundNum = roundNum
        self.__roundValue = round(self._value, roundNum)

    @property
    def roundValue(self):
        return self.__roundValue
    
    @roundValue.setter
    def roundValue(self, roundValue):
        if not isinstance(roundValue, (int, float)):
            raise TypeError("Error: El valor redondeado debe ser un número.")
        self.__roundValue = roundValue
    
    def calculateError(self):
        roundError = abs(self._value - self.roundValue)
        return roundError