# Realice un algoritmo que solicite inicialmente el número de estudiantes de un curso, 
# Lea para cada uno de ellos las 4 notas (de 0 a 5) correspondientes a los parciales de la asignatura y 
# al finalizar indique: 
#   a. El promedio de la nota final del curso (todas las notas ingresadas) (todas las notas parciales tienen el mismo porcentaje)
#   b. El promedio más alto del curso
#   c. El promedio más bajo del curso.
#   d. El número de personas que no aprobaron la asignatura (nota final menor a 3.0)

#las notas ingresadas deben estar entre 0 y 5
#la asignatura se pierde con una nota menor a 3

#nota final = (nota1 + nota2 + nota3 + nota4) / 4

estudiantes = int(input("Ingrese el número de estudiantes: "))
notas = []
promedios = []
perdidos = 0
for i in range(estudiantes):
    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))
    nota4 = float(input("Ingrese la nota 4: "))
    notas.append([nota1, nota2, nota3, nota4])
    promedio = (nota1 + nota2 + nota3 + nota4) / 4
    promedios.append(promedio)
    if promedio < 3:
        perdidos += 1
print("El promedio de la nota final del curso es:", sum(promedios) / len(promedios))
promedios.sort()
print("El promedio más alto del curso es:",promedios[(len(promedios) - 1)] )
print("El promedio más bajo del curso es:", promedios[0])
print("El número de personas que no aprobaron la asignatura es:", perdidos)