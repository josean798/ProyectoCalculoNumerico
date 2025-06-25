import numpy as np

class GaussSeidel:
    """
    Clase para resolver sistemas de ecuaciones lineales usando el método iterativo de Gauss-Seidel.

    Atributos:
        __matrix (np.ndarray): Matriz de coeficientes del sistema.
        __tolerance (float): Tolerancia para el criterio de convergencia.
        __maxIterations (int): Número máximo de iteraciones permitidas.
        __vector (np.ndarray): Vector de términos independientes.
        n (int): Tamaño del sistema (número de ecuaciones).
    """

    __matrix = np.array([])
    __tolerance = 0.0
    __maxIterations = 0.0
    __vector = np.array([])

    def __init__(self, matriz):
        """
        Inicializa el objeto GaussSeidel con la matriz dada.

        Args:
            matriz (array-like): Matriz de coeficientes (puede ser lista de listas o np.ndarray).

        Raises:
            ValueError: Si la matriz no es válida.
        """
        self.__matrix = np.array(matriz, dtype=float)
        self.__tolerance = 1e-10
        self.__maxIterations = 1000
        self.n = len(self.__matrix)
        self.__vector = np.array([2] * self.n)
        self.validateMatrix()
        if not self.isDiagonallyDominant():
            self.makeDiagonallyDominant()

    def validateMatrix(self):
        """
        Valida que la matriz y el vector sean correctos para el método de Gauss-Seidel.

        Raises:
            ValueError: Si la matriz no es cuadrada o contiene elementos no numéricos.
        """
        if not isinstance(self.__matrix, (np.ndarray)):
            raise ValueError("La matriz debe ser un arreglo de NumPy.")
        
        if len(self.__matrix) == 0:
            raise ValueError("La matriz no puede estar vacía.")
            
        if not len(self.__matrix) == len(self.__matrix[0]):
            raise ValueError("La matriz debe ser cuadrada.")

        firstRowLenght = len(self.__matrix[0])    
        for row in self.__matrix:
            if len(row) == 0:
                raise ValueError("los vectores no pueden estar vacios")
            if len(row) != firstRowLenght:
                raise ValueError("los vectores deben ser todos de igual forma")
            for element in row:
                if not isinstance(element, (int, float)):
                    raise ValueError("Todos los elementos de la matriz deben ser números decimales.")
                
        if len(self.__vector) != len(self.__matrix):
            raise ValueError("El vector debe tener la misma longitud que el número de filas de la matriz.")

    def isDiagonallyDominant(self):
        """
        Verifica si la matriz es diagonalmente dominante.

        Returns:
            bool: True si la matriz es diagonalmente dominante, False en caso contrario.
        """
        for i in range(self.n):
            sumRow = 0
            for j in range(len(self.__matrix[i])):
                sumRow += abs(self.__matrix[i, j])
                sumRow -= abs(self.__matrix[i, i])
            if abs(self.__matrix[i, i]) < sumRow:
                return False
        return True

    def makeDiagonallyDominant(self):
        """
        Intenta reorganizar las filas de la matriz para hacerla diagonalmente dominante.
        """
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
        """
        Calcula la máxima diferencia absoluta entre dos vectores.

        Args:
            x_new (np.ndarray): Nuevo vector de soluciones.
            x (np.ndarray): Vector de soluciones anterior.

        Returns:
            float: Máxima diferencia absoluta.
        """
        maxDiff = 0  
        for i in range(len(x_new)):
            diff = abs(x_new[i] - x[i])  
            if diff > maxDiff:  
                maxDiff = diff
        return maxDiff

    def solve(self):
        """
        Resuelve el sistema de ecuaciones usando el método de Gauss-Seidel.

        Returns:
            np.ndarray: Vector solución del sistema.

        Raises:
            ValueError: Si el método no converge en el número máximo de iteraciones.
        """
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
        """
        Devuelve la matriz de coeficientes.

        Returns:
            np.ndarray: Matriz de coeficientes.
        """
        return self.__matrix
    
    def setMatrix(self, matrix):
        """
        Asigna una nueva matriz de coeficientes.

        Args:
            matrix (np.ndarray): Nueva matriz de coeficientes.
        """
        self.__matrix = matrix

    def setTolerance(self, tolerance):
        """
        Asigna una nueva tolerancia para el criterio de convergencia.

        Args:
            tolerance (float): Nueva tolerancia.
        """
        self.__tolerance = tolerance 

    def setMaxIterations(self, maxIterations):
        """
        Asigna el número máximo de iteraciones permitidas.

        Args:
            maxIterations (int): Número máximo de iteraciones.
        """
        self.__maxIterations = maxIterations