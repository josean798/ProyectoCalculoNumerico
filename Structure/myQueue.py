from Structure.myList import myList

class Queue:
    """
    Implementación de una cola (FIFO) usando una lista enlazada personalizada.

    Atributos:
        _items (myList): Lista enlazada que almacena los elementos de la cola.
    """

    def __init__(self):
        """
        Inicializa una cola vacía.
        """
        self._items = myList()

    def enqueue(self, item):
        """
        Encola un elemento al final de la cola.

        Args:
            item: Elemento a agregar a la cola.
        """
        self._items.insertAt(item, self._items.getSize())

    def dequeue(self):
        """
        Desencola el primer elemento de la cola.

        Returns:
            any: El dato del primer elemento en la cola.

        Raises:
            IndexError: Si la cola está vacía.
        """
        if self.isEmpty():
            raise IndexError("Dequeue from empty queue")
        node = self._items.removeAt(0)  # Elimina el nodo de la lista
        return node.data  # Devuelve solo el dato, no el Node

    def front(self):
        """
        Devuelve el primer elemento sin desencolar.

        Returns:
            any: El dato del primer elemento en la cola.

        Raises:
            IndexError: Si la cola está vacía.
        """
        if self.isEmpty():
            raise IndexError("Front from empty queue")
        return self._items.getNodeByPos(0).data

    def isEmpty(self):
        """
        Verifica si la cola está vacía.

        Returns:
            bool: True si la cola está vacía, False en caso contrario.
        """
        return self._items.getSize() == 0

    def size(self):
        """
        Devuelve el tamaño de la cola.

        Returns:
            int: Número de elementos en la cola.
        """
        return self._items.getSize()

    def __iter__(self):
        """
        Permite iterar sobre los elementos de la cola.

        Returns:
            iter: Iterador sobre los datos de la cola.
        """
        current_node = self._items.getHead().next  # Comienza desde el primer nodo real
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next