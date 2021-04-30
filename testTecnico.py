from Tecnico import Tecnico
import os
opcion=1
listaTecnico=[]

def menu():
                                                                                                                        
    os.system("cls")
   
    print("\t.......................")
    print("\t Menu Tecnico")
    print("\t.......................")
    print("\t① Registrar Tecnico")
    print("\t② Eliminar Tecnico") 
    print("\t③ Listar Tecnico")
    print("\t④ Actualiza Oficial")
    print("\t⓪. Salir ")

def Registrar(listaTecnico):
    #os.system("cls")

    nombre=input("Nombre: ")
    apellido=input("Apellido")
    direccion=input("Direccion:")
    ci=input("Ci:")
    fecha=input("Fecha: ")
    educacion=input("Titilo : ")
    experiencia=input("Nivel: ")
    salario=input("Salario: ")
    TituloTecnico=input("Titulo Tecnico: ")

    tecnico=Tecnico(nombre,apellido,direccion,ci,fecha,educacion,experiencia,salario,TituloTecnico)
    listaTecnico.append(tecnico)
def MenuEliminarTecnico():
    print("1.Eliminar por # Tecnico")    
    print("2.Eliminar por Nombre de Tecnico")    
    print("3.Eliminar por ci de Tecnico")
    print("0 Csncelar")
def EliminacionCi(Ci,listatecnico):
    for i in range(len(listatecnico)):
        if Ci==listatecnico[i].getCi():
            del listatecnico[i]

def EliminacionNombre(Nombre,listatecnico):
    for i in range(len(listatecnico)):
        if Nombre==listatecnico[i].getNombre():
            del listatecnico[i]        
def EliminacionPrincipal(listatecnico):
    ListarTecnico(listatecnico)
    MenuEliminarTecnico()
    opp=int(input(">> "))
    if opp==1:
        Numero=int(input("Ingrese el numero del Cliente"))
        del listatecnico[Numero-1]
    elif opp==2:
        Nombre=input("Ingrese el nombre del Empleado")
        EliminacionNombre(Nombre,listatecnico)
    elif opp==3:
        Ci=input("Ingrese el Numero de Carnet del Empleado")
        EliminacionCi(Ci,listatecnico)    
    else:
        print("Opcion no valida")
def ListarTecnico(listaTecnico):
    for i in range(len(listaTecnico)):
        print("============================")
        print("Oficial # ",(i+1))
        
        print("Nombre= ",listaTecnico[i].getNombre())
        print("Apellido= ",listaTecnico[i].getApellido())
        print("Direccion=",listaTecnico[i].getDireccion())
        print("Ci= ",listaTecnico[i].getCi())
        print("Nivel De Educacion= ",listaTecnico[i].geteducacion())
        print("Experiencia=",listaTecnico[i].getexperiencia())
        print("Salario=",listaTecnico[i].getsalario())
        print("Titulo Tecnologico",listaTecnico[i].getTecnico())
        print("Fecha de Registro=",listaTecnico[i].getFecha())
        print("============================")
           
    input()
def ModificarTecnico(listatecnico):
    ListarTecnico(listatecnico)
    
    os.system("cls")
    name=input("Ingrese el nombre Empleado")
    apellid=input("Ingrese el apellido del empleado")
    for i in listatecnico:
        if i.getNombre()==name and i.getApellido()==apellid:
            nombre=input("Nombre: ")
            apellido=input("Apellido")
            direccion=input("Direccion:")
            ci=input("Ci:")
            fecha=input("Fecha: ")
            educacion=input("Titilo : ")
            experiencia=input("Nivel: ")
            salario=input("Salario: ")
            tiTecnico=input("Titulo Tecnico")
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
            if tiTecnico!=None:
                i.setTecnico(tiTecnico)                
            if fecha!=None:
                i.setFecha(fecha)        

        else:
            print("Empleado no Encontrado")           





    

while opcion!=0:
    menu()
    opcion=int(input("\t >> "))
    if opcion==1:
        os.system("cls")
        Registrar(listaTecnico)
    if opcion==2:
        os.system("cls")
        EliminacionPrincipal(listaTecnico)    
    elif opcion==3:
        os.system("cls")
        ListarTecnico(listaTecnico)
    elif opcion==4:
        ModificarTecnico(listaTecnico)   
    elif opcion==0:
        os.system("cls")
        print("Espere el sistema esta guardando datos")
    else:
        print("No existe es opcion!!!")
        
        