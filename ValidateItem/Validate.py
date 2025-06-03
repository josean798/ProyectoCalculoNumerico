from Repositories import Repositories

def validEnterNumber(number):

    try:
    
        num= Repositories.numericSystem.NumericSystem()
        num.setNumber(number)
        return num 
    
    except ValueError as e:
        return None


        