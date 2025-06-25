from Structure.myList import myList

class Stack:
    """
    Implementación de una pila (LIFO) usando una lista enlazada personalizada.

    Atributos:
        _items (myList): Lista enlazada que almacena los elementos de la pila.
    """

    def __init__(self):
        """
        Inicializa una pila vacía.
        """
        self._items = myList()

    def push(self, item):
        """
        Apila un elemento en la parte superior de la pila.

        Args:
            item: Elemento a agregar a la pila.
        """
        self._items.insertAt(item, self._items.getSize())

    def pop(self):
        """
        Desapila y devuelve el elemento en la parte superior de la pila.

        Returns:
            any: El dato del elemento desapilado.

        Raises:
            IndexError: Si la pila está vacía.
        """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        node = self._items.removeAt(self._items.getSize() - 1)  # Elimina el nodo
        return node.data  # Devuelve solo el dato, no el Node

    def peek(self):
        """
        Devuelve el elemento en el tope sin desapilar.

        Returns:
            any: El dato del elemento en el tope.

        Raises:
            IndexError: Si la pila está vacía.
        """
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items.getNodeByPos(self._items.getSize() - 1).data

    def is_empty(self):
        """
        Verifica si la pila está vacía.

        Returns:
            bool: True si la pila está vacía, False en caso contrario.
        """
        return self._items.getSize() == 0

    def size(self):
        """
        Devuelve el tamaño de la pila.

        Returns:
            int: Número de elementos en la pila.
        """
        return self._items.getSize()

    def __iter__(self):
        """
        Permite iterar sobre los elementos de la pila.

        Returns:
            iter: Iterador sobre los datos de la pila.
        """
        current_node = self._items.getHead().next  # Comienza desde el primer nodo real
        while current_node is not None:
            yield current_node.data