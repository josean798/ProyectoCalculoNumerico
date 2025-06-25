import time

class myDate:
    """
    Clase para representar y validar fechas y horas personalizadas.

    Atributos:
        __year (int): Año.
        __month (int): Mes.
        __day (int): Día.
        __hour (int): Hora.
        __minute (int): Minuto.
        __second (int): Segundo.
        __microsecond (int): Microsegundo.
    """

    __year = 0
    __month = 0
    __day = 0
    __hour = 0
    __minute = 0
    __second = 0
    __microsecond = 0

    def __init__(self, year: int, month: int, day: int, hour: int = 0, minute: int = 0, second: int = 0, microsecond: int = 0):
        """
        Inicializa un objeto myDate con validación de cada campo.

        Args:
            year (int): Año.
            month (int): Mes.
            day (int): Día.
            hour (int, opcional): Hora. Por defecto 0.
            minute (int, opcional): Minuto. Por defecto 0.
            second (int, opcional): Segundo. Por defecto 0.
            microsecond (int, opcional): Microsegundo. Por defecto 0.

        Raises:
            TypeError: Si algún argumento no es entero.
            ValueError: Si algún argumento está fuera de rango o la fecha no es válida.
        """
        self.__year = self.__validateYear(year)
        self.__month = self.__validateMonth(month)
        self.__day = self.__validateDay(day, month, year)
        self.__hour = self.__validateHour(hour)
        self.__minute = self.__validateMinute(minute)
        self.__second = self.__validateSecond(second)
        self.__microsecond = self.__validateMicrosecond(microsecond)

    @property
    def getYear(self) -> int:
        """
        Devuelve el año.

        Returns:
            int: Año.
        """
        return self.__year

    @property
    def getMonth(self) -> int:
        """
        Devuelve el mes.

        Returns:
            int: Mes.
        """
        return self.__month

    @property
    def getDay(self) -> int:
        """
        Devuelve el día.

        Returns:
            int: Día.
        """
        return self.__day

    @property
    def getHour(self) -> int:
        """
        Devuelve la hora.

        Returns:
            int: Hora.
        """
        return self.__hour

    @property
    def getMinute(self) -> int:
        """
        Devuelve los minutos.

        Returns:
            int: Minutos.
        """
        return self.__minute

    @property
    def getSecond(self) -> int:
        """
        Devuelve los segundos.

        Returns:
            int: Segundos.
        """
        return self.__second

    @property
    def getMicrosecond(self) -> int:
        """
        Devuelve los microsegundos.

        Returns:
            int: Microsegundos.
        """
        return self.__microsecond

    def setYear(self, year: int):
        """
        Asigna un nuevo año, validando el valor.

        Args:
            year (int): Año.

        Raises:
            TypeError: Si el año no es entero.
            ValueError: Si el año es menor que 1.
        """
        self.__year = self.__validateYear(year)

    def setMonth(self, month: int):
        """
        Asigna un nuevo mes, validando el valor y ajustando el día si es necesario.

        Args:
            month (int): Mes.

        Raises:
            TypeError: Si el mes no es entero.
            ValueError: Si el mes no está entre 1 y 12.
        """
        original_day = self.__day
        self.__month = self.__validateMonth(month)
        self.__day = self.__validateDay(original_day, month, self.__year)

    def setDay(self, day: int):
        """
        Asigna un nuevo día, validando el valor.

        Args:
            day (int): Día.

        Raises:
            TypeError: Si el día no es entero.
            ValueError: Si el día no es válido para el mes y año actuales.
        """
        self.__day = self.__validateDay(day, self.__month, self.__year)

    def setHour(self, hour: int):
        """
        Asigna una nueva hora, validando el valor.

        Args:
            hour (int): Hora.

        Raises:
            TypeError: Si la hora no es entera.
            ValueError: Si la hora no está entre 0 y 23.
        """
        self.__hour = self.__validateHour(hour)

    def setMinute(self, minute: int):
        """
        Asigna un nuevo minuto, validando el valor.

        Args:
            minute (int): Minuto.

        Raises:
            TypeError: Si el minuto no es entero.
            ValueError: Si el minuto no está entre 0 y 59.
        """
        self.__minute = self.__validateMinute(minute)

    def setSecond(self, second: int):
        """
        Asigna un nuevo segundo, validando el valor.

        Args:
            second (int): Segundo.

        Raises:
            TypeError: Si el segundo no es entero.
            ValueError: Si el segundo no está entre 0 y 59.
        """
        self.__second = self.__validateSecond(second)

    def setMicrosecond(self, microsecond: int):
        """
        Asigna un nuevo microsegundo, validando el valor.

        Args:
            microsecond (int): Microsegundo.

        Raises:
            TypeError: Si el microsegundo no es entero.
            ValueError: Si el microsegundo no está entre 0 y 999999.
        """
        self.__microsecond = self.__validateMicrosecond(microsecond)

    def __validateYear(self, year: int) -> int:
        """
        Valida el año.

        Args:
            year (int): Año.

        Returns:
            int: Año validado.

        Raises:
            TypeError: Si el año no es entero.
            ValueError: Si el año es menor que 1.
        """
        if not isinstance(year, int):
            raise TypeError("El año debe ser un entero")
        if year < 1:
            raise ValueError("El año no puede ser menor que 1")
        return year

    def __validateMonth(self, month: int) -> int:
        """
        Valida el mes.

        Args:
            month (int): Mes.

        Returns:
            int: Mes validado.

        Raises:
            TypeError: Si el mes no es entero.
            ValueError: Si el mes no está entre 1 y 12.
        """
        if not isinstance(month, int):
            raise TypeError("El mes debe ser un entero")
        if not 1 <= month <= 12:
            raise ValueError("El mes debe estar entre 1 y 12")
        return month

    def __validateDay(self, day: int, month: int, year: int) -> int:
        """
        Valida el día según el mes y el año.

        Args:
            day (int): Día.
            month (int): Mes.
            year (int): Año.

        Returns:
            int: Día validado.

        Raises:
            TypeError: Si el día no es entero.
            ValueError: Si el día no es válido para el mes y año dados.
        """
        if not isinstance(day, int):
            raise TypeError("El día debe ser un entero")
        daysInMonth = self.__getDaysInMonth(month, year)
        if not 1 <= day <= daysInMonth:
            raise ValueError(f"El día debe estar entre 1 y {daysInMonth} para el mes {month}")
        return day

    def __validateHour(self, hour: int) -> int:
        """
        Valida la hora.

        Args:
            hour (int): Hora.

        Returns:
            int: Hora validada.

        Raises:
            TypeError: Si la hora no es entera.
            ValueError: Si la hora no está entre 0 y 23.
        """
        if not isinstance(hour, int):
            raise TypeError("La hora debe ser un entero")
        if not 0 <= hour <= 23:
            raise ValueError("La hora debe estar entre 0 y 23")
        return hour

    def __validateMinute(self, minute: int) -> int:
        """
        Valida los minutos.

        Args:
            minute (int): Minuto.

        Returns:
            int: Minuto validado.

        Raises:
            TypeError: Si el minuto no es entero.
            ValueError: Si el minuto no está entre 0 y 59.
        """
        if not isinstance(minute, int):
            raise TypeError("Los minutos deben ser un entero")
        if not 0 <= minute <= 59:
            raise ValueError("Los minutos deben estar entre 0 y 59")
        return minute

    def __validateSecond(self, second: int) -> int:
        """
        Valida los segundos.

        Args:
            second (int): Segundo.

        Returns:
            int: Segundo validado.

        Raises:
            TypeError: Si el segundo no es entero.
            ValueError: Si el segundo no está entre 0 y 59.
        """
        if not isinstance(second, int):
            raise TypeError("Los segundos deben ser un entero")
        if not 0 <= second <= 59:
            raise ValueError("Los segundos deben estar entre 0 y 59")
        return second

    def __validateMicrosecond(self, microsecond: int) -> int:
        """
        Valida los microsegundos.

        Args:
            microsecond (int): Microsegundo.

        Returns:
            int: Microsegundo validado.

        Raises:
            TypeError: Si el microsegundo no es entero.
            ValueError: Si el microsegundo no está entre 0 y 999999.
        """
        if not isinstance(microsecond, int):
            raise TypeError("Los microsegundos deben ser un entero")
        if not 0 <= microsecond <= 999999:
            raise ValueError("Los microsegundos deben estar entre 0 y 999999")
        return microsecond

    def __getDaysInMonth(self, month: int, year: int) -> int:
        """
        Devuelve la cantidad de días de un mes dado, considerando años bisiestos.

        Args:
            month (int): Mes.
            year (int): Año.

        Returns:
            int: Días en el mes.
        """
        if month in {4, 6, 9, 11}:
            return 30
        elif month == 2:
            return 29 if self.__isLeapYear(year) else 28
        else:
            return 31

    def __isLeapYear(self, year: int) -> bool:
        """
        Determina si un año es bisiesto.

        Args:
            year (int): Año.

        Returns:
            bool: True si es bisiesto, False en caso contrario.
        """
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        else:
            return year % 400 == 0

    @classmethod
    def now(cls):
        """
        Crea un objeto myDate con la fecha y hora actual del sistema.

        Returns:
            myDate: Instancia con la fecha y hora actual.
        """
        currentTime = time.time()
        localTime = time.localtime(currentTime)
        return cls(
            year=localTime.tm_year,
            month=localTime.tm_mon,
            day=localTime.tm_mday,
            hour=localTime.tm_hour,
            minute=localTime.tm_min,
            second=localTime.tm_sec,
            microsecond=int((currentTime - int(currentTime)) * 1e6)
        )

    def __str__(self):
        """
        Devuelve la representación en string de la fecha y hora.

        Returns:
            str: Fecha y hora en formato 'YYYY-MM-DD HH:MM:SS.microsegundos'.
        """
        return (f"{self.__year}-{self.__month:02d}-{self.__day:02d} "
                f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}."
                f"{self.__microsecond:06d}")

    def __repr__(self):
        """
        Devuelve la representación formal del objeto myDate.

        Returns:
            str: Representación formal del objeto.
        """
        return (f"MyDate(year={self.__year}, month={self.__month}, day={self.__day}, "
                f"hour={self.__hour}, minute={self.__minute}, second={self.__second}, "
                f"microsecond={self.__microsecond})")