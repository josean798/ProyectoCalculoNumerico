from composables.StoreArchive import createArchive, createArchiveError


def storeMain(arrayResults, serial, archiveUtil, routeLog, date, errorList, resultGauss, elementalOperations):

    createArchive(arrayResults, archiveUtil, serial, resultGauss, elementalOperations, date)
    createArchiveError(errorList, routeLog, date)
