import numpy as np 
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from composables.StoreMain import storeMain
from Process.Process import processResults, methodProcess, processFormula, numberProcess
from Repositories.ArchiveUtil import ArchiveUtil
from ValidateItem.Validate import validArchiveName, validContentArchive
from composables.StoreArchive import  createArchiveError, createArchiveListResult
def ProcessMain(routeInput, routeOutput, routeLog, formulaDir, date, errorList, arraysList, listResults):
    arrayNumbers = None
    arrayResults = None
    arrayConverted = None
    archObject = None
    resultGauss = None
    elementalOperations = None
    serial = None
    serialFormula = None
    archiveUtilInput = ArchiveUtil(routeInput)
    archiveUtilOut = ArchiveUtil(routeOutput)
    arhiveUtilLog = ArchiveUtil(routeLog)
    archiveUtilFormula = ArchiveUtil(formulaDir)
    
    
    indexOperations = numberProcess()
    index = methodProcess()
    
    for archiveName in archiveUtilInput.getDirectoriesList():
        if archiveName == ".gitkeep": 
            continue
        if validArchiveName(archiveName) and validContentArchive(archiveUtilInput.getArchive(archiveName), archiveName):

            elementalOperations, resultGauss, arrayNumbers, arrayResults, arrayConverted, serial, archObject, errorList, arraysList = processResults(index, resultGauss, errorList, arraysList, arrayNumbers, arrayResults, arrayConverted, archiveUtilInput, archiveName, serial, date, elementalOperations)
            
            storeMain(arrayResults, serial, archiveUtilOut, arhiveUtilLog, date, errorList, resultGauss, elementalOperations)
            archObject.close()


    for archiveFormulaName in archiveUtilFormula.getDirectoriesList():
        if archiveFormulaName == ".gitkeep":
            continue
        if validArchiveName(archiveFormulaName) and validContentArchive(archiveUtilFormula.getArchive(archiveFormulaName), archiveFormulaName):
            errorList, listResults = processFormula(indexOperations, archiveFormulaName, archiveUtilFormula, date, errorList, arraysList, listResults)
            serialFormula = archiveUtilFormula.getSerial(archiveFormulaName)  
    createArchiveListResult(listResults, archiveUtilOut, serialFormula, date)
    createArchiveError(errorList, arhiveUtilLog, date)