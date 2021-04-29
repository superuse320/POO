
class Empleado:
    def __init__(self,nombre):
        self.__nombre=nombre
    def __str__(self):
        dato="Nombre:"+self.__nombre
        return dato
    def getnombre(self):
        return self.__nombre          