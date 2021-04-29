class Empleado:
    def __init__(self,nombre,apellido,direccion,ci):
        self.nombre=nombre
        self.apellido=apellido
        self.direccion=direccion
        self.ci=ci

    def __str__(self):
        dato="Nombre:"+self.nombre+"\nApellido "+self.apellido+"\nDireccion "+self.direccion+"\nCi "+self.ci
        return dato      
