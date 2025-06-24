import numpy as np

class MatrixElementalOperations:
    __matrix = None
    __record = None

    def __init__(self, matrix):
        if not isinstance(matrix, np.ndarray):
            raise ValueError("La matrix debe ser un array de numpy")
            
        self.__matrix = matrix.copy()
        self.__record = np.array([])
    
    def rowSwap(self, row1, row2):
        if row1 < 0 or row2 < 0 or row1 >= self.__matrix.shape[0] or row2 >= self.__matrix.shape[0]:
            raise ValueError("Índices de fila fuera de rango")
            
        if row1 == row2:
            return
            
        self.__matrix[[row1, row2]] = self.__matrix[[row2, row1]]
        
        self.__record = np.append(self.__record, f"Intercambio fila {row1} con fila {row2}")
    
    def multiplyRow(self, row, scalar):
        if scalar == 0:
            raise ValueError("El escalar no puede ser cero")
            
        if row < 0 or row >= self.__matrix.shape[0]:
            raise ValueError("Índice de fila fuera de rango")
            
        self.__matrix[row] *= scalar
        
        self.__record = np.append(self.__record, f"Multiplicar fila {row} por {scalar}")
    
    def addMultiple(self, destinationRow, sourceRow, scalar):

        if destinationRow < 0 or sourceRow < 0 or \
           destinationRow >= self.__matrix.shape[0] or sourceRow >= self.__matrix.shape[0]:
            raise ValueError("Índices de fila fuera de rango")
            
        if destinationRow == sourceRow and scalar == -1:
            raise ValueError("Esta operación anularía la fila completa")
            
        self.__matrix[destinationRow] += scalar * self.__matrix[sourceRow]
        
        self.__record = np.append(self.__record, f"Sumar a fila {destinationRow} el múltiplo {scalar} de fila {sourceRow}")
    
    def getMatrix(self):
        return self.__matrix.copy()
    
    def getRecord(self):
        return self.__record.copy()
    
    def __str__(self):
        return str(self.__matrix)