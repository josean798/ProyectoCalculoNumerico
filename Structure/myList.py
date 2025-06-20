import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from Node import Node


class myList:
    def __init__(self):
        self.head = Node(None)  
        self.size = 0

    def isEmpty(self):
        return self.head.next is None

    def insert(self, data):
        new_node = Node(data)
        if self.head.next is None:
            self.head.next = new_node
        else:
            new_node.next = self.head.next
            self.head.next = new_node
        self.size += 1

    def insertAt(self, data, pos):
        if pos <= 0:
            self.insert(data)
            return

        new_node = Node(data)
        current = self.head.next
        prev = self.head
        index = 0

        while current is not None and index < pos:
            prev = current
            current = current.next
            index += 1

        prev.next = new_node
        new_node.next = current
        self.size += 1

    def remove(self):
        if self.is_empty():
            raise ValueError("La lista está vacía")
        removed = self.head.next
        self.head.next = removed.next
        self.size -= 1
        return removed

    def removeAt(self, pos):
        if pos < 0 or pos >= self.size:
            raise IndexError("Posición inválida")

        if pos == 0:
            return self.remove()

        current = self.head.next
        prev = self.head
        index = 0

        while index < pos:
            prev = current
            current = current.next
            index += 1

        prev.next = current.next
        self.size -= 1
        return current

    def getSize(self):
        return self.size

    def showList(self):
        if self.is_empty():
            print("|::")
            return

        current = self.head.next
        while current is not None:
            print(current, end="")
            if current.next is not None:
                print(" -> ", end="")
            current = current.next
        print(" |::")

    def __iter__(self):
        self.current = self.head.next
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration 
        else:
            value = self.current.data
            self.current = self.current.next  
            return value


