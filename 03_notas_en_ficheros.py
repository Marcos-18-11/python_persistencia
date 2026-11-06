#Al iniciar el programa se debe mostrar el siguiente menú, 
# 1 añadir nota, 
# 2 Mostrar notas externas, 
# 3 Total de aprobados, 
# 4 Nota media, 
# 5 Mostrar todas
# 6 Salir

#El usuario elige una opción del 1 al 6 
#y el programa le mestra o le ide los datos necesarios, 
# para llevarla acabo, 
# después vuelve a salir el menú hasta que elija la opción de salir
#Las notas se guardan en un fichero
notas_fichero="notas.txt"
activo=True
def imprimir_menu():
        print("                            ")
        print("|--------------------------|")
        print("1.| Añadir nota            |")
        print("|--------------------------|")
        print("2.| Mostrar notas extremas |")
        print("|--------------------------|")
        print("3.| Total de aprobados     |")
        print("|--------------------------|")
        print("4.| Nota media             |")
        print("|--------------------------|")
        print("5.| Mostrar todas          |")
        print("|--------------------------|")
        print("6.| Salir                  |")
        print("|--------------------------|")
        print("                            ")
        print("                            ")
     
def añadir_notas():
    try:
                    nota=int(input("Introduzca una nota(0-10): "))
                    f=open(notas_fichero,"a")
                    f.write(str(nota)+"\n")
                    print("                            ")
                    print("|--------------------------|")
                    print(f"Nota introducida: | {nota} |")
                    print("|--------------------------|")
                    print("                            ")
    except ValueError:
                    print("                            ")
                    print("|------------------------------|")
                    print("| Introduzca valores numéricos |")
                    print("|------------------------------|")
                    print("                            ")
def leer_notas():
    maximo=-1
    minimo=11
    try:
        with open(notas_fichero,"r") as f:
            linea=f.readline()
            
            while linea!="":
                nota_actual=int(linea.strip())
                if nota_actual>=maximo:
                    maximo=nota_actual
                if nota_actual<=minimo:
                    minimo=nota_actual
                linea=f.readline()
        print("                            ")
        print("|---------------------------|")
        print(f"Nota más alta | {maximo}| ")
        print("|--------------------------|")
        print(f"Nota más baja | {minimo}| ")
        print("|---------------------------|")
        print("                            ")
    except FileNotFoundError:
        print("No hay registros")
def total_aprobados():
    contador=0
    try:
        with open(notas_fichero,"r") as f:
            linea=f.readline()
                        
            while linea!="":
                nota_actual=int(linea.strip())
                if nota_actual>=5:
                    contador+=1
                linea=f.readline()    
        print("                            ")
        print("|--------------------------------|")
        print(f"Total de aprobados: | {contador} |")
        print("|--------------------------------|")
        print("                            ")
    except FileNotFoundError:
            print("No hay registros")
    
def nota_media():
    try:
        with open(notas_fichero,"r") as f:
            notas=f.readlines()
        if not notas:
            return 0
        return sum([float(n.strip()) for n in notas])/len(notas)
    except FileNotFoundError:
        print("No hay registros")
        
def mostrar_todas():
    try:
        with open(notas_fichero,"r") as f:
            linea=f.readlines()
            print(linea)
        
    except FileNotFoundError:
        print("No hay registros")
    
    
while activo:
    
    imprimir_menu()
    
    print("____________________________")
    print("                            ")
    opcion=int(input("| Introduzca una de las opciones del menú |"))
    print("____________________________")
    print("                            ")
    print("                            ")
    print("                            ")
    match opcion:
        case 1:
            añadir_notas()
        case 2:
            leer_notas()
        case 3:
            total_aprobados()
            
        case 4:
            
            print(f"Nota media: | {nota_media()} |")
            
        case 5:
            mostrar_todas()
        case 6:
            print("                            ")
            print("                             ")
            print("---------------Fin del programa-----------------------")
            print("                             ")
            print("                            ")
            activo=False
        case _:
            print("                            ")
            print("|                                |")
            print("| -Introduzca una opción válida- |")
            print("|                                |")
            print("                            ")
            
print("                            ")
print("...Cerrando aplicación...")