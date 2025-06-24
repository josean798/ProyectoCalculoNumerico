from Structure.myList import myList

class Stack:
    def __init__(self):
        self._items = myList()

    def push(self, item):
        """Apila un elemento"""
        self._items.insertAt(item, self._items.getSize())

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        node = self._items.removeAt(self._items.getSize() - 1)  # Elimina el nodo
        return node.data  # Devuelve solo el dato, no el Node

    def peek(self):
        """Devuelve el elemento en el tope sin desapilar"""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items.getNodeByPos(self._items.getSize() - 1).data

    def is_empty(self):
        """Verifica si la pila está vacía"""
        return self._items.getSize() == 0

    def size(self):
        """Devuelve el tamaño de la pila"""
        return self._items.getSize()

    def __iter__(self):
        """Iterador para la pila"""
        current_node = self._items.getHead().next  # Comienza desde el primer nodo real
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next

