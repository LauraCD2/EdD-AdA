#Diseñar un algoritmo para calcular el porcentaje de hombres y de mujeres que hay en un grupo,
#dados los totales de hombres y de mujeres (se ingresan por consola)

#Entrada
print("Ingrese el total de hombres")
hombres = int(input())
print("Ingrese el total de mujeres")
mujeres = int(input())

#Proceso
total = hombres + mujeres
porcentajeHombres = (hombres * 100) / total
porcentajeMujeres = (mujeres * 100) / total

#Salida
print("El porcentaje de hombres es: ", porcentajeHombres)
print("El porcentaje de mujeres es: ", porcentajeMujeres)
