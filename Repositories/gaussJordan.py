import numpy as np

class GaussJordan:
    """
    Clase para resolver sistemas de ecuaciones lineales usando el método de Gauss-Jordan.

    Atributos:
        __matrix (np.ndarray): Matriz de coeficientes del sistema.
        __pivots (np.ndarray): Vector de pivotes de la matriz.
        __vector (np.ndarray): Vector de términos independientes.
    """

    __matrix = np.array([])
    __pivots = np.array([])
    __vector = np.array([])

    def __init__(self, matrix):
        """
        Inicializa el objeto GaussJordan con la matriz dada.

        Args:
            matrix (array-like): Matriz de coeficientes (puede ser lista de listas o np.ndarray).

        Raises:
            ValueError: Si la matriz no es válida.
        """
        self.__matrix = np.array(matrix, dtype=float)
        self.__pivots = np.array([0.0] * len(self.__matrix))
        self.__vector = np.array([2] * len(self.__matrix))
        self.validateMatrix()

    def validateMatrix(self):
        """
        Valida que la matriz y el vector sean correctos para el método de Gauss-Jordan.

        Raises:
            ValueError: Si la matriz no es cuadrada o aumentada, o si contiene elementos no numéricos.
        """
        if not isinstance(self.__matrix, (np.ndarray)):
            raise ValueError("La matriz debe ser un arreglo de NumPy.")

        if len(self.__matrix) < len(self.__matrix[0]):
            raise ValueError("La matriz tiene infinitas soluciones")

        firstRowLenght = len(self.__matrix[0])
        for row in self.__matrix:
            if len(row) == 0:
                raise ValueError("Los vectores no pueden estar vacíos")
            if len(row) != firstRowLenght:
                raise ValueError("Los vectores deben ser todos de igual forma")
            for element in row:
                if not isinstance(element, (int, float)):
                    raise ValueError("Todos los elementos de la matriz deben ser números decimales.")

        if len(self.__matrix[0]) < len(self.__matrix):
            raise ValueError("La matriz debe ser cuadrada o aumentada.")

        if len(self.__vector) != len(self.__matrix):
            raise ValueError("El vector debe tener la misma longitud que el número de filas de la matriz.")

    def solve(self):
        """
        Resuelve el sistema de ecuaciones usando el método de Gauss-Jordan.

        Returns:
            np.ndarray: Solución del sistema (vector de incógnitas).

        Raises:
            ValueError: Si algún pivote es cero (sistema singular o sin solución única).
        """
        rows = len(self.__matrix)
        cols = len(self.__matrix[0])
        augmentedMatrix = np.array([[self.__matrix[i][j] for j in range(cols)] + [self.__vector[i]] for i in range(rows)])

        for i in range(rows):
            pivot = augmentedMatrix[i, i]
            if pivot == 0:
                raise ValueError("El pivote es cero, lo que indica que el sistema puede ser singular o no tener solución única.")

            self.__pivots[i] = pivot

            augmentedMatrix[i] = augmentedMatrix[i] / pivot

            for j in range(rows):
                if i != j:
                    factor = augmentedMatrix[j, i]
                    augmentedMatrix[j] = augmentedMatrix[j] - factor * augmentedMatrix[i]

        return augmentedMatrix[:, -1]

    def getMatrix(self):
        """
        Devuelve la matriz de coeficientes.

        Returns:
            np.ndarray: Matriz de coeficientes.
        """
        return self.__matrix

    def getPivots(self):
        """
        Devuelve el vector de pivotes.

        Returns:
            np.ndarray: Vector de pivotes.
        """
        return self.__pivots

    def setMatrix(self, matriz):
        """
        Asigna una nueva matriz de coeficientes.

        Args:
            matriz (array-like): Nueva matriz de coeficientes.
        """
        self.__matrix = matriz