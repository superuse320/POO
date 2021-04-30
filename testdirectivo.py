from Empleado import Empleado
from Directivo import Directivo
import os
def menu():
                                                                                                                        
    os.system("cls")
   
    print("\t.......................")
    print("\t Menu Directivo")
    print("\t.......................")
    print("\t① Registrar Directivo")
    print("\t② Eliminar Directivo") 
    print("\t③ Listar Directivo")
    print("\t④ Actualiza Directivo")
    print("\t⓪. Salir ")

def Registrar(listaEmpleados):
    #os.system("cls")

    nombre=input("Nombre: ")
    apellido=input("Apellido")
    direccion=input("Direccion:")
    ci=input("Ci:")
    fecha=input("Fecha: ")
    ctitulo=input("Titilo : ")
    nivel=input("Nivel: ")
    salario=input("Salario: ")

    directivo=Directivo(nombre,apellido,direccion,ci,fecha,ctitulo,nivel,salario)
    listaDirectivo.append(directivo)
def MenuEliminarDirectivo():
    print("1.Eliminar por # Directivo")    
    print("2.Eliminar por Nombre de Directivo")    
    print("3.Eliminar por ci de Directivo")
    print("0 Csncelar")
def EliminacionCi(Ci,listadirectivo):
    for i in range(len(listadirectivo)):
        if Ci==listadirectivo[i].getCi():
            del listadirectivo[i]

def EliminacionNombre(Nombre,listadirectivo):
    for i in range(len(listadirectivo)):
        if Nombre==listadirectivo[i].getNombre():
            del listadirectivo[i]        
def EliminacionPrincipal(listadirectivo):
    ListarDirectivos(listadirectivo)
    MenuEliminarDirectivo()
    opp=int(input(">> "))
    if opp==1:
        Numero=int(input("Ingrese el numero del Cliente"))
        del listaDirectivo[Numero-1]
    elif opp==2:
        Nombre=input("Ingrese el nombre del Empleado")
        EliminacionNombre(Nombre,listadirectivo)
    elif opp==3:
        Ci=input("Ingrese el Numero de Carnet del Empleado")
        EliminacionCi(Ci,listadirectivo)    
    else:
        print("Opcion no valida")


    
    

def ListarDirectivos(listaDirectivo):
    for i in range(len(listaDirectivo)):
        print("============================")
        print("Directivo # ",(i+1))
        
        print("Nombre= ",listaDirectivo[i].getNombre())
        print("Apellido= ",listaDirectivo[i].getApellido())
        print("Direccion=",listaDirectivo[i].getDireccion())
        print("Ci= ",listaDirectivo[i].getCi())
        print("Titulo= ",listaDirectivo[i].getTitulo())
        print("Nivel= ",listaDirectivo[i].getnivel())
        print("Salario= ",listaDirectivo[i].getsalario())
        print("Fecha de Registro=",listaDirectivo[i].getFecha())
        print
        print("============================")
           
    input()
def ModificarEmpleado(listadirectivo):
    ListarDirectivos(listadirectivo)
    
    os.system("cls")
    name=input("Ingrese el nombre Empleado")
    apellid=input("Ingrese el apellido del empleado")
    for i in listadirectivo:
        if i.getNombre()==name and i.getApellido()==apellid:
            nombre=input("Nombre: ")
            apellido=input("Apellido: ")
            direccion=input("Direccion: ")
            ci=input("Ci:" )
            fecha=input("Fecha: ")
            ctitulo=input("Titilo : ")
            nivel=input("Nivel: ")
            salario=input("Salario: ")
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
            if ctitulo!=None:
                i.setTitulo(ctitulo)
            if nivel!=None:
                i.setnivel(nivel)
            if salario!=None:
                i.setsalario(salario)        

        else:
            print("Empleado no Encontrado")           





    

opcion=1
listaDirectivo=[]

while opcion!=0:
    menu()
    opcion=int(input("\t >> "))
    if opcion==1:
        os.system("cls")
        Registrar(listaDirectivo)
    if opcion==2:
        os.system("cls")
        EliminacionPrincipal(listaDirectivo)    
    elif opcion==3:
        os.system("cls")
        ListarDirectivos(listaDirectivo)
    elif opcion==4:
        ModificarEmpleado(listaDirectivo)   
    elif opcion==0:
        os.system("cls")
        print("Espere el sistema esta guardando datos")
    else:
        print("No existe es opcion!!!")
        
        