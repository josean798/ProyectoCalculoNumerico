class translator:

    __num=""

    def __init__(self, number):
        if not isinstance(number, str):
            raise ValueError("El input debe ser un string")
        self.__num = number
        self.validateNum()

    def validateNum(self):
        validChars = set("0123456789abcdefABCDEF")
        if not all(char in validChars for char in self.__num):
            raise ValueError("El input debe ser un número hexadecimal válido")

    def translator(self):
        counter=0
        newNum = 0
        for number in self.__num[::-1]:
            if number=="A" or number=="a":
                number = 10
            elif number=="B" or number=="b":
                number = 11
            elif number=="C" or number=="c":
                number = 12
            elif number=="D" or number=="d":
                number = 13
            elif number=="E" or number=="e":
                number = 14
            elif number=="F" or number=="f":
                number = 15
            newNum += int(number) * (16 ** counter)
            counter += 1
            print(newNum)
        self.__num = str(newNum)

    def getNumber(self):
        return self.__num