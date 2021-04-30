from Empleado import Empleado
import os
def menu():
                                                                                                                        
    os.system("cls")
   
    print("\t.......................")
    print("\t Menu Empleado")
    print("\t.......................")
    print("\t① Registrar Empleado")
    print("\t② Eliminar Empleado") 
    print("\t③ Listar Empleado")
    print("\t④ Actualiza Empleado")
    print("\t⓪. Salir ")

def Registrar(listaEmpleados):
    #os.system("cls")

    nombre=input("Nombre: ")
    apellido=input("Apellido")
    direccion=input("Direccion:")
    ci=input("Ci:")
    fecha=input("Fecha: ")
    empleado=Empleado(nombre,apellido,direccion,ci,fecha)
    listaEmpleados.append(empleado)
def MenuEliminarEmpleado():
    print("1.Eliminar por # Empleado")    
    print("2.Eliminar por Nombre de Empleado")    
    print("3.Eliminar por ci de Empleado")
    print("0 Csncelar")
def EliminacionCi(Ci,listaempleados):
    for i in range(len(listaempleados)):
        if Ci==listaempleados[i].getCi():
            del listaempleados[i]

def EliminacionNombre(Nombre,listaempleados):
    for i in range(len(listaempleados)):
        if Nombre==listaempleados[i].getNombre():
            del listaempleados[i]        
def EliminacionPrincipal(listaempleados):
    ListarEmpleados(listaempleados)
    MenuEliminarEmpleado()
    opp=int(input(">> "))
    if opp==1:
        Numero=int(input("Ingrese el numero del Cliente"))
        del listaEmpleados[Numero-1]
    elif opp==2:
        Nombre=input("Ingrese el nombre del Empleado")
        EliminacionNombre(Nombre,listaempleados)
    elif opp==3:
        Ci=input("Ingrese el Numero de Carnet del Empleado")
        EliminacionCi(Ci,listaempleados)    
    else:
        print("Opcion no valida")


    
    

def ListarEmpleados(listaEmpleados):
    for i in range(len(listaEmpleados)):
        print("============================")
        print("Cliente # ",(i+1))
        
        print("Nombre= ",listaEmpleados[i].getNombre())
        print("Apellido= ",listaEmpleados[i].getApellido())
        print("Direccion=",listaEmpleados[i].getDireccion())
        print("Ci= ",listaEmpleados[i].getCi())
        print("Fecha de Registro=",listaEmpleados[i].getFecha())
        print("============================")
           
    input()
def ModificarEmpleado(listaempleado):
    ListarEmpleados(listaempleado)
    
    os.system("cls")
    name=input("Ingrese el nombre Empleado")
    apellid=input("Ingrese el apellido del empleado")
    for i in listaempleado:
        if i.getNombre()==name and i.getApellido()==apellid:
            nombre=input()
            apellido=input()
            direccion=input()
            ci=input()
            fecha=input()
        if nombre!=None:
            i.setNombre(nombre)
            if apellido!=None:
                i.setApellido(apellido)
            if direccion!=None:
                i.setDireccion(direccion)
            if ci!=None:
                i.setCi(ci)
            if fecha!=None:
                i.setFecha(fecha) 
        else:
            print("Empleado no Encontrado")           





    

opcion=1
listaEmpleados=[]

while opcion!=0:
    menu()
    opcion=int(input("\t >> "))
    if opcion==1:
        os.system("cls")
        Registrar(listaEmpleados)
    if opcion==2:
        os.system("cls")
        EliminacionPrincipal(listaEmpleados)    
    elif opcion==3:
        os.system("cls")
        ListarEmpleados(listaEmpleados)
    elif opcion==4:
        ModificarEmpleado(listaEmpleados)    
    elif opcion==0:
        os.system("cls")
        print("Espere el sistema esta guardando datos")
    else:
        print("No existe es opcion!!!")
        
        
