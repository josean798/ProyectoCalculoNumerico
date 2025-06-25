import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from myList import myList

class myReplace:
    """
    Clase para realizar reemplazos de subcadenas en una cadena de texto utilizando una lista enlazada personalizada.

    Atributos:
        __originalString (str): Cadena de texto original sobre la que se realizarán los reemplazos.
    """

    __originalString = ""

    def __init__(self, originalString):
        """
        Inicializa un objeto myReplace con la cadena de texto original.

        Args:
            originalString (str): Cadena de texto sobre la que se realizarán los reemplazos.

        Raises:
            ValueError: Si el valor proporcionado no es una cadena de texto o está vacía.
        """
        if not isinstance(originalString, str):
            raise ValueError("El valor proporcionado debe ser una cadena de texto")
        if not originalString:
            raise ValueError("La cadena no puede estar vacía")
        self.__originalString = originalString

    def getReplace(self, oldSubstring=None, newSubstring=None):
        """
        Reemplaza todas las apariciones de una subcadena por otra en la cadena original.

        Args:
            oldSubstring (str): Subcadena a reemplazar.
            newSubstring (str): Nueva subcadena que reemplazará a la anterior.

        Returns:
            str: Nueva cadena con los reemplazos realizados.

        Raises:
            ValueError: Si faltan parámetros, no son cadenas de texto, o la subcadena a reemplazar está vacía.
        """
        if oldSubstring is None or newSubstring is None:
            raise ValueError("Error: Faltan parámetros para realizar el reemplazo")
        if not isinstance(oldSubstring, str) or not isinstance(newSubstring, str):
            raise ValueError("Error: Ambos parámetros deben ser cadenas de texto")
        if not oldSubstring:
            raise ValueError("Error: La subcadena a reemplazar no puede estar vacía")

        resultList = myList()
        currentPosition = 0

        i = 0
        lenOld = len(oldSubstring)
        lenOriginal = len(self.__originalString)

        while i <= lenOriginal - lenOld:
            if self.__originalString[i:i+lenOld] == oldSubstring:
                for char in newSubstring:
                    resultList.insertAt(char, currentPosition)
                    currentPosition += 1
                i += lenOld
            else:
                resultList.insertAt(self.__originalString[i], currentPosition)
                currentPosition += 1
                i += 1

        while i < lenOriginal:
            resultList.insertAt(self.__originalString[i], currentPosition)
            currentPosition += 1
            i += 1

        resultStr = ""
        currentNode = resultList.getNode()
        while currentNode is not None:
            resultStr += currentNode.data
            currentNode = currentNode.next

        return resultStr

    def __str__(self):
        """
        Devuelve la representación en string de la cadena original.

        Returns:
            str: Cadena de texto original.
        """
        return self.__originalString