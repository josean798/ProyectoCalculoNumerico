import numpy as np
from Structure.myList import myList
from Structure.myReplace import myReplace

class myNumbers:
    """
    Clase para evaluar fórmulas matemáticas con hasta tres variables (A, B, C) y una lista de números.

    Atributos:
        __numbersList (np.ndarray): Arreglo de números (como float) usados en la fórmula.
        __A (float): Primer número de la lista.
        __B (float): Segundo número de la lista.
        __C (float): Tercer número de la lista.
        __formula (str): Fórmula matemática a evaluar.
        __result (float): Resultado de la evaluación de la fórmula.
    """

    __numbersList = np.array([])
    __A = 0
    __B = 0
    __C = 0
    __formula = ""
    __result = 0

    def __init__(self, numbers, formula):
        """
        Inicializa un objeto myNumbers.

        Args:
            numbers (array-like): Lista de números (pueden ser strings o floats).
            formula (str): Fórmula matemática a evaluar, usando A, B, C como variables.

        Raises:
            ValueError: Si la fórmula o los números no son válidos.
        """
        # Convertir todos los elementos a float si vienen como string
        self.__numbersList = np.array([float(n) for n in numbers])
        formula_replacer = myReplace(formula)
        self.__formula = formula_replacer.getReplace(" ", "").lower() 
        self.validateFormula()
        self.validateNumbers()
        if len(self.__numbersList) > 0:
            self.__A = self.__numbersList[0]
        if len(self.__numbersList) > 1:
            self.__B = self.__numbersList[1]
        if len(self.__numbersList) > 2:
            self.__C = self.__numbersList[2]

    def validateFormula(self):
        """
        Valida que la fórmula solo contenga caracteres permitidos y no tenga operadores consecutivos.

        Raises:
            ValueError: Si la fórmula contiene caracteres no válidos o operadores consecutivos.
        """
        validChars = "aAbBcC0123456789-+/*()"
        for char in self.__formula:
            if char not in validChars:
                raise ValueError("La fórmula contiene caracteres no válidos")
            
        for i in range(len(self.__formula)-1):
            if self.__formula[i] in '+-*' and self.__formula[i+1] in '+-*':
                raise ValueError("Operadores consecutivos no permitidos")

    def validateNumbers(self):
        """
        Valida que todos los elementos de la lista de números sean de tipo float o int.

        Raises:
            ValueError: Si algún elemento no es un número.
        """
        for i in range(len(self.__numbersList)):
            if not isinstance(self.__numbersList[i], (float, int)):
                raise ValueError("Los miembros del arreglo deben ser números")

    def replaceFormula(self):
        """
        Reemplaza las variables A, B y C en la fórmula por sus valores numéricos.

        Returns:
            str: Fórmula con los valores numéricos sustituidos.
        """
        replacer_a = myReplace(self.__formula)
        formula_with_a = replacer_a.getReplace("a", str(self.__A))
        
        replacer_b = myReplace(formula_with_a)
        formula_with_b = replacer_b.getReplace("b", str(self.__B))
        
        replacer_c = myReplace(formula_with_b)
        formula = replacer_c.getReplace("c", str(self.__C))
        
        return formula

    def evaluate(self):
        """
        Evalúa la fórmula matemática con los valores actuales de A, B y C.

        Returns:
            float: Resultado de la evaluación.
        """
        self.__result = self.evaluateExpression(self.replaceFormula())
        return self.__result

    def evaluateExpression(self, expr):
        """
        Evalúa una expresión matemática, resolviendo primero los paréntesis.

        Args:
            expr (str): Expresión matemática a evaluar.

        Returns:
            float: Resultado de la evaluación.
        """
        while '(' in expr:
            expr = self.evaluateParentheses(expr)
        tokens = self.tokenize(expr)
        return self.calculate(tokens)

    def evaluateParentheses(self, expr):
        """
        Evalúa la subexpresión dentro del paréntesis más interno.

        Args:
            expr (str): Expresión matemática con paréntesis.

        Returns:
            str: Expresión con el paréntesis resuelto.

        Raises:
            ValueError: Si los paréntesis no están balanceados.
        """
        start = expr.rfind('(')
        end = expr.find(')', start)
        if start == -1 or end == -1:
            raise ValueError("Paréntesis no balanceados")
        subExpr = expr[start + 1:end]
        subResult = self.calculate(self.tokenize(subExpr))
        return expr[:start] + str(subResult) + expr[end + 1:]

    def tokenize(self, expr):
        """
        Convierte una expresión matemática en una lista de tokens (números y operadores).

        Args:
            expr (str): Expresión matemática.

        Returns:
            myList: Lista de tokens.
        """
        tokens = myList()
        currentToken = ""
        for char in expr:
            if char in '+-*/':
                if currentToken != "":
                    tokens.insertAt(currentToken, tokens.getSize())  
                    currentToken = ""
                tokens.insertAt(char, tokens.getSize())  
            else:
                currentToken += char
        if currentToken != "":
            tokens.insertAt(currentToken, tokens.getSize())  
        return tokens

    def calculate(self, tokens):
        """
        Calcula el resultado de una lista de tokens (expresión matemática).

        Args:
            tokens (myList): Lista de tokens (números y operadores).

        Returns:
            float: Resultado de la evaluación.

        Raises:
            ZeroDivisionError: Si ocurre una división por cero.
        """
        i = 0
        while i < tokens.getSize():
            token = tokens.getNodeByPos(i).data
            if token in '*/':
                left = float(tokens.getNodeByPos(i-1).data)
                right = float(tokens.getNodeByPos(i+1).data)
                if token == '*':
                    res = left * right
                else:
                    if right == 0:
                        raise ZeroDivisionError("División por cero detectada en la fórmula.")
                    res = left / right
                tokens.removeAt(i-1)  
                tokens.removeAt(i-1)  
                tokens.removeAt(i-1)  
                tokens.insertAt(str(res), i-1)  
                i -= 1  
            i += 1
        if tokens.getSize() == 0:
            return 0
        result = float(tokens.getNodeByPos(0).data)
        i = 1
        while i < tokens.getSize():
            op = tokens.getNodeByPos(i).data
            right = float(tokens.getNodeByPos(i+1).data)
            if op == '+':
                result += right
            elif op == '-':
                result -= right
            i += 2
        return result