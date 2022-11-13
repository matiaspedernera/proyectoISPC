class Reserva:

    #---Constructor con parametros---
    def __init__(self, num, esta, ubi, cant):
        self.__numero=num
        self.__estado=esta
        self.__ubicacion=ubi
        self.__cant_pers=cant


    #--- Setters ---
    def setNumero(self, num):
        self.__numero=num

    def setEstado(self, esta):
        self.__estado=esta

    def setUbicacion(self, ubi):
        self.__ubicacion=ubi

    def setCantidad(self, cant):
        self.__cant_pers=cant


    #--- Getters ---
    def getNumero(self):
        return (self.__numero)

    def getEstado(self):
        return self.__estado

    def getUbicacion(self):
        return (self.__ubicacion)
    
    def getCantidad(self):
        return (self.__cant_pers)

