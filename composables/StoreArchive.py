from random import randint



def createArchive(arrayResults, archiveUtil, serialArchive, resultGauss,  elementalOperations, date):
    randomNumber = randint(1,1000-1)
    nameArchive = serialArchive + "_" + date +"_"+"serial"+ str(randomNumber)+".txt" 
    textElemental = ""
    textGauss = ""
    if arrayResults is not None:
        for i in range(len(arrayResults)):
           
            for j in range(len(arrayResults[i])):
                if arrayResults[i][j] == "":
                    continue
                else:
                    archiveUtil.setOrCreateFiles(nameArchive, arrayResults[i][j], True)
        
        for i in range(len(elementalOperations)):
            textElemental += elementalOperations[i] + ", "
        
        for i in range(len(resultGauss)):
            textGauss += str(resultGauss[i]) + ", "
                
        textElemental = f"Operaciones elementales:{textElemental}"
        textGauss = f"Resultados de Gauss:{textGauss}"
        archiveUtil.setOrCreateFiles(nameArchive, textElemental, True)
        archiveUtil.setOrCreateFiles(nameArchive, textGauss, True)

def createArchiveError(errorList, routeLog, date):
    randomNumber = randint(1,1000-1)
    nameArchive = "ErrorArchive" + "_" + date +"_"+"serial"+ str(randomNumber)+".log" 

    if errorList is not None:
        for error in errorList:
            routeLog.setOrCreateFiles(nameArchive, error, True)

def createArchiveListResult(listResults, archiveUtil, serialArchive, date):
    randomNumber = randint(1,1000-1)
    nameArchive = serialArchive + "_" + date +"_"+"serial"+ str(randomNumber)+".txt" 
    if listResults is not None:
        for result in listResults:
            archiveUtil.setOrCreateFiles(nameArchive, result, True)