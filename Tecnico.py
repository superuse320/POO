
from Operario import Operario
class Tecnico(Operario):
    def __init__(self,nombre,apellido,direccion,ci,fecha,nveleducacion,aniosdeexperiencia,salario,TituloTecnico):
        self.__TituloTecnico=TituloTecnico
        super().__init__(nombre,apellido,direccion,ci,fecha,nveleducacion,aniosdeexperiencia,salario)
    def __str__(self):
        return "Nombre :"+self.__nombre+"\nApellido"+self.__apellido+"\nDireccion"+self.__direccion+"\nCi"+self.__ci+"\nFecha"+self.__fecha+"\nNivel de Educacion"+self.__nveleducacion+"\nAnios de Experiencia"+self.__aniosdeexperiecia+"\nSalario"+self.__salario+"Cargo"+self.__cargo+"Titulo Tecnologico"+self.__TituloTecnico
    def getTecnico(self):
        return self.__TituloTecnico
    def setTecnico(self,TituloTecnico):
        self.__TituloTecnico=TituloTecnico    