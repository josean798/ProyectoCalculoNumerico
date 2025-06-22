import numpy as np 
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from datetime import datetime
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
                       
def processArchive(arrayNumbers, arrayResults, serial, date):
    
    
    if arrayNumbers is not None and arrayResults is not None:
        arrayNumbers, arrayResults = validEnterNumber(arrayNumbers, arrayResults, serial, date)
     
def processResults(arrayNumbers, arrayResults, archInput, archName, serial):
    
    archiveObject = archInput.getArchive(archName)
    serial = archInput.getSerial(archName)
    filasCol = archiveQuantities(archiveObject)
    filas, columnas = filasCol[0], filasCol[1]
    arrayNumbers = np.empty((filas, columnas), dtype=object)
    arrayResults = np.empty((filas, columnas), dtype=object)
    date = str(datetime.now().date()).replace(":", "-")
    
    iniNumbers(arrayNumbers)
    iniResults(arrayResults)
    attachData(archiveObject, arrayNumbers)
    processArchive(arrayNumbers, arrayResults, serial, date)
    
    return arrayNumbers, arrayResults, serial, archiveObject
