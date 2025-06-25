from Structure.myList import myList

class Queue:
    def __init__(self):
        self._items = myList()

    def enqueue(self, item):
        """Encola un elemento"""
        self._items.insertAt(item, self._items.getSize())

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Dequeue from empty queue")
        node = self._items.removeAt(0)  # Elimina el nodo de la lista
        return node.data  # Devuelve solo el dato, no el Node

    def front(self):
        """Devuelve el primer elemento sin desencolar"""
        if self.isEmpty():
            raise IndexError("Front from empty queue")
        return self._items.getNodeByPos(0).data

    def isEmpty(self):
        """Verifica si la cola está vacía"""
        return self._items.getSize() == 0

    def size(self):
        """Devuelve el tamaño de la cola"""
        return self._items.getSize()

    def __iter__(self):
        """Iterador para la cola"""
        current_node = self._items.getHead().next  # Comienza desde el primer nodo real
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next

