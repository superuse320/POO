from Empleado import Empleado
class Operario(Empleado):
    def __init__(self,nombre,apellido,direccion,ci,fecha,nveleducacion,aniosdeexperiencia,salario):
        self.__nveleducacion=nveleducacion
        self.__aniosdeexperiencia=aniosdeexperiencia
        self.__salario=salario


        super().__init__(nombre,apellido,direccion,ci,fecha)
    def __str__(self):
        return "Nombre :"+self.__nombre+"\nApellido"+self.__apellido+"\nDireccion"+self.__direccion+"\nCi"+self.__ci+"\nFecha"+self.__fecha+"\nNivel de Educacion"+self.__nveleducacion+"\nAnios de Experiencia"+self.__aniosdeexperiecia+"\nSalario"+self.__salario
    def geteducacion(self):
        return self.__nveleducacion
    def getexperiencia(self):
        return self.__aniosdeexperiencia
    def getsalario(self): 
        return self.__salario
    def seteducacion(self,nveleducacion):
        self.__nveleducacion=nveleducacion
    def setexperiencia(self,aniosdeexperiencia):
        self.__aniosdeexperiencia=aniosdeexperiencia
    def setsalario(self,salario): 
        self.__salario=salario     

                
