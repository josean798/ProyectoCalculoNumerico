from Error import Error

class PropagationError(Error):
    """
    Clase para calcular el error de propagación en una operación aritmética.

    Hereda de:
        Error

    Métodos:
        calculateError(): Calcula el error de propagación.
        value (property): Getter y setter para el valor real.
        _operation(value): Método estático que simula una operación con error de propagación.
    """

    def __init__(self, value):
        """
        Inicializa la clase PropagationError.

        Args:
            value (int|float): Valor real o de referencia.

        Raises:
            TypeError: Si el valor no es numérico.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Error: El valor debe ser un número.")
        super().__init__(value)

    @property
    def value(self):
        """
        Obtiene el valor real o de referencia.

        Returns:
            int|float: Valor real o de referencia.
        """
        return self._value
    
    @value.setter
    def value(self, value):
        """
        Establece el valor real o de referencia.

        Args:
            value (int|float): Valor real o de referencia.

        Raises:
            TypeError: Si el valor no es numérico.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Error: El valor debe ser un número.")
        self._value = value
    
    @staticmethod
    def _operation(value):
        """
        Simula una operación aritmética con error de propagación.

        Args:
            value (int|float): Valor de entrada.

        Returns:
            float: Resultado de la operación con error de propagación.
        """
        return (value + 0.1) * 3 - 0.3

    def calculateError(self):
        """
        Calcula el error de propagación entre el valor real y el valor con error.

        Returns:
            float: Error de propagación absoluto.
        """
        realValue = self._value * 3
        errorValue = self._operation(self._value)
        propError = abs(realValue - errorValue)
        return propError