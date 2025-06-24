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
                    numerico = numericSystem(number.upper())
                    text = f"El sistema de {number} es: {numerico.whichSystemIs()}"
                    systems = numerico.getSystems()
                    for k in range(len(systems)):
                        currentSystem = systems[k]
                        digito = Digit(number, currentSystem)
                        text = text + f", tiene {digito.getSignificantFigures()} cifras significativas en el sistema {currentSystem}"
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
        solution = f"Infinitas soluciones o no tiene solución"
        return solution

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
    