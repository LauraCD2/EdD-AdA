#importe el archivo de excel con la base de datos de estudiantes de la UIS (BD_EstudiantesUIS.xlsx)

#Imprima el código y el nombre de los estudiantes de la carrera X (debe leerse el código de la carrera a listar) que tengan promedio acumulado igual o mayor a 4 y decir cuántos fueron.
#Imprima el código y el nombre de los estudiantes que ingresaron antes de 1990 (codigo inicia por 1) y están condicionales (promedio entre 2.7 y 3.2).

import numpy as np
import pandas as pd

#importe Base de Datos BD_EstudiantesUIS.xlsx
#import openpyxl as xl

#wb = xl.load_workbook('BD_EstudiantesUIS.xlsx')
#sheet = wb['Hoja1']

#Imprima el código y el nombre de los estudiantes de la carrera X (debe leerse el código de la carrera a listar) que tengan promedio acumulado igual o mayor a 4 y decir cuántos fueron.
# Pida el numero de la carrera a listar
# de la base de datos, lea el codigo y el nombre de los estudiantes de la carrera ingresada que tengan promedio acumulado igual o mayor a 4
# LA CARRERA SELECCIONADA corresponde a las dos primeras cifras de la columna A de la base de datos (codigo)
#carrera = input("Ingrese el código de la carrera a listar: ")

# importar la base de datos
df = pd.read_excel('BD_EstudiantesUIS.xlsx')

# Imprimir el código y el nombre de los estudiantes de la carrera X que tengan promedio acumulado igual o mayor a 4
carrera = input("Ingrese el código de la carrera a listar: ")

estudiantes_carrera = df[df['codigo'].astype(str).str[:2] == carrera]  # seleccionar estudiantes de la carrera X
estudiantes_aprobados = estudiantes_carrera[estudiantes_carrera['promedio'] >= 4]  # seleccionar estudiantes con promedio mayor o igual a 4

print("Estudiantes de la carrera " + carrera + " con promedio acumulado igual o mayor a 4:")
print(estudiantes_aprobados[['codigo', 'nombre']])  # imprimir código y nombre de los estudiantes

# contar estudiantes
num_estudiantes = len(estudiantes_aprobados)
print("Total de estudiantes con promedio igual o mayor a 4: " + str(num_estudiantes))
