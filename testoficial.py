from Oficial import Oficial
import os
opcion=1
listaOficial=[]

def menu():
                                                                                                                        
    os.system("cls")
   
    print("\t.......................")
    print("\t Menu Oficial")
    print("\t.......................")
    print("\t① Registrar Oficial")
    print("\t② Eliminar Oficial") 
    print("\t③ Listar Oficial")
    print("\t④ Actualiza Oficial")
    print("\t⓪. Salir ")

def Registrar(listaOficial):
    #os.system("cls")

    nombre=input("Nombre: ")
    apellido=input("Apellido")
    direccion=input("Direccion:")
    ci=input("Ci:")
    fecha=input("Fecha: ")
    educacion=input("Titilo : ")
    experiencia=input("Nivel: ")
    salario=input("Salario: ")
    cargo=input("Cargo")

    oficial=Oficial(nombre,apellido,direccion,ci,fecha,educacion,experiencia,salario,cargo)
    listaOficial.append(oficial)
def MenuEliminarOficial():
    print("1.Eliminar por # Oficial")    
    print("2.Eliminar por Nombre de Oficial")    
    print("3.Eliminar por ci de Oficial")
    print("0 Csncelar")
def EliminacionCi(Ci,listaoficial):
    for i in range(len(listaoficial)):
        if Ci==listaoficial[i].getCi():
            del listaoficial[i]

def EliminacionNombre(Nombre,listaoficial):
    for i in range(len(listaoficial)):
        if Nombre==listaoficial[i].getNombre():
            del listaoficial[i]        
def EliminacionPrincipal(listaoficial):
    ListarOficial(listaoficial)
    MenuEliminarOficial()
    opp=int(input(">> "))
    if opp==1:
        Numero=int(input("Ingrese el numero del Cliente"))
        del listaoficial[Numero-1]
    elif opp==2:
        Nombre=input("Ingrese el nombre del Empleado")
        EliminacionNombre(Nombre,listaoficial)
    elif opp==3:
        Ci=input("Ingrese el Numero de Carnet del Empleado")
        EliminacionCi(Ci,listaoficial)    
    else:
        print("Opcion no valida")
def ListarOficial(listaOficial):
    for i in range(len(listaOficial)):
        print("============================")
        print("Oficial # ",(i+1))
        
        print("Nombre= ",listaOficial[i].getNombre())
        print("Apellido= ",listaOficial[i].getApellido())
        print("Direccion=",listaOficial[i].getDireccion())
        print("Ci= ",listaOficial[i].getCi())
        print("Nivel De Educacion= ",listaOficial[i].geteducacion())
        print("Experiencia=",listaOficial[i].getexperiencia())
        print("Salario=",listaOficial[i].getsalario())
        print("Fecha de Registro=",listaOficial[i].getFecha())
        print("============================")
           
    input()
def ModificarOficial(listaoficial):
    ListarOficial(listaoficial)
    
    os.system("cls")
    name=input("Ingrese el nombre Empleado")
    apellid=input("Ingrese el apellido del empleado")
    for i in listaoficial:
        if i.getNombre()==name and i.getApellido()==apellid:
            nombre=input("Nombre: ")
            apellido=input("Apellido")
            direccion=input("Direccion:")
            ci=input("Ci:")
            fecha=input("Fecha: ")
            educacion=input("Titilo : ")
            experiencia=input("Nivel: ")
            salario=input("Salario: ")
            cargo=input("Cargo")
            if nombre!=None:
                i.setNombre(nombre)
            if apellido!=None:
                i.setApellido(apellido)
            if direccion!=None:
                i.setDireccion(direccion)
            if ci!=None:
                i.setCi(ci)
            if educacion!=None:
                i.seteducacion(educacion)
            if experiencia!=None:
                i.setexperiencia(experiencia)
            if salario!=None:
                i.setsalario(salario)
            if cargo!=None:
                i.setcargo(cargo)                
            if fecha!=None:
                i.setFecha(fecha)        

        else:
            print("Empleado no Encontrado")           





    

while opcion!=0:
    menu()
    opcion=int(input("\t >> "))
    if opcion==1:
        os.system("cls")
        Registrar(listaOficial)
    if opcion==2:
        os.system("cls")
        EliminacionPrincipal(listaOficial)    
    elif opcion==3:
        os.system("cls")
        ListarOficial(listaOficial)
    elif opcion==4:
        ModificarOficial(listaOficial)   
    elif opcion==0:
        os.system("cls")
        print("Espere el sistema esta guardando datos")
    else:
        print("No existe es opcion!!!")
        
        