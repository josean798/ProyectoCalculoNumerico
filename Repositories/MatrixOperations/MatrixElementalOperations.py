import numpy as np

class MatrixElementalOperations:
    """
    Clase para realizar operaciones elementales sobre matrices utilizando NumPy.

    Atributos:
        __matrix (np.ndarray): Matriz sobre la que se realizan las operaciones.
        __record (np.ndarray): Registro de las operaciones realizadas.

    Métodos:
        rowSwap(row1, row2): Intercambia dos filas de la matriz.
        multiplyRow(row, scalar): Multiplica una fila por un escalar.
        addMultiple(destinationRow, sourceRow, scalar): Suma a una fila un múltiplo de otra fila.
        getMatrix(): Devuelve una copia de la matriz actual.
        getRecord(): Devuelve una copia del registro de operaciones.
        __str__(): Representación en cadena de la matriz.
    """

    __matrix = None
    __record = None

    def __init__(self, matrix):
        """
        Inicializa la clase MatrixElementalOperations.

        Args:
            matrix (np.ndarray): Matriz inicial.

        Raises:
            ValueError: Si la matriz no es un array de numpy.
        """
        if not isinstance(matrix, np.ndarray):
            raise ValueError("La matrix debe ser un array de numpy")
            
        self.__matrix = matrix.copy()
        self.__record = np.array([])
    
    def rowSwap(self, row1, row2):
        """
        Intercambia dos filas de la matriz.

        Args:
            row1 (int): Índice de la primera fila.
            row2 (int): Índice de la segunda fila.

        Raises:
            ValueError: Si los índices están fuera de rango o son iguales.
        """
        if row1 < 0 or row2 < 0 or row1 >= self.__matrix.shape[0] or row2 >= self.__matrix.shape[0]:
            raise ValueError("Índices de fila fuera de rango")
            
        if row1 == row2:
            return
            
        self.__matrix[[row1, row2]] = self.__matrix[[row2, row1]]
        
        self.__record = np.append(self.__record, f"Intercambio fila {row1} con fila {row2}")
    
    def multiplyRow(self, row, scalar):
        """
        Multiplica una fila de la matriz por un escalar.

        Args:
            row (int): Índice de la fila.
            scalar (float|int): Escalar por el que multiplicar la fila.

        Raises:
            ValueError: Si el escalar es cero o el índice está fuera de rango.
        """
        if scalar == 0:
            raise ValueError("El escalar no puede ser cero")
            
        if row < 0 or row >= self.__matrix.shape[0]:
            raise ValueError("Índice de fila fuera de rango")
            
        self.__matrix[row] *= scalar
        
        self.__record = np.append(self.__record, f"Multiplicar fila {row} por {scalar}")
    
    def addMultiple(self, destinationRow, sourceRow, scalar):
        """
        Suma a una fila un múltiplo de otra fila.

        Args:
            destinationRow (int): Índice de la fila destino.
            sourceRow (int): Índice de la fila fuente.
            scalar (float|int): Escalar por el que multiplicar la fila fuente antes de sumarla.

        Raises:
            ValueError: Si los índices están fuera de rango o la operación anularía la fila.
        """
        if destinationRow < 0 or sourceRow < 0 or \
           destinationRow >= self.__matrix.shape[0] or sourceRow >= self.__matrix.shape[0]:
            raise ValueError("Índices de fila fuera de rango")
            
        if destinationRow == sourceRow and scalar == -1:
            raise ValueError("Esta operación anularía la fila completa")
            
        self.__matrix[destinationRow] += scalar * self.__matrix[sourceRow]
        
        self.__record = np.append(self.__record, f"Sumar a fila {destinationRow} el múltiplo {scalar} de fila {sourceRow}")
    
    def getMatrix(self):
        """
        Devuelve una copia de la matriz actual.

        Returns:
            np.ndarray: Copia de la matriz.
        """
        return self.__matrix.copy()
    
    def getRecord(self):
        """
        Devuelve una copia del registro de operaciones realizadas.

        Returns:
            np.ndarray: Copia del registro de operaciones.
        """
        return self.__record.copy()
    
    def __str__(self):
        """
        Representación en cadena de la matriz.

        Returns:
            str: Representación de la matriz.
        """
        return str(self.__matrix)