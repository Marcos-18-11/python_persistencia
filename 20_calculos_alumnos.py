""" A partir del documento alumnos.json realizar:

-calcular la nota media global
-mostrar nota más alta de cada curso
-total de alumnos de cada curso """
import pandas as pd
df=pd.read_json("alumnos.json",encoding="UTF-8")
print(f"Nota media de los alumnos: {df["nota"].mean():.2f}")

grupo=df.groupby("curso").agg(nota_alta=("nota","max"),total_alumnos=("nombre","count"))
print(grupo)