import numpy as np

class GaussSeidel:

    __matrix=np.array([])
    __tolerance=0.0
    __maxIterations = 0.0
    __vector=np.array([])

    def __init__(self, matriz):
        self.__matrix = np.array(matriz, dtype=float)
        self.__tolerance = 1e-10
        self.__maxIterations = 1000
        self.n = len(self.__matrix)
        self.__vector = np.array([2] * self.n)
        self.validateMatrix()
        if not self.isDiagonallyDominant():
            self.makeDiagonallyDominant()

    def validateMatrix(self):
        if not isinstance(self.__matrix, (np.ndarray)):
                raise ValueError("La matriz debe ser un arreglo de NumPy.")
        
        if len(self.__matrix) == 0:
            raise ValueError("La matriz no puede estar vacía.")
            
        if not len(self.__matrix)==len(self.__matrix[0]):
            raise ValueError("La matriz debe ser cuadrada.")

        firstRowLenght=len(self.__matrix[0])    
        for row in self.__matrix:
            if len(row)==0:
                raise ValueError("los vectores no pueden estar vacios")
            if len(row)!=firstRowLenght:
                raise ValueError("los vectores deben ser todos de igual forma")
            for element in row:
                if not isinstance(element, (int, float)):
                    raise ValueError("Todos los elementos de la matriz deben ser números decimales.")
                
        if len(self.__vector) != len(self.__matrix):
            raise ValueError("El vector debe tener la misma longitud que el número de filas de la matriz.")


    def isDiagonallyDominant(self):
        for i in range(self.n):
            for i in range(self.n):
                sumRow = 0
                for j in range(len(self.__matrix[i])):
                    sumRow += abs(self.__matrix[i, j]) 
                    sumRow -= abs(self.__matrix[i, i])  
        
            if abs(self.__matrix[i, i]) < sumRow:
                return False
        return True

    def makeDiagonallyDominant(self):
        for i in range(self.n):
            maxVal = -1  
            maxIndex = i  
    
        for j in range(len(self.__matrix[i])):
            currentAbs = abs(self.__matrix[i][j])
            if currentAbs > maxVal:
                maxVal = currentAbs
                maxIndex = j
    
        if maxIndex != i:
            
            tempRow = self.__matrix[i].copy()
            self.__matrix[i] = self.__matrix[maxIndex]
            self.__matrix[maxIndex] = tempRow
        
            tempVal = self.__vector[i]
            self.__vector[i] = self.__vector[maxIndex]
            self.__vector[maxIndex] = tempVal

    def maxAbsoluteDiff(self, x_new, x):
        maxDiff = 0  
        for i in range(len(x_new)):
            diff = abs(x_new[i] - x[i])  
            if diff > maxDiff:  
                maxDiff = diff
        return maxDiff


    def solve(self):
        x = np.array([0.0 for i in range(self.n)])
        for iteration in range(self.__maxIterations):
            xNew = np.array(x, dtype=float)
            for i in range(self.n):
                sum1 = 0 
                for j in range(i):
                    sum1 += self.__matrix[i, j] * xNew[j]  

                sum2 = 0  
                for j in range(i + 1, self.n):
                    sum2 += self.__matrix[i, j] * x[j]  

                xNew[i] = (self.__vector[i] - sum1 - sum2) / self.__matrix[i, i]
    
            if self.maxAbsoluteDiff(xNew, x) < self.__tolerance:
                return xNew
            x = xNew
        raise ValueError("El método no convergió en el número máximo de iteraciones")
    
    def getMatrix(self):
        return self.__matrix
    
    def setMatrix(self, matrix):
        self.__matrix=matrix

    def setTolerance(self, tolerance):
        self.__tolerance=tolerance 

    def setMaxIterations(self, maxIterations):
        self.__maxIterations=maxIterations