import os

class ArchiveUtil():
    """
    Clase utilitaria para la gestión de archivos y directorios.

    Atributos:
        __router (str): Ruta del directorio de trabajo.

    Métodos:
        getRouter(): Devuelve la ruta actual.
        getArchive(nameArchive): Devuelve un objeto archivo abierto en modo lectura.
        getDirectoriesList(): Devuelve la lista de archivos y carpetas en el directorio actual.
        getSerial(nameArchive): Obtiene el serial de un archivo .bin.
        setRouter(router): Cambia la ruta del directorio de trabajo.
        setOrCreateFiles(nameArchive, content, bool): Crea o escribe en un archivo.
        utilDirectory(router): Valida y establece la ruta del directorio.
    """

    __router = ""

    def __init__(self, router = os.getcwd()):#constructor polimorfico
        """
        Inicializa la clase ArchiveUtil.

        Args:
            router (str): Ruta del directorio de trabajo. Por defecto, el directorio actual.

        Raises:
            Exception: Si la ruta es vacía.
        """

        if (not router or len(router) == 0):
            raise Exception("Manage-Error: La ruta es vacia.")
        self.utilDirectory(router)

    #getters    
    def getRouter(self):
        """
        Devuelve la ruta actual del directorio de trabajo.

        Returns:
            str: Ruta del directorio.
        """
        return str(self.__router)
    
    def getArchive(self, nameArchive):
        """
        Devuelve un objeto archivo abierto en modo lectura.

        Args:
            nameArchive (str): Nombre del archivo (con extensión).

        Returns:
            file|None: Objeto archivo abierto o None si no se encuentra.

        Raises:
            Exception: Si el nombre está vacío.
        """
        if (not nameArchive or len(nameArchive) == 0):
            raise Exception("Manage-Error: El nombre esta Vacio.")
        
        try: #usamos try en este constexto ya que OPEN es un objeto externo a nuestra clase
            archive = open(self.__router+"\\"+nameArchive)#requiere que el nombre venga con su extencion. 
            return archive
        except FileNotFoundError as e:
            print("Manage-Error: El archivo no ha sido encontrado", e)
            return None

    def getDirectoriesList(self):
        """
        Devuelve la lista de archivos y carpetas en el directorio actual.

        Returns:
            list|None: Lista de archivos y carpetas, o None si ocurre un error.
        """
        try:#usamos try en este constexto ya que OPEN es un objeto externo a nuestra clase
            directories = os.listdir(self.__router)  # Obtiene la lista de archivos y directorios

            if (len(directories) > 0):
                return directories
            else:
                raise FileNotFoundError("No se encontraron archivos.")

        except FileNotFoundError as e:
            print("Manage-Error: Directorio no existe: ", e)
            return None

        except NotADirectoryError as e:
            print("Manage-Error: Ocurrió un error inesperado:", e)
            return None

    def getSerial(self, nameArchive):
        """
        Obtiene el serial de un archivo .bin.

        Args:
            nameArchive (str): Nombre del archivo.

        Returns:
            str|None: Serial extraído del nombre o None si ocurre un error.

        Raises:
            Exception: Si el nombre está vacío o no es .bin.
        """
        if (not nameArchive or len(nameArchive) == 0):
            raise Exception("Manage-Error: El nombre esta Vacio.")
        
        try:
            if (not nameArchive.endswith(".bin")):
                raise Exception("Manage-Error: El archivo no es de tipo .bin")
            return nameArchive.split("_")[-1].split(".")[0]
        
        except Exception as e:
            print("Manage-Error: Error al obtener el serial", e)
        
    #setters
    def setRouter(self, router):
        """
        Cambia la ruta del directorio de trabajo.

        Args:
            router (str): Nueva ruta del directorio.

        Raises:
            Exception: Si la ruta es vacía.
        """
        if (not router or len(router) == 0):
            raise Exception("Manage-Error: La ruta es vacia.")
        self.utilDirectory(router)

    def setOrCreateFiles(self, nameArchive, content = "", bool = False):#metodo polimorfico
        """
        Crea o escribe en un archivo.

        Args:
            nameArchive (str): Nombre del archivo (con extensión).
            content (str): Contenido a escribir. Si está vacío, crea el archivo.
            bool (bool): Si es True, agrega salto de línea tras el contenido.

        Raises:
            Exception: Si el nombre está vacío.
        """
        if (not nameArchive or len(nameArchive) == 0):
            raise Exception("Manage-Error: El nombre esta Vacio.")
        
        
        try: #usamos try en este constexto ya que OPEN es un objeto externo a nuestra clase
            if (not content or len(content) == 0):
                archive = open(self.__router+"\\"+nameArchive+".txt", "x")
                return
            
            archive = open(self.__router+"\\"+nameArchive, "a")#requiere que el nombre venga con su extencion. 
            
            if (bool == True):
                archive.write(content+"\n")
            else:
                archive.write(content)

        except FileNotFoundError as e:
            print("Manage-Error: El archivo no ha sido encontrado", e)

    #utilitarias
    def utilDirectory(self, router):
        """
        Valida y establece la ruta del directorio de trabajo.

        Args:
            router (str): Ruta a validar.

        Raises:
            NotADirectoryError: Si la ruta existe pero no es un directorio.
            FileNotFoundError: Si el directorio no existe.
        """       
        if (os.path.exists(router) and not os.path.isdir(router)):
            raise NotADirectoryError(f"Manage-Error: La ruta '{router}' no es un directorio.")
        elif (not os.path.exists(router)):
            raise FileNotFoundError(f"Manage-Error: El directorio '{router}' no existe.")
        
        self.__router = router