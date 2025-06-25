from Error import Error
import math

class TruncationError(Error):
    """
    Clase para calcular el error de truncamiento al aproximar funciones matemáticas mediante series.

    Hereda de:
        Error

    Atributos:
        _value (int|float): Valor sobre el que se evalúa la función.
        __n (int): Número de términos de la serie para la aproximación.

    Métodos:
        calculateError(): Calcula el error de truncamiento.
        value (property): Getter y setter para el valor.
        n (property): Getter y setter para el número de términos.
        _aproxFunction(n, value): Método estático que aproxima cos(x) usando n términos de la serie de Taylor.
    """

    __n = None

    def __init__(self, value, n):
        """
        Inicializa la clase TruncationError.

        Args:
            value (int|float): Valor sobre el que se evalúa la función.
            n (int): Número de términos de la serie para la aproximación.

        Raises:
            TypeError: Si el valor no es numérico o n no es un entero positivo.
        """
        if not isinstance(value, (int, float)) or not isinstance(n, int) or n <= 0:
            raise TypeError("Error: El valor debe ser un número y n debe ser un entero positivo.")
        super().__init__(value)
        self.__n = n

    @property
    def value(self):
        """
        Obtiene el valor sobre el que se evalúa la función.

        Returns:
            int|float: Valor de entrada.
        """
        return self._value
    
    @value.setter
    def value(self, value):
        """
        Establece el valor sobre el que se evalúa la función.

        Args:
            value (int|float): Valor de entrada.

        Raises:
            TypeError: Si el valor no es numérico.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Error: El valor debe ser un número.")
        self._value = value

    @property
    def n(self):
        """
        Obtiene el número de términos de la serie para la aproximación.

        Returns:
            int: Número de términos.
        """
        return self.__n
    
    @n.setter
    def n(self, n):
        """
        Establece el número de términos de la serie para la aproximación.

        Args:
            n (int): Número de términos.

        Raises:
            TypeError: Si n no es un entero positivo.
        """
        if not isinstance(n, int) or n <= 0:
            raise TypeError("Error: n debe ser un entero positivo.")
        self.__n = n
    
    @staticmethod
    def _aproxFunction(n, value):
        """
        Aproxima cos(x) usando n términos de la serie de Taylor.

        Args:
            n (int): Número de términos de la serie.
            value (int|float): Valor de x.

        Returns:
            float: Aproximación de cos(x) usando n términos.

        Raises:
            ValueError: Si n no es un entero positivo.
            TypeError: Si value no es numérico.
        """
        if n <= 0 or not isinstance(n, int):
            raise ValueError("Error: n debe ser un entero positivo.")
        if not isinstance(value, (int, float)):
            raise TypeError("Error: El valor debe ser un número.")
        sum = 0
        for i in range(n):
            sum += (-1)**i * (value**(2*i)) / math.factorial(2*i)
        return sum
    
    def calculateError(self):
        """
        Calcula el error de truncamiento entre el valor exacto de cos(x) y su aproximación por serie de Taylor.

        Returns:
            float: Error absoluto de truncamiento.
        """
        exValue = math.cos(self._value)
        truncValue = self._aproxFunction(self.__n, self._value)
        truncError = abs(exValue - truncValue)
        return truncError