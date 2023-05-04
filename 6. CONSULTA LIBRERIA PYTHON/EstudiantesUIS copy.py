#importe el archivo de excel con la base de datos de estudiantes de la UIS (BD_EstudiantesUIS.xlsx)

#1. Imprima el código y el nombre de los estudiantes de la carrera X (debe leerse el código de la carrera a listar) que tengan promedio acumulado igual o mayor a 4 y decir cuántos fueron.
#2. Imprima el código y el nombre de los estudiantes que ingresaron antes de 1990 (codigo inicia por 1) y están condicionales (promedio entre 2.7 y 3.2).

import numpy as np
#import pandas as pd
import streamlit as st

#Imprima el código y el nombre de los estudiantes de la carrera X (debe leerse el código de la carrera a listar) que tengan promedio acumulado igual o mayor a 4 y decir cuántos fueron.
# Pida el numero de la carrera a listar, de la base de datos, lea los estudiantes de la carrera ingresada que tengan promedio acumulado igual o mayor a 4
# LA CARRERA SELECCIONADA corresponde a las dos primeras cifras de la columna A de la base de datos (codigo)

# importar la base de datos (este no funciona en streamlit) CON STREAMLIT
uploaded_file = st.file_uploader(
    "BD_EstudiantesUIS.xlsx", accept_multiple_files=False)
if uploaded_file is not None:
    file_name = uploaded_file
else:
    file_name = "BD_EstudiantesUIS.xlsx"
#df = pd.read_excel('BD_EstudiantesUIS.xlsx')

# 1. Imprimir el código y el nombre de los estudiantes de la carrera X que tengan promedio acumulado igual o mayor a 4
carrera = input("Ingrese el código de la carrera a listar: ")
