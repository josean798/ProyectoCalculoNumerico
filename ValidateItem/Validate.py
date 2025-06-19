from Repositories.numericSystem import numericSystem
import re

def validEnterNumber(number):

    try:
    
        num= numericSystem.NumericSystem()
        num.setNumber(number)
        return num 
    
    except ValueError as e:
        return None

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
    