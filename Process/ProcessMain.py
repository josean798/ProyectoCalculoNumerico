import numpy as np 
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from composables.StoreMain import storeMain
from Process.Process import processResults, methodProcess
from Repositories.ArchiveUtil import ArchiveUtil
from ValidateItem.Validate import validArchiveName, validContentArchive

def ProcessMain(routeInput, routeOutput, routeLog, date, errorList, arraysList):
    arrayNumbers = None
    arrayResults = None
    arrayConverted = None
    archObject = None
    resultGauss = None
    elementalOperations = None
    serial = None
    archiveUtilInput = ArchiveUtil(routeInput)
    archiveUtilOut = ArchiveUtil(routeOutput)
    arhiveUtilLog = ArchiveUtil(routeLog)
    
    index = methodProcess()
    for archiveName in archiveUtilInput.getDirectoriesList():
        if archiveName == ".gitkeep": 
            continue
        if validArchiveName(archiveName) and validContentArchive(archiveUtilInput.getArchive(archiveName), archiveName):

            elementalOperations, resultGauss, arrayNumbers, arrayResults, arrayConverted, serial, archObject, errorList, arraysList = processResults(index, resultGauss, errorList, arraysList, arrayNumbers, arrayResults, arrayConverted, archiveUtilInput, archiveName, serial, date, elementalOperations)
            
            storeMain(arrayResults, serial, archiveUtilOut, arhiveUtilLog, date, errorList, resultGauss, elementalOperations)
            archObject.close()

    for i in errorList:
        print(i)