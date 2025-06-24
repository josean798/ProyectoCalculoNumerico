from random import randint



def createArchive(arrayResults, archiveUtil, serialArchive, date):
    randomNumber = randint(1,1000-1)
    nameArchive = serialArchive + "_" + date +"_"+"serial"+ str(randomNumber)+".txt" 

    if arrayResults is not None:
        for i in range(len(arrayResults)):
            for j in range(len(arrayResults[i])):
                if arrayResults[i][j] == "":
                    continue
                else:
                    archiveUtil.setOrCreateFiles(nameArchive, arrayResults[i][j], True)
    
    