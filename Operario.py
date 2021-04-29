from Empleado import Empleado
class Operario:
    def __init__(self,nombre,salario):
        self.__salario=salario   
        super().__init__(nombre)
    def __str__(self):
        sueldo="Salario :"+self.__salario
    def getsalario(self):
        return self.__salario
                


