"""
Sobre el archivo de ventas, realizar:

-A partir de nombre de tienda, mostrar sus ventas totales

-Mostrar el mayor gasto de personal de tiendas

-A partir del nombre de tienda, mes en la que esta obtuvo mayor facturación 
"""
import pandas as pd
tienda=input("Introduzca el nombre de la tienda: ")
df=pd.read_csv("ventas_tiendas.csv",encoding="UTF-8")
df_1=df[df["nombre_tienda"]==tienda]
print(f"la facturación total de {tienda} es: {df_1["facturacion"].sum()}")

ventas_totales=df.groupby("nombre_tienda").agg(total_ventas=("facturacion","sum"))
print(ventas_totales)

mayor_gasto=df.groupby("nombre_tienda").agg(gasto=("gastos_personal","sum"))
print(mayor_gasto)
print(f"Mayor gasto: {mayor_gasto.max()}")

print(df.query("nombre_tienda==@tienda").sort_values(by="facturacion",ascending=False).iloc[0]["nombre_tienda"])
print(df.query("nombre_tienda==@tienda").sort_values(by="facturacion",ascending=False).iloc[0]["mes"])

print("Tienda con el record de facturación")
print(df.sort_values(by="facturacion",ascending=False).iloc[0]["nombre_tienda"])