import numpy as np
import random
from Repositories.MatrixOperations.MatrixElementalOperations import MatrixElementalOperations
class matrixOperations:
    """
    Clase para realizar operaciones aleatorias sobre una matriz utilizando MatrixElementalOperations.

    Atributos:
        __matrixInicial (np.ndarray): Matriz original sobre la que se realizan las operaciones.
        __ops (MatrixElementalOperations): Objeto que gestiona las operaciones elementales sobre la matriz.

    Métodos:
        generateRandomValue(minValue, maxValue, exclude=None): Genera un valor aleatorio en el rango dado, excluyendo un valor si se indica.
        randomOperations(): Realiza una secuencia de operaciones aleatorias sobre la matriz.
        getResults(): Devuelve el registro de operaciones realizadas.
    """

    __matrixInicial = None
    __ops = None
    
    def __init__(self, matriz):
        """
        Inicializa la clase matrixOperations.

        Args:
            matriz (np.ndarray): Matriz inicial sobre la que se trabajará.

        Raises:
            ValueError: Si la matriz no es un array de numpy.
        """
        if not isinstance(matriz, np.ndarray):
            raise ValueError("La matriz debe ser un array de numpy")
            
        self.__matrixInicial = matriz.copy()
        self.__ops = MatrixElementalOperations(self.__matrixInicial)
    
    def generateRandomValue(self, minValue, maxValue, exclude=None):
        """
        Genera un valor aleatorio entero en el rango [minValue, maxValue], excluyendo un valor si se indica.

        Args:
            minValue (int): Valor mínimo.
            maxValue (int): Valor máximo.
            exclude (int|float|None): Valor a excluir (opcional).

        Returns:
            int: Valor aleatorio generado.
        """
        while True:
            val = random.randint(minValue, maxValue)
            if exclude is None or not np.isclose(val, exclude):
                return val
    
    def randomOperations(self):
        """
        Realiza una secuencia de operaciones aleatorias sobre la matriz:
        - Intercambia dos filas aleatorias (si hay al menos 2 filas).
        - Multiplica una fila aleatoria por un escalar aleatorio distinto de cero.
        - Suma a una fila un múltiplo aleatorio de otra fila (si hay al menos 2 filas).
        """
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
        """
        Devuelve el registro de operaciones realizadas sobre la matriz.

        Returns:
            np.ndarray: Registro de operaciones.
        """
        return self.__ops.getRecord()
    
