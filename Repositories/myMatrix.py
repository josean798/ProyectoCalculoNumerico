import numpy as np
from Structure.stack import Stack
from Structure.myQueue import Queue
from Structure.myReplace import myReplace

class MyMatrix:
    def __init__(self, matrizA, matrizB, matrizC, formula):
        self._matrizA = matrizA
        self._matrizB = matrizB
        self._matrizC = matrizC
        formula_replacer_space = myReplace(formula)
        self._formula = formula_replacer_space.getReplace(" ", "").lower()
        self.validate()

    def validate(self):
        if not all(isinstance(m, np.ndarray) for m in [self._matrizA, self._matrizB, self._matrizC]):
            raise ValueError("Las matrices deben ser numpy arrays")
        if not all(c in "abc0123456789+-*/()" for c in self._formula):
            raise ValueError("Caracteres inválidos en la fórmula")

    def getMatrix(self, char):
        if char == 'a': return self._matrizA
        if char == 'b': return self._matrizB
        if char == 'c': return self._matrizC
        try:
            return float(char)
        except ValueError:
            raise ValueError(f"Operando inválido: '{char}'")

    def shuntingYard(self):
        precedence = {'*': 3, '/': 3, '+': 2, '-': 2}
        output = Queue()
        operators = Stack()
        i = 0

        while i < len(self._formula):
            token = self._formula[i]
            
            if token.isdigit() or (token == '-' and (i == 0 or self._formula[i-1] in '+-*/(')):
                j = i + 1
                while j < len(self._formula) and (self._formula[j].isdigit() or self._formula[j] == '.'):
                    j += 1
                output.enqueue(self._formula[i:j])
                i = j
                continue
            
            elif token in {'a', 'b', 'c'}:
                output.enqueue(token)
                i += 1
            
            elif token == '(':
                operators.push(token)
                i += 1
            elif token == ')':
                while not operators.is_empty() and operators.peek() != '(':
                    output.enqueue(operators.pop())
                operators.pop()  
                i += 1
            
            elif token in '+-*/':
                while (not operators.is_empty() and 
                       operators.peek() != '(' and 
                       precedence[operators.peek()] >= precedence[token]):
                    output.enqueue(operators.pop())
                operators.push(token)
                i += 1

        while not operators.is_empty():
            output.enqueue(operators.pop())

        return output

    def evaluateRpn(self, rpnQueue):
        stack = Stack()

        while not rpnQueue.isEmpty():
            token = rpnQueue.dequeue()

            if token in {'a', 'b', 'c'}:
                stack.push(self.getMatrix(token))
            elif token.replace('-', '').replace('.', '').isdigit():
                stack.push(float(token))
            elif token in '+-*/':
                if stack.size() < 2:
                    raise ValueError("Faltan operandos")
                right = stack.pop()
                left = stack.pop()
                stack.push(self.performOperation(left, right, token))

        if stack.size() != 1:
            raise ValueError("Expresión mal formada")
        return stack.pop()

    def performOperation(self, left, right, operator):
    
        if isinstance(left, np.ndarray) and isinstance(right, np.ndarray):
            if operator == '+': 
                if left.shape != right.shape:
                    raise ValueError("Dimensiones incompatibles para suma, { (m, n), (p, q) } donde (m, n) ≠ (p, q)")
                return left + right
            elif operator == '-':
                if left.shape != right.shape:
                    raise ValueError("Dimensiones incompatibles para resta, { (m, n), (p, q) } donde (m, n) ≠ (p, q)")
                return left - right
            elif operator == '*':
                if left.shape[1] != right.shape[0]:
                    raise ValueError("Dimensiones incompatibles para multiplicación: { (m, n), (p, q) } donde n ≠ p")
                return np.dot(left, right)
            elif operator == '/':
                try:
                    return np.dot(left, np.linalg.inv(right))
                except np.linalg.LinAlgError:
                    raise ValueError("Matriz no invertible: no se puede calcular la inversa de la matriz { (p, q) }")
        
        elif isinstance(left, np.ndarray) and isinstance(right, (int, float)):
            if operator == '*': return left * right
            elif operator == '/': return left / right
        
        elif isinstance(left, (int, float)) and isinstance(right, np.ndarray):
            if operator == '*': return left * right
            else: raise ValueError("Operación no soportada entre escalar y matriz: { escalar, (m, n) }")
        
        else:
            if operator == '+': return left + right
            elif operator == '-': return left - right
            elif operator == '*': return left * right
            elif operator == '/': 
                if right == 0: raise ValueError("División por cero")
                return left / right

    def evaluate(self):
        rpnQueue = self.shuntingYard()
        return self.evaluateRpn(rpnQueue)

