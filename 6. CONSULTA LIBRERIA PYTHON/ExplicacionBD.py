#creé una BD de estudiantes con 6500 estudiantes con sus respectivos datos (codigo, nombre, promedio acumulado)

####RANDOMIZADOR DE CODIGOS DE ESTUDIANTES 
import random

# Definir los valores posibles para las dos primeras cifras (CODIGOS CARRERAS)
primeras_cifras = ['10', '11', '14', '16', '18', '19', '20', '21', '22', '23', '24', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '37', '39', '40', '41', '43', '44', '45', '46', '51', '52', '56', '57', '58', '60', '63', '64', '68']

# Generar 6500 números aleatorios de 9 cifras
numeros = []
for i in range(6500):
    # Generar las dos primeras cifras aleatoriamente
    primeras = random.choice(primeras_cifras)
    
    # Generar la tercera cifra aleatoriamente (1 o 2) (SEMESTRE DE INGRESO)
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
import random
nombres = ['Juan', 'María', 'Pedro', 'Luisa', 'Ana', 'Jorge', 'Marta', 'Carlos', 'Laura', 'Andrés', 'Gabriela', 'Roberto', 'Sofía', 'Alejandro', 'Isabella', 'Diego', 'Valentina', 'Fernando', 'Catalina', 'Pablo', 'Carolina', 'Mauricio', 'Natalia', 'Lorenzo', 'Jimena', 'Simón', 'Melissa', 'Lucas', 'Daniela', 'Gustavo', 'Daniela', 'Emilio', 'Camila', 'José', 'Mariana', 'Raúl', 'Paola', 'Mario', 'Juliana', 'Tomás', 'Adriana', 'Federico', 'Gabriela', 'Ricardo', 'Verónica', 'Julián', 'Lucía', 'Esteban', 'Andrea', 'Eduardo', 'Clara']
apellidos = ['González', 'Rodríguez', 'García', 'Martínez', 'Sánchez', 'Pérez', 'López', 'Fernández', 'Gómez', 'Díaz', 'Torres', 'Vargas', 'Ramos', 'Romero', 'Suárez', 'Castro', 'Álvarez', 'Ruiz', 'Mendoza', 'Hernández', 'Ramírez', 'Flores', 'Vega', 'Cruz', 'Gutiérrez', 'Ortiz', 'Reyes', 'Morales', 'Núñez', 'Carrasco', 'Medina', 'Acosta', 'Guzmán', 'Ponce', 'Barrera', 'Salas', 'Maldonado', 'Villalobos', 'Olivera', 'Delgado', 'Vera', 'Cabrera', 'Molina', 'Miranda', 'Lara', 'Valenzuela', 'Navarro', 'Valdés', 'Ibarra', 'Bautista', 'Cortés', 'Soria']
nombres_completos = []
for i in range(6500):
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    nombres_completos.append(nombre + ' ' + apellido)
for nombre_completo in nombres_completos:
    print(nombre_completo)


####RANDOMIZADOR DE PROMEDIO
import random
for i in range(6500):
    promedio = round(random.uniform(2.7, 5.0), 2)
    print("{:.2f}".format(promedio))#.replace(".", ","))





