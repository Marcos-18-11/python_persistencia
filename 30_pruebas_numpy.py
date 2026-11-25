import numpy as np
datos=np.array([10,2,11,8,20])
datos2=np.array([[4,8,11,-1,20],[5,3,11,0,0]])
print(datos[0])
print(datos2[1][1])

print(datos2[datos2>0])
for fila in datos2:
    for celda in fila:
        print(celda)
a1=np.array([200,120,39])
a2=np.array([130,380,369])
suma=np.add(a1,a2)
print(suma)
print(f"Promedio: {np.average(suma)}")
print(f"Mayor: posición - {np.argmax(suma)} ,valor: {np.max(suma)}")
print(f"Menor: posición - {np.argmin(suma)} ,valor: {np.min(suma)}")
 
print(f"Condición mayor a 0: {np.extract(datos2>0,datos2)}") 