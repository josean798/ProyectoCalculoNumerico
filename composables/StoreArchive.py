from Repositories.digit import Digit
from Repositories.numericSystem import numericSystem 
import numpy as np
from datetime import datetime
from random import randint



def createArchive(arrayResults, archiveUtil, serialArchive):
    randomNumber = randint(1,1000-1)
    time = str(datetime.now().date()).replace(":", "-")
    nameArchive = serialArchive + "_" + time +"_"+"serial"+ str(randomNumber) 

    if arrayResults is not None:
        for i in range(len(arrayResults)):
            for j in range(len(arrayResults[i])):
                if arrayResults[i][j] == "":
                    continue
                else:
                    archiveUtil.setOrCreateFiles(nameArchive, arrayResults[i][j], True)
    
    