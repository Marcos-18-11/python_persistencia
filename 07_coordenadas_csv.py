#se pide al usuario su posicion, 
#despues el programa le mostrará las coordenadas del punto mas cercano a su posición

#Segunda version, se pide al usuario las coordenadas de su posicion y se muestra su posicion mas cercan a una d elas tiendas del csv
import csv
import math

""" with open("coordenadas.csv","r") as f:
    
    coordenadas_tiendas=list(csv.DictReader(f)) 
     
print("Introduzca las coordenadas de su posición")
x_usuario=float(input("Coordenada 'X'"))
y_usuario=float(input("Coordenada 'Y'"))

coordenadas_usuario=(x_usuario,y_usuario)

def distancia(punto1,punto2):
    distance=math.hypot(punto1[0]-punto2[0],punto1[1]-punto2[1])
    return distance

distancias=[]

for row in coordenadas_tiendas:
    x_tienda=float(row["x"])
    y_tienda=float(row["y"])
    coordenadas_cada_tienda=(x_tienda,y_tienda)
    distancias.append(distancia(coordenadas_cada_tienda,coordenadas_usuario))
       
cercano=min(distancias)

indice=distancias.index(cercano)+1

print(f"La tienda mas cercana es la número: {indice}")
print(f"La distancia es: {cercano}") """
import csv
import math
print("Introduzca las coordenadas de su posición")
x_usuario=float(input("Coordenada 'X'"))
y_usuario=float(input("Coordenada 'Y'"))

coordenadas_usuario=(x_usuario,y_usuario)

def distancia(punto1,punto2):
    distance=math.hypot(punto1[0]-punto2[0],punto1[1]-punto2[1])
    return distance
with open("coordenads.csv","r") as f:
    next(f)
    coordenadas=list(csv.reader(f))
    coordenada_tienda=min(coordenadas,key=lambda c:distancia((int(c[0]),int(c[1])),coordenadas_usuario))

print(f"La tienda mas cercana a {coordenadas_usuario} tiene de coordenadas {coordenada_tienda}") 
    