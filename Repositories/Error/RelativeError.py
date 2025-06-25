from Error import Error

class RelativeError(Error):
    """
    Clase para calcular el error relativo entre un valor real y un valor aproximado.

    Hereda de:
        Error

    Atributos:
        _value (int|float): Valor real.
        __aproxValue (int|float): Valor aproximado.

    Métodos:
        calculateError(): Calcula el error relativo.
        value (property): Getter y setter para el valor real.
        aproxValue (property): Getter y setter para el valor aproximado.
    """

    __aproxValue = None

    def __init__(self, value, aproxValue):
        """
        Inicializa la clase RelativeError.

        Args:
            value (int|float): Valor real.
            aproxValue (int|float): Valor aproximado.

        Raises:
            TypeError: Si los valores no son numéricos.
        """
        if not isinstance(value, (int, float)) or not isinstance(aproxValue, (int, float)):
            raise TypeError("Error: Los valores deben ser números.")
        super().__init__(value)
        self.__aproxValue = aproxValue

    @property
    def value(self):
        """
        Obtiene el valor real.

        Returns:
            int|float: Valor real.
        """
        return self._value
    
    @value.setter
    def value(self, value):
        """
        Establece el valor real.

        Args:
            value (int|float): Valor real.

        Raises:
            TypeError: Si el valor no es numérico.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Error: El valor debe ser un número.")
        self._value = value
    
    @property
    def aproxValue(self):
        """
        Obtiene el valor aproximado.

        Returns:
            int|float: Valor aproximado.
        """
        return self.__aproxValue
    
    @aproxValue.setter
    def aproxValue(self, aproxValue):
        """
        Establece el valor aproximado.

        Args:
            aproxValue (int|float): Valor aproximado.

        Raises:
            TypeError: Si el valor no es numérico.
        """
        if not isinstance(aproxValue, (int, float)):
            raise TypeError("Error: El valor aproximado debe ser un número.")
        self.__aproxValue = aproxValue
    
    def calculateError(self):
        """
        Calcula el error relativo entre el valor real y el valor aproximado.

        Returns:
            float: Error relativo.
        """
        relError = abs(self._value - self.__aproxValue) / abs(self._value)
        return relError