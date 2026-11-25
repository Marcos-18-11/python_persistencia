import numpy as np
consumos=[1250, 1380, 980, 1450 ,1520, 1100, 1600]
dias=["Lúnes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

""" 
1. Consumo total semanal
2. Consumo medio diario
3. Días con mayor y menor consumo 
4. Días con consumo superior a la media
5. Porcentaje de consumo cada día
6. Días con un consumo un 20% inferior a la media
7. Coste total, sabiendo que de lunes a viernes el coste del kw es de 0,02 y en fin de semana es de 0,18
8. Mostrar el consumo diario usando los dos arrays
 """
 
total_semanal=np.sum(consumos)
promedio=np.average(consumos)
print(f"Total de consumo semanal: {total_semanal}")
print(f"Consumo medio diario: {promedio}")
print(f"Día de mayor consumo: {dias[np.argmax(consumos)]}")
print(f"Día de menor consumo: {dias[np.argmin(consumos)]}")

consumo_elevado=(e>promedio for e in consumos)

print("Días de consumo superior al promedio: ")
contador=1
for c in consumo_elevado:
    print(contador)
    if c:
        print("Superior")
    else:
        print("inferior")
    contador+=1
    
tarifas = np.array([0.02, 0.02, 0.02, 0.02, 0.02, 0.018, 0.018])
coste_total = np.sum(consumos * tarifas)
print(f"Porcentajes de consumo semanal: {coste_total:.2f} €")


inferior=promedio-promedio/5
for dia,energia in zip(dias,consumos):
    if energia<=inferior:
        print(f"{dia} se consumió: {energia} kw")
        
for dia, consumo in zip(dias, consumos):
        print(f"El día {dia} ha consumido {((consumo/total_semanal)*100).round(2)}% del total")


#función ZIP, permite combinar dos arrays