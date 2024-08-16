import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

##with open('AirQualityUCI.csv', 'r') as file:
with open('c:/Users/Usuario/Desktop/Brandon/Universidad/2024 - Sem 2/Probabilidad/Tareas/Tarea01/AirQualityUCI.csv', 'r') as file:
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


RIC = Q3 - Q1 # Brandon lo Añadio
LimSup = 1.5*RIC + Q3 # Brandon lo Añadio
LimInf = Q1 - 1.5*RIC # Brandon lo Añadio

print("Media: ", media)
print("Q1: ", Q1)
print("Q2: ", Q2)
print("Q3: ", Q3)
print("RIC: ", Q3-Q1) # Brandon lo Añadio
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


#****Creacion del diagrama de cajas****
#
figura = plt.figure(figsize=(10,5))
ax = figura.add_subplot(111) 

# Se utiliza boxplot de la libreria "matplotlib" como funcion para generar el diagrama de 
# cajas, el mismo genera la caja con sus respectivos puntos atipicos, cuartiles y bigotes. 
bp = ax.boxplot(datos, vert=0)

# Modifica los bigotes de la funcion boxplot para que sean una linea continua color negro
for whisker in bp['whiskers']:
    whisker.set(color ='#000000', linewidth = 1.5, linestyle ="-")

# Caracterizar los puntos atipicos como circulos
for flier in bp['fliers']:
    flier.set(marker ='o', alpha = 0.5)

# Identificar los cuartiles en el grafico por medio de leyenda los puntos importantes
ax.axvline(Q1, color='green', linestyle='--', linewidth=1.5, label='Q1 (25%)')
ax.axvline(Q2, color='red', linestyle='--', linewidth=1.5, label='Q2 (Mediana)')
ax.axvline(Q3, color='blue', linestyle='--', linewidth=1.5, label='Q3 (75%)')   
ax.axvline(LimSup,color='black', linestyle='-', linewidth=1.5, label='Limite Superior')
ax.axvline(LimInf,color='black', linestyle='-', linewidth=1.5, label='Limite Inferior')

# Añade un cuadro de leyenda para los cuartiles así como añadir titulo y datos de eje
ax.legend()
ax.set_xlabel('Nivel de óxido de estaño')
ax.yaxis.set_ticks([])
ax.set_title('Niveles de óxido de estaño registrados')


plt.show()
