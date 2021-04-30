
from Operario import Operario
class Oficial(Operario):
    def __init__(self,nombre,apellido,direccion,ci,fecha,nveleducacion,aniosdeexperiencia,salario,cargo):
        self.__cargo=cargo
        super().__init__(nombre,apellido,direccion,ci,fecha,nveleducacion,aniosdeexperiencia,salario)
    def __str__(self):
        return "Nombre :"+self.__nombre+"\nApellido"+self.__apellido+"\nDireccion"+self.__direccion+"\nCi"+self.__ci+"\nFecha"+self.__fecha+"\nNivel de Educacion"+self.__nveleducacion+"\nAnios de Experiencia"+self.__aniosdeexperiecia+"\nSalario"+self.__salario+"Cargo"+self.__cargo
    def getcargo(self):
        return self.__cargo
    def setcargo(self,cargo):
        self.__cargo=cargo     
#juan=Oficial("1","2","3","4","5","6","7","8","9")
#print(juan.getNombre())
#print(juan.getApellido())
#print(juan.getDireccion())
#print(juan.geteducacion())
#print(juan.getsalario()) 
#print(juan.geteducacion())
        


    