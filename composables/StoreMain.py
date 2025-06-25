from composables.StoreArchive import createArchive, createArchiveError, createArchiveListResult


def storeMain(arrayResults, serial, archiveUtil, date, resultGauss, elementalOperations):   

    createArchive(arrayResults, archiveUtil, serial, resultGauss, elementalOperations, date)
   
