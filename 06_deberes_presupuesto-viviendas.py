#Sobre houses.csv, pides presupuesto y el programa te ha de mostrar las opciones disponibles

"""
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
    """
import streamlit as st   
import csv
presupuesto = st.number_input("Dime tu presupuesto: ")
with open("houses.csv", "r") as f:
    disponibles=list(filter(lambda p:float(p["price"])<=presupuesto,csv.DictReader(f)))
    st.table(disponibles)

