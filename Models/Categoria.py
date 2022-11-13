class Reserva:

    #---Constructor con parametros---
    def __init__(self, cod, nom, desc):
        self.__codigo=cod
        self.__nombre=nom
        self.__descripcion=desc


    #--- Setters ---
    def setCodigo(self, cod):
        self.__codigo=cod

    def setNombre(self, nom):
        self.__nombre=nom

    def setDescripcion(self, desc):
        self.__descripcion=desc


    #--- Getters ---
    def getCodigo(self):
        return (self.__codigo)

    def getNombre(self):
        return (self.__nombre)

    def getDescripcion(self):
        return self.__descripcion
    
