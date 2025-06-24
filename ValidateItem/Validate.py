from Repositories.numericSystem import * 
from Repositories.digit import *
from Repositories.elementalOperations import *
import re
import numpy as np 

def validEnterNumber(arrayNumbers, arrayResults, serial, date):
    systems = np.array([], dtype=object)
    
    if arrayNumbers is not None and systems is not None:
        for i in range(len(arrayNumbers)):
            for j in range(len(arrayNumbers[i])):
                text = ""
                number = arrayNumbers[i][j]
                try:
                    if isinstance(number, str):
                        if ',' in number and '.' not in number:
                            replace = myReplace(number)
                            number = replace.getReplace(',', '.')                            
                    if number == "":
                        arrayResults[i][j] = ""
                        arrayNumbers[i][j] = "0"
                        continue
                    numerico = numericSystem(number.upper())
                    text = f"El sistema de {number} es: {numerico.whichSystemIs()}"
                    systems = numerico.getSystems()
                    for k in range(len(systems)):
                        currentSystem = systems[k]
                        digito = Digit(number, currentSystem)
                        text = text + f", tiene {digito.getSignificantFigures()} cifras significativas en el sistema {currentSystem}"
                        elemental = ElementalOperations(number.upper(), currentSystem)
                        text = text + f", operaciones elementales: {elemental.finalResult()}"
                    arrayResults[i][j] = text
                except Exception as e:
                    nameError = type(e).__name__
                    exception = str(e)
                    data = f"{number}"
                    location = f"Fila: {i}, Colimna: {j}"
                    error = f"{nameError}_{date}_{serial}:[{exception}/{data}/{location}]"
                    print(error)    
                    arrayResults[i][j] = f"El numero {number} no tiene sistema numerico"
                    arrayNumbers[i][j] = "0"
                
    return arrayNumbers, arrayResults

def validArchiveName(archiveName):
    if re.search(r'^.+_.+_serial\d+\.bin$', archiveName):
        return True  
    else:
        print(f"Error: Archivo ingresado con nonbre incorrecto o vacio")
        print(f"Verifique que el nombre es formato: Nombre_Fecha(xx/xx/20xx)_Serialxx.bin")
        print(f"El nombre ingresado es: {archiveName}")
        return False    

def validContentArchive(archive, archiveName):
    archive.seek(0)
    content = archive.read().strip()
    if not content:
        print("Error: Hay un archivo vacio.")
        print(f"Verifique que el archivo {archiveName} no este vacio")
        return False
    return True
    