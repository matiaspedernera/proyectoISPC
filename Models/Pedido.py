class Pedido:

    #---Constructor con parametros---
    def __init__(self, id, fecha, esta, tipo, obser, mesa):
        self.__id=id
        self.__fecha_hora=fecha
        self.__estado=esta
        self.__tipo=tipo
        self.__observacion=obser
        self.__mesa_num=mesa


    #--- Setters ---
    def setId(self, id):
        self.__id=id 

    def setFechaHora(self, fecha):
        self.fecha_hora=fecha

    def setEstado(self, esta):
        self.__estado=esta

    def setTipo(self, tipo):
        self.__tipo=tipo

    def setObserva(self, obser):
        self.__observacion=obser

    def setMesa(self, mesa):
        self.__mesa_num=mesa


    #--- Getters ---
    def getId(self):
        return (self.__id)

    def getFechaHora(self):
        return (self.__fecha_hora)

    def getEstado(self):
        return self.__estado
    
    def getTipo(self):
        return (self.__tipo)

    def getObserva(self):
        return(self.__observacion)

    def getMesa(self):
        return (self.__mesa)


    #--- Metodos ---
    def calcularImporte(self):
        pass
