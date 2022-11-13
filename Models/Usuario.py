class Usuario:

    #---Constructor con parametros---
    def __init__(self, id, nom, ape, mail, contra, tipo):
        self.__id=id
        self.__nombre=nom
        self.__apellido=ape
        self.__email=mail
        self.__password=contra
        self.__tipo=tipo
        

    #--- Setters ---
    def setId(self, id):
        self.__id=id 

    def setNombre(self, nom):
        self.__nombre=nom

    def setApellido(self, ape):
        self.__apellido=ape

    def setEmail(self, mail):
        self.__email=mail

    def setPassword(self, contra):
        self.__password=contra

    def setTipo(self, tipo):
        self.__tipo=tipo


    #--- Getters ---
    def getId(self):
        return (self.__id)

    def getNombre(self):
        return (self.__nombre)

    def getApellido(self):
        return self.__apellido
    
    def getEmail(self):
        return (self.__email)

    def getPassword(self):
        return(self.__password)

    def getTipo(self):
        return (self.__tipo)


    #--- Metodos ---
    def login(self):
        pass

    def registrar(self):
        pass