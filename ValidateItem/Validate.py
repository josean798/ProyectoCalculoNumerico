import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from Repositories.numericSystem import * 
from Repositories.digit import *
from Repositories.elementalOperations import *
from Repositories.translator import *
from Structure.myReplace import myReplace  
from Repositories.gaussJordan import *
from Repositories.gaussSeidel import * 
from Repositories.matrixOperations import *
import re
import numpy as np 
from Repositories.myNumbers import myNumbers
from Repositories.myMatrix import MyMatrix

def validErrorRegister(errorList, serial, errorName, exception, data, location, date):
    if errorList is None:
        print("Error: La estructura de errores no está inicializada.")
        return
    if not serial or not isinstance(serial, str):
        print("Error: Serial inválido para el registro de error.")
        return
    if not errorName or not isinstance(errorName, str):
        print("Error: Nombre de error inválido.")
        return
    if not exception or not isinstance(exception, str):
        print("Error: Excepción inválida.")
        return
    if data is None:
        print("Error: Dato inválido para el registro de error.")
        return
    if not location or not isinstance(location, str):
        print("Error: Ubicación inválida para el registro de error.")
        return
    

    error = f"{errorName}_{date}_{serial}:[{exception}/{data}/{location}]"
    errorList.insert(error)


def validEnterNumber(arrayNumbers, arrayResults, arrayConverted, serial, date, errorList):
    systems = np.array([], dtype=object)
    
    if arrayNumbers is not None and systems is not None:
        for i in range(len(arrayNumbers)):
            for j in range(len(arrayNumbers[i])):
                text = ""
                number = arrayNumbers[i][j]
                try:
                    if isinstance(number, str):
                        if ',' in number and '.' not in number:
                            replace = myReplace(number)
                            number = replace.getReplace(',', '.')                            
                    if number == "":
                        arrayResults[i][j] = ""
                        arrayNumbers[i][j] = "0"
                        arrayConverted[i][j] = "0"
                        continue
                    numeric = numericSystem(number.upper())
                    text = f"El sistema de {number} es: {numeric.whichSystemIs()}"
                    systems = numeric.getSystems()
                    for k in range(len(systems)):
                        currentSystem = systems[k]
                        digit = Digit(number, currentSystem)
                        text = text + f", tiene {digit.getSignificantFigures()} cifras significativas en el sistema {currentSystem}"
                        elemental = ElementalOperations(number.upper(), currentSystem)
                        text = text + f", operaciones elementales: {elemental.finalResult()}"
                    arrayResults[i][j] = text
                    auxTras = translator(number)
                    auxTras.translate()
                    auxNumber = auxTras.getNumber()
                    arrayConverted[i][j] = auxNumber
                except Exception as e:
                    errorName = type(e).__name__
                    exception = str(e)
                    data = f"{number}"
                    location = f"validEnterNumber()"
                    validErrorRegister(errorList, serial, errorName , exception, data, location, date)
                    arrayResults[i][j] = f"El numero {number} no tiene sistema numerico"
                    arrayNumbers[i][j] = "0"
                    arrayConverted[i][j] = "0"
                
    return arrayNumbers, arrayResults, arrayConverted

def validInput(text):
    while True:
        try:
            userInput = int(input(text).strip())
            if not userInput:
                raise ValueError("El valor ingresado no puede estar vacío.")
            if userInput < 0:
                raise ValueError("El valor ingresado debe ser un número entero positivo.")
            if userInput > 2:
                raise ValueError("El valor ingresado debe ser 1 o 2.")
            return userInput
        except ValueError as e:
            print(f"Error: {e}")
            print("Por favor, intente nuevamente.")
            
def validElementalMatrixOperations(arrayConverted, errorList, serial, date):    
    try:
        elemental = matrixOperations(arrayConverted)
        elemental.randomOperations()
        result = elemental.getResults()
        return result
    except Exception as e:
        errorName = type(e).__name__
        exception = str(e)
        data = f"{' '.join(str(x) for fila in arrayConverted for x in fila)}"
        location = f"validElementalOperations()"
        validErrorRegister(errorList, serial, errorName , exception, data, location, date)
        result = f"Error en las operaciones elementales"
        return result

def validMatrixGaussJordan(arrayConverted, errorList, serial, date):
    try:
        solver = GaussJordan(arrayConverted)
        solution = solver.solve()
        return solution
    except Exception as e:
        errorName = type(e).__name__
        exception = str(e)
        data = f"{' '.join(str(x) for fila in arrayConverted for x in fila)}"
        location = f"validMatrixGaussJordan()"
        validErrorRegister(errorList, serial, errorName , exception, data, location, date)
        sol = f"Infinitas soluciones o no tiene solución"
        return sol

