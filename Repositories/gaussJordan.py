import numpy as np

class GaussJordan:

    __matrix=np.array([])
    __pivots=np.array([])
    __vector=np.array([])

    def __init__(self, matrix):
        self.__matrix = np.array(matrix, dtype=float)
        self.__pivots = np.array([0.0] * len(self.__matrix))
        self.__vector = np.array([2] * len(self.__matrix))
        self.validateMatrix()

    def validateMatrix(self):
        if not isinstance(self.__matrix, (np.ndarray)):
            raise ValueError("La matriz debe ser un arreglo de NumPy.")
        
        firstRowLenght=len(self.__matrix[0])    
        for row in self.__matrix:
            if len(row)==0:
                raise ValueError("los vectores no pueden estar vacios")
            if len(row)!=firstRowLenght:
                raise ValueError("los vectores deben ser todos de igual forma")
            for element in row:
                if not isinstance(element, (int, float)):
                    raise ValueError("Todos los elementos de la matriz deben ser números decimales.")
        
        if len(self.__matrix[0]) < len(self.__matrix):
            raise ValueError("La matriz debe ser cuadrada o aumentada.")
        
        if len(self.__vector) != len(self.__matrix):
            raise ValueError("El vector debe tener la misma longitud que el número de filas de la matriz.")

    def solve(self):
        rows = len(self.__matrix)
        cols = len(self.__matrix[0])  
        augmentedMatrix = np.array([[self.__matrix[i][j] for j in range(cols)] + [self.__vector[i]] for i in range(rows)])

        for i in range(rows):
            pivot = augmentedMatrix[i, i]
            if pivot == 0:
                raise ValueError("El pivote es cero, lo que indica que el sistema puede ser singular o no tener solución única.")

            self.__pivots[i]=pivot
            
            augmentedMatrix[i] = augmentedMatrix[i] / pivot
            
            for j in range(rows):
                if i != j:
                    factor = augmentedMatrix[j, i]
                    augmentedMatrix[j] = augmentedMatrix[j] - factor * augmentedMatrix[i]
        
        return augmentedMatrix[:, -1]
    
    def getMatrix(self):
        return self.__matrix
    
    def getPivots(self):
        return self.__pivots
    
    def setMatrix(self, matriz):
        self.__matrix=matriz

    def setMatrix(self, matriz):
        self.__matrix=matriz


  