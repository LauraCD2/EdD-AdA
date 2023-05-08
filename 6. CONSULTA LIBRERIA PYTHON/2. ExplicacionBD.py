#creé una BD de estudiantes con 6500 estudiantes con sus respectivos datos (codigo, nombre, promedio acumulado)

####RANDOMIZADOR DE CODIGOS DE ESTUDIANTES 
import random

# Definir los valores posibles para las dos primeras cifras (CODIGOS CARRERAS)
primeras_cifras = ['10', '11', '14', '16', '18', '19', '20', '21', '22', '23', '24', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '37', '39', '40', '41', '43', '44', '45', '46', '51', '52', '56', '57', '58', '60', '63', '64', '68']

# Generar 6500 números aleatorios de 9 cifras
numeros = []
for i in range(6500):
    # Generar las dos primeras cifras aleatoriamente de la lista de valores posibles de carreras
    primeras = random.choice(primeras_cifras)
    
    # Generar la tercera cifra aleatoriamente (1 o 2) (siglo 20 | siglo 21)
    tercera = random.choice(['1', '2'])
    
    # Generar las siguientes cifras aleatoriamente
    if tercera == '1':
        cuarta_y_quinta = str(random.randint(0, 99)).zfill(2)
    else:
        cuarta_y_quinta = str(random.randint(0, 22)).zfill(2)
    sexta = random.choice(['0', '1'])
    septima_a_novena = str(random.randint(0, 999)).zfill(3)
    
    # Combinar las cifras para formar el número completo
    numero = primeras + tercera + cuarta_y_quinta + sexta + septima_a_novena
    
    # Agregar el número a la lista
    numeros.append(numero)

# Imprimir los números generados, uno por línea
for numero in numeros:
    print(numero)


####RANDOMIZADOR DE NOMBRES DE ESTUDIANTES
import names

# Generar 6500 nombres y apellidos
full_names = []
for i in range(6500):
    full_name = names.get_full_name()
    full_names.append(full_name)
    #
    full_names.append(full_name)

# Escribir los nombres y apellidos en un archivo de texto
with open('nombres_apellidos.txt', 'w') as f:
    for name in full_names:
        f.write(name + '\n')

####RANDOMIZADOR DE PROMEDIO
import random
for i in range(6500):
    promedio = round(random.uniform(2.7, 5.0), 2)
    print("{:.2f}".format(promedio))#.replace(".", ","))





