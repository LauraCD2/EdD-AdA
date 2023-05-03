#Suponga que en la UIS hay 6500 estudiantes. Por cada uno de ellos tenemos un registro con el código, nombre y promedio acumulado. Hacer el programa que:

#Imprima el código y el nombre de los estudiantes de la carrera X (debe leerse el código de la carrera a listar) que tengan promedio acumulado igual o mayor a 4 y decir cuántos fueron.
#Imprima el código y el nombre de los estudiantes que ingresaron antes de 1990 (codigo inicia por 1) y están condicionales (promedio entre 2.7 y 3.2).

import numpy as np
import pandas as pd

#importe Base de Datos BD_EstudiantesUIS.csv
estudiantes = pd.read_csv("BD_EstudiantesUIS.csv", sep = ";") #separador es ";"

#Imprima el código y el nombre de los estudiantes de la carrera X que tengan promedio acumulado igual o mayor a 4 y decir cuántos fueron.
#pida la carerra a listar
print("ingrese nombre de la carrera a listar")
carrera = input()

#consulte la base de datos y filtre los estudiantes de la carrera ingresada
estudiantes_carrera = estudiantes[estudiantes["Carrera"] == carrera]

print ("Los estudiantes de la carrera", carrera, "que tienen promedio acumulado igual o mayor a 4 son:")