import numpy as np
from Structure.myList import myList
from Structure.myReplace import myReplace

class myNumbers:
    __numbersList = np.array([])
    __A = 0
    __B = 0
    __C = 0
    __formula = ""
    __result = 0

    def __init__(self, numbers, formula):
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
        validChars = "aAbBcC0123456789-+/*()"
        for char in self.__formula:
            if char not in validChars:
                raise ValueError("La fórmula contiene caracteres no válidos")
            
        for i in range(len(self.__formula)-1):
            if self.__formula[i] in '+-*' and self.__formula[i+1] in '+-*':
                raise ValueError("Operadores consecutivos no permitidos")

    def validateNumbers(self):
        for i in range(len(self.__numbersList)):
            if not isinstance(self.__numbersList[i], (float, int)):
                raise ValueError("Los miembros del arreglo deben ser números")

    def replaceFormula(self):
        replacer_a = myReplace(self.__formula)
        formula_with_a = replacer_a.getReplace("a", str(self.__A))
        
        replacer_b = myReplace(formula_with_a)
        formula_with_b = replacer_b.getReplace("b", str(self.__B))
        
        replacer_c = myReplace(formula_with_b)
        formula = replacer_c.getReplace("c", str(self.__C))
        
        return formula

    def evaluate(self):
        self.__result = self.evaluateExpression(self.replaceFormula())
        return self.__result

    def evaluateExpression(self, expr):
        while '(' in expr:
            expr = self.evaluateParentheses(expr)
        tokens = self.tokenize(expr)
        return self.calculate(tokens)

    def evaluateParentheses(self, expr):
        start = expr.rfind('(')
        end = expr.find(')', start)
        if start == -1 or end == -1:
            raise ValueError("Paréntesis no balanceados")
        subExpr = expr[start + 1:end]
        subResult = self.calculate(self.tokenize(subExpr))
        return expr[:start] + str(subResult) + expr[end + 1:]

    def tokenize(self, expr):
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

# Ejemplo de uso con números como string:
numbers = np.array(["10", "2.5", "5"])  
formula = "(2 + A) * B - C"  

calc = myNumbers(numbers, formula)
result = calc.evaluate()
print(f"Resultado de la fórmula {formula}: {result}")