import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from Node import Node


class myList:
    
    __head = None
    __size = 0
    
    def __init__(self):
        self.__head = Node(None)  
        self.__size = 0

    def isEmpty(self):
        return self.__head.next is None or self.__size == 0

    def getSize(self):
        return self.__size

    def getNode(self):
        if self.isEmpty():
            raise ValueError("- list-Error: Lista vacía, nada que obtener")
        return self.__head.next

    def getNodeByData(self, data):
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
        if self.isEmpty():
            raise ValueError("- list-Error: Lista vacía, nada que eliminar")
            
        removed = self.__head.next
        self.__head.next = removed.next
        self.__size -= 1
        return removed

    def removeAt(self, pos):
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
        self.current = self.__head.next  
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration  
        else:
            value = self.current.data
            self.current = self.current.next  
            return value
