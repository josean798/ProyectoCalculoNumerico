import numpy as np
import random
from MatrixOperations.MatrixElementalOperations import MatrixElementalOperations
class CoordinadorOperaciones:
    __matrixInicial = None
    __ops = None
    
    def __init__(self, matriz):
        if not isinstance(matriz, np.ndarray):
            raise ValueError("La matriz debe ser un array de numpy")
            
        self.__matrixInicial = matriz.copy()
        self.__ops = MatrixElementalOperations(self.__matrixInicial)
    
    def generateRandomValue(self, minValue, maxValue, exclude=None):
        while True:
            val = random.randint(minValue, maxValue)
            if exclude is None or not np.isclose(val, exclude):
                return val
    
    def randomOperations(self):
        nRows = self.__ops.getMatrix().shape[0]
        
        if nRows >= 2:
            row1, row2 = random.sample(range(nRows), 2)
            self.__ops.rowSwap(row1, row2)
                
        row = random.randint(0, nRows - 1)
        scalar = self.generateRandomValue(-5, 5, exclude=0)
        self.__ops.multiplyRow(row, scalar)
                
        if nRows >= 2:
            destinationRow, sourceRow = random.sample(range(nRows), 2)
            scalar = self.generateRandomValue(-3, 3)
            self.__ops.addMultiple(destinationRow, sourceRow, scalar)
    
    def getResults(self):
        return self.__ops.getRecord()