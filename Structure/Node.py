class Node:
    
    __data = None
    __next = None
    
    def __init__(self, data=None):
        if data is None:
            self.__data = None
            self.__next = None
        else:
            if data is None:
                raise ValueError("- RefError: Data no puede ser None.")
            self.__data = data
            self.__next = None
    
    def fromCopy(cls, copy):
        if copy is None:
            raise ValueError("- RefError: Copia fallida por nodo nulo.")
        new_node = cls()
        new_node.__data = copy.getData()
        new_node.__next = copy.getNext()
        return new_node
    
    def setData(self, data):
        if data == self.__data:
            raise ValueError("- RefError: Tiene el mismo dato.")
        
        if data is None:
            raise ValueError("- RefError: El dato es nulo.")
        
        self.__data = data
    
    def setNext(self, next_node):
        self.__next = next_node
    
    def getData(self):
        return self.__data
    
    def getNext(self):
        return self.__next
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        self.setData(value)
    
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, value):
        self.setNext(value)
    
    def isEquals(self, obj):
        if self is obj:
            return True
        
        if obj is None or not isinstance(obj, Node):
            return False
        
        if self.__data is None:
            return obj.__data is None
        else:
            return self.__data == obj.__data
    
    def __eq__(self, other):
        return self.isEquals(other)
    
    def __str__(self):
        return f"{{Valor = {self.__data}}}"