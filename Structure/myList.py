import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from Node import Node

class myList:
    """
    Implementación de una lista enlazada simple.

    Atributos:
        __head (Node): Nodo cabeza de la lista (no almacena datos útiles).
        __size (int): Tamaño actual de la lista.
    """

    __head = None
    __size = 0

    def __init__(self):
        """
        Inicializa una lista vacía.
        """
        self.__head = Node(None)
        self.__size = 0

    def isEmpty(self):
        """
        Verifica si la lista está vacía.

        Returns:
            bool: True si la lista está vacía, False en caso contrario.
        """
        return self.__head.next is None or self.__size == 0

    def getSize(self):
        """
        Devuelve el tamaño de la lista.

        Returns:
            int: Número de elementos en la lista.
        """
        return self.__size

    def getNode(self):
        """
        Devuelve el primer nodo de la lista.

        Returns:
            Node: Primer nodo de la lista.

        Raises:
            ValueError: Si la lista está vacía.
        """
        if self.isEmpty():
            raise ValueError("- list-Error: Lista vacía, nada que obtener")
        return self.__head.next

    def getNodeByData(self, data):
        """
        Busca y devuelve el primer nodo que contiene el dato especificado.

        Args:
            data: Dato a buscar.

        Returns:
            Node: Nodo que contiene el dato, o None si no se encuentra.

        Raises:
            ValueError: Si el dato es None o la lista está vacía.
        """
        if data is None:
            raise ValueError("- list-Error: El dato es nulo, no puede realizar la búsqueda")
        if self.isEmpty():
            raise ValueError("- list-Error: Lista vacía, nada que obtener")
        current = self.__head.next
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None

    def getNodeByPos(self, pos):
        """
        Devuelve el nodo en la posición especificada.

        Args:
            pos (int): Posición del nodo (0-indexado).

        Returns:
            Node: Nodo en la posición dada.

        Raises:
            ValueError: Si la lista está vacía.
        """
        if self.isEmpty():
            raise ValueError("- list-Error: Lista vacía, nada que obtener")
        if pos <= 0:
            return self.getNode()
        iterator = 0
        current = self.__head.next
        prev = self.__head
        while current is not None and iterator < pos:
            prev = current
            current = current.next
            iterator += 1
        if iterator == self.__size:
            return prev
        return current

    def insert(self, data):
        """
        Inserta un nuevo nodo al inicio de la lista.

        Args:
            data: Dato a insertar.

        Raises:
            ValueError: Si el dato es None.
        """
        if data is None:
            raise ValueError("- list-Error: El dato no puede ser nulo")
        newNode = Node(data)
        if self.__head.next is None:
            self.__head.next = newNode
        else:
            newNode.next = self.__head.next
            self.__head.next = newNode
        self.__size += 1

    def insertAt(self, data, pos):
        """
        Inserta un nuevo nodo en la posición especificada.

        Args:
            data: Dato a insertar.
            pos (int): Posición donde insertar el nodo.

        Raises:
            ValueError: Si el dato es None.
        """
        if data is None:
            raise ValueError("- list-Error: El dato no puede ser nulo")
        if pos <= 0:
            self.insert(data)
            return
        newNode = Node(data)
        current = self.__head.next
        prev = self.__head
        index = 0
        while current is not None and index < pos:
            prev = current
            current = current.next
            index += 1
        prev.next = newNode
        newNode.next = current
        self.__size += 1

    def remove(self):
        """
        Elimina el primer nodo de la lista.

        Returns:
            Node: Nodo eliminado.

        Raises:
            ValueError: Si la lista está vacía.
        """
        if self.isEmpty():
            raise ValueError("- list-Error: Lista vacía, nada que eliminar")
        removed = self.__head.next
        self.__head.next = removed.next
        self.__size -= 1
        return removed

    def removeAt(self, pos):
        """
        Elimina el nodo en la posición especificada.

        Args:
            pos (int): Posición del nodo a eliminar.

        Returns:
            Node: Nodo eliminado.

        Raises:
            ValueError: Si la posición es inválida.
        """
        if pos < 0 or pos >= self.__size:
            raise ValueError("- list-Error: Posición inválida")
        if pos == 0:
            return self.remove()
        current = self.__head.next
        prev = self.__head
        index = 0
        while index < pos:
            prev = current
            current = current.next
            index += 1
        prev.next = current.next
        self.__size -= 1
        return current

    def removeByData(self, data):
        """
        Elimina el primer nodo que contiene el dato especificado.

        Args:
            data: Dato a eliminar.

        Returns:
            Node: Nodo eliminado.

        Raises:
            ValueError: Si el dato es None, la lista está vacía o el dato no se encuentra.
        """
        if data is None:
            raise ValueError("- list-Error: El dato es nulo, no puede realizar la búsqueda")
        if self.isEmpty():
            raise ValueError("- list-Error: Lista vacía, nada que eliminar")
        prev = self.__head
        current = self.__head.next
        while current is not None and current.data != data:
            prev = current
            current = current.next
        if current is None:
            raise ValueError("- list-Error: Dato no encontrado en la lista")
        prev.next = current.next
        self.__size -= 1
        return current

    def showList(self):
        """
        Muestra el contenido de la lista por consola.
        """
        if self.isEmpty():
            print("|::")
            return
        current = self.__head.next
        while current is not None:
            print(current, end="")
            if current.next is not None:
                print(" -> ", end="")
            current = current.next
        print(" |::")

    def __iter__(self):
        """
        Permite iterar sobre la lista con un for.

        Returns:
            myList: El iterador (self).
        """
        self.current = self.__head.next
        return self

    def __next__(self):
        """
        Devuelve el siguiente elemento en la iteración.

        Returns:
            any: El dato del siguiente nodo.

        Raises:
            StopIteration: Si no hay más elementos.
        """
        if self.current is None:
            raise StopIteration
        else:
            value = self.current.data
            self.current = self.current.next
            return value