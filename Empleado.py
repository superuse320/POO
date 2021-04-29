
class Empleado:
    def __init__(self,nombre,apellido,direccion,ci,fecha):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__direccion=direccion
        self.__ci=ci
        self.__fecha=fecha
    def __str__(self):
        
        return "Nombre:"+self.__nombre+"\nApellido "+self.__apellido+"\nDireccion "+self.direccion__+"\nCi "+self.__ci +"\nFecha"+self.__fecha
        
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getDireccion(self):
        return self.__direccion
    def getCi(self):
        return self.__ci
    def getFecha(self):
        return self.__fecha

    def setNombre(self,nombre):
        self.__nombre=nombre
    def setApellido(self,apellido):
        self.__apellido=apellido
    def setDireccion(self,direccion):
        self.__direccion=direccion
    def setCi(self,ci):
        self.__ci=ci
    def setFecha(self,fecha):
        self.__fecha=fecha   