def validMatrixGaussSeidel(arrayConverted, errorList, serial, date): 
    try:
        solver = GaussSeidel(arrayConverted)
        solution = solver.solve()
        return solution
    except Exception as e:
        errorName = type(e).__name__
        exception = str(e)
        data = f"{' '.join(str(x) for fila in arrayConverted for x in fila)}"
        location = f"validMatrixGaussSeidel()"
        validErrorRegister(errorList, serial, errorName , exception, data, location, date)
        solution = f"La matriz no es cuadrada"
        return solution

def validArchiveName(archiveName):
    if re.search(r'^.+_.+_serial\d+\.bin$', archiveName):
        return True  
    else:
        print(f"Error: Archivo ingresado con nonbre incorrecto o vacio")
        print(f"Verifique que el nombre es formato: Nombre_Fecha(xx/xx/20xx)_Serialxx.bin")
        print(f"El nombre ingresado es: {archiveName}")
        return False    

def validContentArchive(archive, archiveName):
    archive.seek(0)
    content = archive.read().strip()
    if not content:
        print("Error: Hay un archivo vacio.")
        print(f"Verifique que el archivo {archiveName} no este vacio")
        return False
    return True

def validConvertToFloat(arrayConverted, errorList, serial, date):
    try:
        floatMatrix = np.empty(arrayConverted.shape, dtype=float)

        for r in range(len(arrayConverted)):
            for c in range(len(arrayConverted[0])):
                floatMatrix[r, c] = float(arrayConverted[r, c])
    except Exception as e:
        errorName = type(e).__name__
        exception = str(e)
        data = f"{' '.join(str(x) for fila in arrayConverted for x in fila)}"
        location = f"validConvertToFloat()"
        validErrorRegister(errorList, serial, errorName , exception, data, location, date)
        floatMatrix = np.empty(arrayConverted.shape, dtype=float)    
    return floatMatrix



def validProcessByNumbers(arraysList, arrayFormulas, listResults, errorList, serial, date):
    try:
        nodo = arraysList.getNode()
        while nodo is not None:
            matriz = nodo.data
            for fila in matriz:
                n = len(fila)
                num_minis = n // 3 + (1 if n % 3 != 0 else 0)
                mini_arreglos = np.empty((num_minis, 3), dtype=object)
                for idx, i in enumerate(range(0, n, 3)):
                    for j in range(3):
                        if i + j < n:
                            mini_arreglos[idx, j] = fila[i + j]
                        else:
                            mini_arreglos[idx, j] = "0"
                for fidx in range(arrayFormulas.shape[0]):
                    formula = str(arrayFormulas[fidx][0])
                    for mini in mini_arreglos:
                        calc = myNumbers(mini, formula)
                        resultado = calc.evaluate()  
                        text = f"Resultado para {mini} con fórmula '{formula}': {resultado}"
                        listResults.insert(text)
            nodo = nodo.next
    except Exception as e:    
        errorName = type(e).__name__
        exception = str(e)
        data = f"{' '.join(str(x) for fila in arraysList for x in fila)}"
        location = f"validProcessByNumbers()"
        validErrorRegister(errorList, serial, errorName , exception, data, location, date)
    return listResults    

def validProcessByMatrix(arraysList, arrayFormulas, listResults, errorList, serial, date):
    try:
        
        
        nodo = arraysList.getNode()
        
        matrizA = nodo.data
        matrizB = nodo.next.data
        matrizC = nodo.next.next.data
        matrizA = validConvertToFloat(matrizA, errorList, serial, date)
        matrizB = validConvertToFloat(matrizB, errorList, serial, date)
        matrizC = validConvertToFloat(matrizC, errorList, serial, date)
        for fidx in range(arrayFormulas.shape[0]):
            
            
            formula = str(arrayFormulas[fidx][0])
            
            calc = MyMatrix(matrizA, matrizB, matrizC, formula)
            resultado = calc.evaluate()
                
            text = f"Resultado para fórmula '{formula}': {resultado}"
                
            listResults.insert(text)
            
    except Exception as e:
        errorName = type(e).__name__
        exception = str(e)
        data = "No se pudieron extraer tres matrices de arraysList"
        location = "validProcessByMatrix()"
        validErrorRegister(errorList, serial, errorName, exception, data, location, date)
        text = f"No se pudo procesar: {str(e)}"
        listResults.insert(text)

    return listResults