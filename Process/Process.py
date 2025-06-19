import numpy as np 
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from Repositories.digit import Digit
from Repositories.numericSystem import numericSystem
from ValidateItem.Validate import * 

def iniNumbers(arrayNumbers):

    if arrayNumbers is not None:
        for i in range(len(arrayNumbers)):
            for j in range(len(arrayNumbers[i])):
                arrayNumbers[i][j] = ""

def iniResults(arrayResults):

    if arrayResults is not None:
        for i in range(len(arrayResults)):
            for j in range(len(arrayResults[i])):
                arrayResults[i][j] = ""                


def archiveQuantities(archivo):

    filasCol = np.array([0,0])

    if(archivo == None):
        print("Error al abrir dicho archivo")
        return filasCol

    cont = 0
    band = 0
    aux = 0

    for i in archivo:
        cont += 1
        campos = np.array([campo for campo in i.strip().split("#") if campo != ""], dtype=object)

        if band == 0:
            aux = len(campos)
            band = 1
        elif (len(campos) > aux):
            aux = len(campos)

    filasCol[0] = cont  
    filasCol[1] = aux
    
    return filasCol


def attachData(archivo, arraynumbers):
    archivo.seek(0)
    fila = 0
    for linea in archivo:
        campos = np.array([campo for campo in linea.strip().split("#") if campo != ""], dtype=arraynumbers.dtype)
        for col in range(len(campos)):
            arraynumbers[fila][col] = campos[col]

        for col in range(len(campos), arraynumbers.shape[1]):
            arraynumbers[fila][col] = ""    
        fila += 1
                       
def processArchive(arrayNumbers, arrayResults):
    systems = np.array([], dtype=object)
    
    if arrayNumbers is not None and systems is not None:
        for i in range(len(arrayNumbers)):
            for j in range(len(arrayNumbers[i])):
                text = ""
                error = ""
                numero = arrayNumbers[i][j]
                if numero == "":
                    arrayResults[i][j] = ""
                    arrayNumbers[i][j] = "0"
                    continue
                error, numerico = validEnterNumber(numero.upper())
                if numerico == False:
                    text = f"El numero {numero} no tiene sistema numerico"
                    arrayNumbers[i][j] = "0"
                    arrayResults[i][j] = text
                    print(error)
                else: 
                    text = f"El sistema de {numero} es: {numerico.whichSystemIs()}"
                    systems = numerico.getSystems()
                    for k in range(len(systems)):
                        currentSystem = systems[k]
                        digito = Digit(numero, currentSystem)
                        text = text + f", tiene {digito.getSignificantFigures()} cifras significativas en el sistema {currentSystem}"
                    arrayResults[i][j] = text
     
def processResults(arrayNumbers, arrayResults, archInput, archName, serial):
    
    archiveObject = archInput.getArchive(archName)
    serial = archInput.getSerial(archName)
    filasCol = archiveQuantities(archiveObject)
    filas, columnas = filasCol[0], filasCol[1]
    arrayNumbers = np.empty((filas, columnas), dtype=object)
    arrayResults = np.empty((filas, columnas), dtype=object)
    
    iniNumbers(arrayNumbers)
    iniResults(arrayResults)
    attachData(archiveObject, arrayNumbers)
    processArchive(arrayNumbers, arrayResults)
    
    return arrayNumbers, arrayResults, serial, archiveObject
    
            
        
             
                    





    