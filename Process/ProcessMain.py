import numpy as np 
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from composables.StoreMain import storeMain
from Process.Process import processResults
from Repositories.ArchiveUtil import ArchiveUtil
from ValidateItem.Validate import validArchiveName, validContentArchive

def ProcessMain(routeInput, routeOutput, date):
    arrayNumbers = None
    arrayResults = None
    archObject = None
    serial = None
    archiveUtilInput = ArchiveUtil(routeInput)
    archiveUtilOut = ArchiveUtil(routeOutput)
    
    for archiveName in archiveUtilInput.getDirectoriesList():
        if archiveName == ".gitkeep": 
            continue
        if validArchiveName(archiveName) and validContentArchive(archiveUtilInput.getArchive(archiveName), archiveName):
            
            arrayNumbers, arrayResults, serial, archObject = processResults(arrayNumbers, arrayResults, archiveUtilInput, archiveName, serial)
                
            storeMain(arrayResults, serial, archiveUtilOut, date)
            archObject.close()
    
    
    
    
   