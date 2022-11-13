class Reserva:

    #---Constructor con parametros---
    def __init__(self, num, fecha, esta, deta):
        self.__numero=num
        self.__fecha_hora=fecha
        self.__estado=esta
        self.__detalle=deta


    #--- Setters ---
    def setNumero(self, num):
        self.__numero=num

    def setFecha(self, fecha):
        self.__fecha_hora=fecha

    def setEstado(self, esta):
        self.__estado=esta

    def setDetalle(self, deta):
        self.__detalle=deta


    #--- Getters ---
    def getNumero(self):
        return (self.__numero)

    def getFecha(self):
        return (self.__fecha_hora)

    def getEstado(self):
        return self.__estado
    
    def getDetalle(self):
        return (self.__detalle)

