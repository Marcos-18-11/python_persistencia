""" A partir del fichero houses.csv

Se solicita un presupuesto y te muestra los datos
de los pisos que puedes comprar ordenados de mayor a menor """
import pandas as pd
presupuesto=float(input("Introduzca su presupuestyo disponible: "))
df=pd.read_csv("houses.csv",encoding="UTF-8")
print(df.query("price<=@presupuesto").sort_values(by="price",ascending=False))