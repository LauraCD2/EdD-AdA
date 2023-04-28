#creé una BD de estudiantes con 6500 estudiantes con sus respectivos datos (codigo, nombre, promedio acumulado)
####RANDOMIZADOR DE CODIGOS DE ESTUDIANTES
import random
codigos = []
for i in range(6500):
    codigo = str(random.randint(1, 2)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    codigos.append(codigo)
for codigo in codigos:
    print(codigo)
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
####RANDOMIZADOR DE PROMEDIOS ACUMULADOS DE ESTUDIANTES
import random
from unidecode import unidecode
carreras = ['QUIMICA', 'FISICA', 'BIOLOGIA', 'LICENCIATURA EN MATEMATICAS', 'MATEMATICAS', 
            'INGENIERIA METALURGICA', 'INGENIERIA DE PETROLEOS', 'INGENIERIA QUIMICA', 'GEOLOGIA', 
            'INGENIERIA DE SISTEMAS', 'INGENIERIA CIVIL', 'INGENIERIA ELECTRICA', 'INGENIERIA ELECTRONICA', 
            'INGENIERIA INDUSTRIAL', 'INGENIERIA MECANICA', 'DISEÑO INDUSTRIAL', 
            'MEDICINA', 'NUTRICION Y DIETETICA', 'FISIOTERAPIA', 'MICROBIOLOGIA Y BIOANALISIS', 'ENFERMERIA', 
            'TRABAJO SOCIAL', 'LICENCIATURA EN MUSICA', 'LICENCIATURA EN INGLES', 'LICENCIATURA EN ESPANOL Y LITERATURA', 
            'HISTORIA Y ARCHIVISTICA', 'DERECHO', 'FILOSOFIA', 'ECONOMIA']
for i in range(6500):
    carrera = random.choice(carreras)
    print(carrera)
####RANDOMIZADOR DE AÑOS DE INGRESO DE ESTUDIANTES
import random
for i in range(6500):
    year = random.randint(1950, 2023)
    print(year)
####RANDOMIZADOR DE AÑO DE INGRESO DE ESTUDIANTES
import random
for i in range(6500):
    promedio = round(random.uniform(2.7, 5.0), 2)
    print("{:.2f}".format(promedio).replace(".", ","))





