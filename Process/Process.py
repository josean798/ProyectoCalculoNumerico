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

def iniConverted(arrayConverted):

    if arrayConverted is not None:
        for i in range(len(arrayConverted)):
            for j in range(len(arrayConverted[i])):
                arrayConverted[i][j] = ""

def archiveQuantities(archive):

    filCol = np.array([0,0])

    if(archive == None):
        print("Error al abrir dicho archivo")
        return filCol

    count = 0
    flag = 0
    aux = 0

    for i in archive:
        count += 1
        camp = np.array([camps for camps in i.strip().split("#") if camps != ""], dtype=object)

        if flag == 0:
            aux = len(camp)
            flag = 1
        elif (len(camp) > aux):
            aux = len(camp)

    filCol[0] = count  
    filCol[1] = aux
    
    return filCol


def attachData(archive, arraynumbers):
    archive.seek(0)
    fil = 0
    for linea in archive:
        campos = np.array([campo for campo in linea.strip().split("#") if campo != ""], dtype=arraynumbers.dtype)
        for col in range(len(campos)):
            arraynumbers[fil][col] = campos[col]

        for col in range(len(campos), arraynumbers.shape[1]):
            arraynumbers[fil][col] = ""    
        fil += 1

def numberProcess():
    text = "Como prefiere operar \n1.Con numeros \n2.Matrices"
    index = validInput(text)
    return index

def methodProcess():
    text = "Ingrese que metodo desea usar: \n1. Gauss Jordan\n2. Gauss Seidel\nIngrese el indice: "
    index = validInput(text)
    return index

def processArchive(arrayNumbers, arrayResults, arrayConverted, errorList, arraysList, serial, date):


    if arrayNumbers is not None and arrayResults is not None:
        arrayNumbers, arrayResults, arrayConverted = validEnterNumber(arrayNumbers, arrayResults, arrayConverted, serial, date, errorList)
        arraysList.insert(arrayConverted)
        
def methodSelected(index, arrayConverted, errorList, serial, date):
    result = None
    if index == 1:
        result = validMatrixGaussJordan(arrayConverted, errorList, serial, date)
        return result
    elif index == 2:
        result = validMatrixGaussSeidel(arrayConverted, errorList, serial, date)
        return result
def elementalOperations(arrayConverted, errorList, serial, date):
    elementalResult = validElementalMatrixOperations(arrayConverted, errorList, serial, date)
    return elementalResult

def processResults(index, result, errorList, arraysList, arrayNumbers, arrayResults, arrayConverted, archInput, archName, serial, date, elementalResult):

    archiveObject = archInput.getArchive(archName)
    serial = archInput.getSerial(archName)
    filcol = archiveQuantities(archiveObject)
    fil, col = filcol[0], filcol[1]
    arrayNumbers = np.empty((fil, col), dtype=object)
    arrayResults = np.empty((fil, col), dtype=object)
    arrayConverted = np.empty((fil, col), dtype=object)
    
    iniNumbers(arrayNumbers)
    iniResults(arrayResults)
    iniConverted(arrayConverted)
    attachData(archiveObject, arrayNumbers)
    processArchive(arrayNumbers, arrayResults, arrayConverted, errorList, arraysList, serial, date)
    elementalResult = elementalOperations(arrayConverted, errorList, serial, date)
    result = methodSelected(index, arrayConverted, errorList, serial, date)
    return elementalResult,result, arrayNumbers, arrayResults, arrayConverted, serial, archiveObject, errorList, arraysList
