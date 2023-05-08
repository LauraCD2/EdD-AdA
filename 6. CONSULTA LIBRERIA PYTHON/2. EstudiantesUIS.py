#importe el archivo de excel con la base de datos de estudiantes de la UIS (BD_EstudiantesUIS.xlsx)

#1. Imprima el código y el nombre de los estudiantes de la carrera X (debe leerse el código de la carrera a listar) que tengan promedio acumulado igual o mayor a 4 y decir cuántos fueron.
#2. Imprima el código y el nombre de los estudiantes que ingresaron antes de 1990 (codigo inicia por 1) y están condicionales (promedio entre 2.7 y 3.2).

import numpy as np
import pandas as pd

#Imprima el código y el nombre de los estudiantes de la carrera X (debe leerse el código de la carrera a listar) que tengan promedio acumulado igual o mayor a 4 y decir cuántos fueron.
# Pida el numero de la carrera a listar, de la base de datos, lea los estudiantes de la carrera ingresada que tengan promedio acumulado igual o mayor a 4
# LA CARRERA SELECCIONADA corresponde a las dos primeras cifras de la columna A de la base de datos (codigo)

#Importar la base de datos de estudiantes de la UIS
df = pd.read_excel('BD_EstudiantesUIS.xlsx')
#df = pd.read_excel('BD_EstudiantesUIS.xlsx', sheet_name='Hoja 1')

# 1. Imprimir el código y el nombre de los estudiantes de la carrera X que tengan promedio acumulado igual o mayor a 4
carrera = input("Ingrese el código de la carrera a listar: ")

estudiantes_carrera = df[df['codigo'].astype(str).str[:2] == carrera]  # seleccionar estudiantes de la carrera X
estudiantes_cuatro = estudiantes_carrera[estudiantes_carrera['promedio'] >= 4]  # seleccionar estudiantes con promedio mayor o igual a 4

print("Estudiantes de la carrera " + carrera + " con promedio acumulado igual o mayor a 4:")
print(estudiantes_cuatro[['codigo', 'nombre', 'promedio']])  # imprimir código y nombre de los estudiantes

# contar estudiantes con promedio mayor o igual a 4 de la carrera X
num_estudiantes = len(estudiantes_cuatro)
print("Total de estudiantes con promedio igual o mayor a 4: " + str(num_estudiantes))

#2. Imprimir el código y el nombre de los estudiantes que ingresaron antes de 1990 (la tercera cifra es 1 y la cuarta cifra menor que 9) y están condicionales (promedio entre 2.7 y 3.2).
noventa = df[df['codigo'].astype(str).str[2] == '1']  # seleccionar estudiantes que ingresaron en el siglo XX
# seleccionar estudiantes que ingresaron antes de 1990 y están condicionales
novecond = noventa[(noventa['codigo'].astype(str).str[3] < '9') & (noventa['promedio'] >= 2.7) & (noventa['promedio'] <= 3.2)]

print ("Estudiantes que ingresaron antes de 1990 y están condicionales:"+ "\n" + str(novecond[['codigo', 'nombre', 'promedio']]))
print ("Total de estudiantes que ingresaron antes de 1990 y están condicionales: " + str(len(novecond)))


print ("Hecho por: Laura Camila Diaz Delgado - 2220100")