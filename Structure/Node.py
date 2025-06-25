class Node:
    """
    Nodo para una lista enlazada simple.

    Atributos:
        __data (any): Dato almacenado en el nodo.
        __next (Node): Referencia al siguiente nodo.
    """

    __data = None
    __next = None

    def __init__(self, data=None):
        """
        Inicializa un nodo con el dato proporcionado.

        Args:
            data (any, opcional): Dato a almacenar en el nodo. Por defecto es None.

        Raises:
            ValueError: Si el dato es None y se intenta validar.
        """
        if data is None:
            self.__data = None
            self.__next = None
        else:
            if data is None:
                raise ValueError("- RefError: Data no puede ser None.")
            self.__data = data
            self.__next = None

    def fromCopy(cls, copy):
        """
        Crea un nuevo nodo copiando los datos y la referencia de otro nodo.

        Args:
            copy (Node): Nodo a copiar.

        Returns:
            Node: Nuevo nodo con los mismos datos y referencia.

        Raises:
            ValueError: Si el nodo a copiar es None.
        """
        if copy is None:
            raise ValueError("- RefError: Copia fallida por nodo nulo.")
        new_node = cls()
        new_node.__data = copy.getData()
        new_node.__next = copy.getNext()
        return new_node

    def setData(self, data):
        """
        Asigna un nuevo dato al nodo.

        Args:
            data (any): Nuevo dato a asignar.

        Raises:
            ValueError: Si el dato es igual al actual o es None.
        """
        if data == self.__data:
            raise ValueError("- RefError: Tiene el mismo dato.")
        if data is None:
            raise ValueError("- RefError: El dato es nulo.")
        self.__data = data

    def setNext(self, next_node):
        """
        Asigna la referencia al siguiente nodo.

        Args:
            next_node (Node): Nodo siguiente.
        """
        self.__next = next_node

    def getData(self):
        """
        Devuelve el dato almacenado en el nodo.

        Returns:
            any: Dato almacenado.
        """
        return self.__data

    def getNext(self):
        """
        Devuelve la referencia al siguiente nodo.

        Returns:
            Node: Siguiente nodo.
        """
        return self.__next

    @property
    def data(self):
        """
        Propiedad para obtener el dato del nodo.

        Returns:
            any: Dato almacenado.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Propiedad para asignar el dato del nodo.

        Args:
            value (any): Nuevo dato a asignar.
        """
        self.setData(value)

    @property
    def next(self):
        """
        Propiedad para obtener el siguiente nodo.

        Returns:
            Node: Siguiente nodo.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Propiedad para asignar el siguiente nodo.

        Args:
            value (Node): Nodo siguiente.
        """
        self.setNext(value)

    def isEquals(self, obj):
        """
        Compara si el nodo es igual a otro nodo.

        Args:
            obj (Node): Nodo a comparar.

        Returns:
            bool: True si los nodos son iguales, False en caso contrario.
        """
        if self is obj:
            return True
        if obj is None or not isinstance(obj, Node):
            return False
        if self.__data is None:
            return obj.__data is None
        else:
            return self.__data == obj.__data

    def __eq__(self, other):
        """
        Sobrecarga del operador == para comparar nodos.

        Args:
            other (Node): Nodo a comparar.

        Returns:
            bool: True si los nodos son iguales, False en caso contrario.
        """
        return self.isEquals(other)

    def __str__(self):
        """
        Devuelve la representación en string del nodo.

        Returns:
            str: Representación del nodo.
        """
        return f"{{Valor = {self.__data}}}"