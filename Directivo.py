from Empleado import Empleado
class Directivo(Empleado):
    def __init__(self,nombre,apellido,direccion,ci,fecha,cTitulo,nivel,salario):
        self.__cTitulo=cTitulo
        self.__nivel=nivel
        self.__salario=salario
        
    
      
        super().__init__(nombre,apellido,direccion,ci,fecha)
    def __str__(self):
        return "Tituldo"+self.__cTitulo+"\nNivel"+self.__nivel+"\nSalario"+self.__salario      
    def setTitulo(self,cTitulo):
        self.__cTitulo=cTitulo
    def setnivel(self,nivel):
        self.__nivel=nivel
    def setsalario(self,salario):
        self.__salario=salario   
    def getTitulo(self):
        return self.__cTitulo
    def getnivel(self):
        return self.__nivel
    def getsalario(self):
        return self.__salario    
