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
                       
def processArchive(arrayNumbers, arrayResults, serial, date):
    
    
    if arrayNumbers is not None and arrayResults is not None:
        arrayNumbers, arrayResults = validEnterNumber(arrayNumbers, arrayResults, serial, date)
     
def processResults(arrayNumbers, arrayResults, archInput, archName, serial, date):
    
    archiveObject = archInput.getArchive(archName)
    serial = archInput.getSerial(archName)
    filcol = archiveQuantities(archiveObject)
    fil, col = filcol[0], filcol[1]
    arrayNumbers = np.empty((fil, col), dtype=object)
    arrayResults = np.empty((fil, col), dtype=object)
    
    
    iniNumbers(arrayNumbers)
    iniResults(arrayResults)
    attachData(archiveObject, arrayNumbers)
    processArchive(arrayNumbers, arrayResults, serial, date)
    
    return arrayNumbers, arrayResults, serial, archiveObject
