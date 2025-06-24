import time

class myDate:
    
    __year = 0
    __month = 0
    __day = 0
    __hour = 0
    __minute = 0
    __second = 0
    __microsecond = 0
    
    def __init__(self, year: int,month: int,day: int,hour: int = 0,minute: int = 0,second: int = 0,microsecond: int = 0):
        self.__year = self.__validateYear(year)
        self.__month = self.__validateMonth(month)
        self.__day = self.__validateDay(day, month, year)
        self.__hour = self.__validateHour(hour)
        self.__minute = self.__validateMinute(minute)
        self.__second = self.__validateSecond(second)
        self.__microsecond = self.__validateMicrosecond(microsecond)
    
    @property
    def getYear(self) -> int:
        return self.__year
    
    @property
    def getMonth(self) -> int:
        return self.__month
    
    @property
    def getDay(self) -> int:
        return self.__day
    
    @property
    def getHour(self) -> int:
        return self.__hour
    
    @property
    def getMinute(self) -> int:
        return self.__minute
    
    @property
    def getSecond(self) -> int:
        return self.__second
    
    @property
    def getMicrosecond(self) -> int:
        return self.__microsecond
    
    def setYear(self, year: int):
        self.__year = self.__validateYear(year)
    
    def setMonth(self, month: int):
        original_day = self.__day
        self.__month = self.__validateMonth(month)
        self.__day = self.__validateDay(original_day, month, self.__year)
    
    def setDay(self, day: int):
        self.__day = self.__validateDay(day, self.__month, self.__year)
    
    def setHour(self, hour: int):
        self.__hour = self.__validateHour(hour)
    
    def setMinute(self, minute: int):
        self.__minute = self.__validateMinute(minute)
    
    def setSecond(self, second: int):
        self.__second = self.__validateSecond(second)
    
    def setMicrosecond(self, microsecond: int):
        self.__microsecond = self.__validateMicrosecond(microsecond)
    
    def __validateYear(self, year: int) -> int:
        if not isinstance(year, int):
            raise TypeError("El año debe ser un entero")
        if year < 1:
            raise ValueError("El año no puede ser menor que 1")
        return year
    
    def __validateMonth(self, month: int) -> int:
        if not isinstance(month, int):
            raise TypeError("El mes debe ser un entero")
        if not 1 <= month <= 12:
            raise ValueError("El mes debe estar entre 1 y 12")
        return month
    
    def __validateDay(self, day: int, month: int, year: int) -> int:
        if not isinstance(day, int):
            raise TypeError("El día debe ser un entero")
        
        daysInMonth = self.__getDaysInMonth(month, year)
        
        if not 1 <= day <= daysInMonth:
            raise ValueError(f"El día debe estar entre 1 y {daysInMonth} para el mes {month}")
        return day
    
    def __validateHour(self, hour: int) -> int:
        if not isinstance(hour, int):
            raise TypeError("La hora debe ser un entero")
        if not 0 <= hour <= 23:
            raise ValueError("La hora debe estar entre 0 y 23")
        return hour
    
    def __validateMinute(self, minute: int) -> int:
        if not isinstance(minute, int):
            raise TypeError("Los minutos deben ser un entero")
        if not 0 <= minute <= 59:
            raise ValueError("Los minutos deben estar entre 0 y 59")
        return minute
    
    def __validateSecond(self, second: int) -> int:
        if not isinstance(second, int):
            raise TypeError("Los segundos deben ser un entero")
        if not 0 <= second <= 59:
            raise ValueError("Los segundos deben estar entre 0 y 59")
        return second
    
    def __validateMicrosecond(self, microsecond: int) -> int:
        if not isinstance(microsecond, int):
            raise TypeError("Los microsegundos deben ser un entero")
        if not 0 <= microsecond <= 999999:
            raise ValueError("Los microsegundos deben estar entre 0 y 999999")
        return microsecond
    
    def __getDaysInMonth(self, month: int, year: int) -> int:
        if month in {4, 6, 9, 11}:
            return 30
        elif month == 2:
            return 29 if self.__isLeapYear(year) else 28
        else:
            return 31
    
    def __isLeapYear(self, year: int) -> bool:
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        else:
            return year % 400 == 0
    
    @classmethod
    def now(cls):
        currentTime = time.time()
        localTime = time.localtime(currentTime)
        
        return cls(year=localTime.tm_year,month=localTime.tm_mon,day=localTime.tm_mday,hour=localTime.tm_hour,minute=localTime.tm_min,second=localTime.tm_sec,microsecond=int((currentTime - int(currentTime)) * 1e6))
    
    def __str__(self):
        return (f"{self.__year}-{self.__month:02d}-{self.__day:02d} "f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}."f"{self.__microsecond:06d}")
    
    def __repr__(self):
        return (f"MyDate(year={self.__year}, month={self.__month}, day={self.__day}, "f"hour={self.__hour}, minute={self.__minute}, second={self.__second}, "f"microsecond={self.__microsecond})")