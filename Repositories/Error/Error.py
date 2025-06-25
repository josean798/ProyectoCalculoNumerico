class Error:
    """
    Clase base para el manejo de errores numéricos.

    Atributos:
        _value (int|float): Valor real o de referencia.

    Métodos:
        calculateError(): Método abstracto para calcular el error (debe ser implementado por las subclases).
        value (property): Getter y setter para el valor.
    """

    _value = None

    def __init__(self, value):
        """
        Inicializa la clase Error.

        Args:
            value (int|float): Valor real o de referencia.

        Raises:
            TypeError: Si el valor no es numérico.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Error: El valor debe ser un número.")
        self._value = value

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

    def calculateError(self):
        """
        Método abstracto para calcular el error.
        Debe ser implementado por las subclases.

        Raises:
            NotImplementedError: Si no se implementa en la subclase.
        """
        pass