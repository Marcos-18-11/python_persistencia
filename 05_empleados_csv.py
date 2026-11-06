import csv
"""
with open("empleados.csv","r") as f:
    datos=csv.reader(f,delimiter=",")
    for row in datos:
        print(row)
with open("empleados.csv","r") as f:
    datos=csv.DictReader(f)
    for row in datos:
        print(row)
with open("empleados.csv","r") as f:
    datos=list(csv.reader(f))
    print(datos)
with open("empleados.csv","r") as f:
    datos=list(csv.DictReader(f))
    print(datos)
    """
    #solicita la introducción de un departamento y te muestra los nombres de las personas de ese departamento
    
dep=input("introduzca un departamento para visualizar los nombres de los empleados de este: ")

with open("empleados.csv","r") as f:
    datos=csv.DictReader(f)
    for emp in datos:
        if emp["departamento"]==dep:
            print(emp["empleado"])

#Nombre del empleado con el mayor salario

with open("empleados.csv","r") as f:
    lista_empleados=list(csv.DictReader(f))
    nombre=max(lista_empleados,key=lambda a:a["salario"])
    print(nombre["empleado"])