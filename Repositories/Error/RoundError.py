from Error import Error

class RoundError(Error):
    """
    Clase para calcular el error de redondeo de un valor numérico.

    Hereda de:
        Error

    Atributos:
        _value (int|float): Valor original.
        __roundNum (int): Número de decimales para redondear.
        __roundValue (int|float): Valor redondeado.

    Métodos:
        calculateError(): Calcula el error de redondeo.
        value (property): Getter y setter para el valor original.
        roundNum (property): Getter y setter para el número de decimales.
        roundValue (property): Getter y setter para el valor redondeado.
    """

    __roundValue = None

    def __init__(self, value, roundNum=0):
        """
        Inicializa la clase RoundError.

        Args:
            value (int|float): Valor original.
            roundNum (int): Número de decimales para redondear (por defecto 0).

        Raises:
            ValueError: Si el valor de redondeo es negativo.
            TypeError: Si el valor de redondeo no es un entero o el valor no es numérico.
        """
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
        """
        Obtiene el valor original.

        Returns:
            int|float: Valor original.
        """
        return self._value
    
    @value.setter
    def value(self, value):
        """
        Establece el valor original.

        Args:
            value (int|float): Valor original.

        Raises:
            TypeError: Si el valor no es numérico.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Error: El valor debe ser un número.")
        self._value = value

    @property
    def roundNum(self):
        """
        Obtiene el número de decimales para redondear.

        Returns:
            int: Número de decimales.
        """
        return self.__roundNum
    
    @roundNum.setter
    def roundNum(self, roundNum):
        """
        Establece el número de decimales para redondear.

        Args:
            roundNum (int): Número de decimales.

        Raises:
            TypeError: Si el valor no es un entero no negativo.
        """
        if not isinstance(roundNum, int) or roundNum < 0:
            raise TypeError("Error: El valor de redondeo debe ser un entero no negativo.")
        self.__roundNum = roundNum
        self.__roundValue = round(self._value, roundNum)

    @property
    def roundValue(self):
        """
        Obtiene el valor redondeado.

        Returns:
            int|float: Valor redondeado.
        """
        return self.__roundValue
    
    @roundValue.setter
    def roundValue(self, roundValue):
        """
        Establece el valor redondeado.

        Args:
            roundValue (int|float): Valor redondeado.

        Raises:
            TypeError: Si el valor redondeado no es numérico.
        """
        if not isinstance(roundValue, (int, float)):
            raise TypeError("Error: El valor redondeado debe ser un número.")
        self.__roundValue = roundValue
    
    def calculateError(self):
        """
        Calcula el error de redondeo entre el valor original y el valor redondeado.

        Returns:
            float: Error de redondeo absoluto.
        """
        roundError = abs(self._value - self.roundValue)
        return roundError