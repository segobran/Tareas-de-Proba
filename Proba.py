import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
with open('AirQualityUCI.csv', 'r') as file:
    data = []

    for line in file:
        parte = line.split(';')
        valor = parte[3].strip()
        data.append(valor)


datos = [int(item) for item in data[1:9358]]
datos.sort()

datos = [dato for dato in datos if dato>=0]

  
media = sum(datos)/len(datos)

s2 = sum([pow((item-media), 2) for item in datos])/(len(datos)-1)
s = pow(s2, 0.5)

Q1 = datos[math.ceil(len(datos)/4)]
Q3 = datos[math.ceil(3*(len(datos)/4))]


if len(datos)%2 == 0:
    Q2 = 0.5*(datos[len(datos)//2]+datos[(len(datos)//2)+1])
else:
    Q2 = datos[(len(datos)+1)//2]

print("Media: ", media)
print("Q1: ", Q1)
print("Q2: ", Q2)
print("Q3: ", Q3)
print("Varianza: ", s2)
print("Desviación estándar:", s)
print(f"Max:{max(datos)}")
print(f"Min:{min(datos)}")


df = pd.DataFrame()

df["COL"] = datos

num_celdas = int(pow(9358,0.5)) #raiz de numero de datos

tamano_celdas = (max(datos)- min(datos))/num_celdas #rango/numceldas

intervalo_celdas = np.linspace(min(datos), 
                                max(datos), num_celdas+1) #creo una distribucion entre el max
                                          # y el min con el tamano correcto 
                                          #segun lo visto en clase
df.hist(bins=intervalo_celdas)
plt.title('Niveles de óxido de estaño registrados')
plt.xlabel('Nivel de óxido de estaño')
plt.ylabel('Cantidad de veces registado por hora')
plt.show()
