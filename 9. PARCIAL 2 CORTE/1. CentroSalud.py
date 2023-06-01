"""Un centro de salud pública necesita gestionar la información de sus pacientes de manera eficiente. Para ello, se ha decidido implementar una estructura de datos basada en listas circular doblemente enlazadas en el lenguaje de programación Python.

Cada paciente tiene asociados los siguientes datos: número de identificación, nombre completo, edad y diagnóstico médico. Se te pide implementar una clase llamada CentroSalud  que permita realizar las siguientes operaciones:

registrar_paciente(identificacion, nombre, edad, diagnostico): Registra un nuevo paciente con los datos proporcionados en la lista doblemente enlazada.
eliminar_paciente(identificacion): Elimina el paciente con el número de identificación dado de la lista doblemente enlazada.
buscar_paciente(identificacion): Devuelve los datos del paciente con el número de identificación dado.
mostrar_pacientes(): Muestra los datos de todos los pacientes registrados en el centro de salud, en el orden en que están enlazados.
mostrar_pacientes_edades(): Muestra la cantidad de pacientes actualmente registrados en los grupos de edad. Bebes(0-2), Primera Infancia(3-5), Niños(6-11), Adolescentes(12-17), Adultos(18-50), Adulto Mayor(51-adelante)

Además, se requiere implementar una funcionalidad adicional:

mostrar_pacientes_diagnosticados(diagnostico): Muestra los datos de los pacientes que tienen el diagnóstico médico especificado.
mostrar_pacientes_nodiagnosticados(): Muestra los datos de los últimos 5 pacientes ingresados al centro que no han sido diagnosticados en orden de llegada.

La implementación de la lista circular doblemente enlazada debe permitir insertar, eliminar y buscar pacientes de manera eficiente, así como mostrar la información de todos los pacientes. 
Todos los datos de los pacientes deben ingresar por teclado al igual que las búsquedas."""

class Paciente:
    def __init__(self, identificacion, nombre, edad, diagnostico):
        self.identificacion = identificacion
        self.nombre = nombre
        self.edad = edad
        self.diagnostico = diagnostico
        self.siguiente = None
        self.anterior = None
    
    def __str__(self):
        return f"{self.identificacion} - {self.nombre} - {self.edad} - {self.diagnostico}"
    
class CentroSalud:
    def __init__(self):
        self.primero = None                  # Paciente inicial
        self.ultimo = None                   # Paciente final
        self.cantidad = 0                    # Cantidad de pacientes
        self.bebes = 0                       # Cantidad de pacientes de 0 a 2 años
        self.primera_infancia = 0            # Cantidad de pacientes de 3 a 5 años
        self.ninos = 0                       # Cantidad de pacientes de 6 a 11 años
        self.adolescentes = 0                # Cantidad de pacientes de 12 a 17 años
        self.adultos = 0                     # Cantidad de pacientes de 18 a 50 años
        self.adultos_mayores = 0             # Cantidad de pacientes de 51 años en adelante
        self.ultimos_nodiagnosticados = []   # Últimos 5 pacientes no diagnosticados
        
    def registrar_paciente(self, identificacion, nombre, edad, diagnostico):
        
        # Verificar si el número de identificación ya existe
        if self.buscar_paciente(identificacion) is not None:
            print("El número de identificación ya existe. No se puede registrar el paciente.")
            return
        
        nuevo = Paciente(identificacion, nombre, edad, diagnostico)
        
        # agrega el paciente a la lista de ultimos no diagnosticados
        if diagnostico == "":
            self.ultimos_nodiagnosticados.append(nuevo)
        if len(self.ultimos_nodiagnosticados) > 5:
            self.ultimos_nodiagnosticados.pop(0)
        
        if self.primero is None:
            self.primero = nuevo
            self.ultimo = nuevo
            self.primero.siguiente = self.ultimo
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
            self.ultimo.anterior = self.primero
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.ultimo = nuevo
        self.cantidad += 1
        self.actualizar_grupos_edad(edad, 1)
        
    def eliminar_paciente(self, identificacion):
        actual = self.primero
        encontrado = False
        for _ in range(self.cantidad):
            if actual.identificacion == identificacion:
                encontrado = True
                break
            actual = actual.siguiente

        if encontrado:
            if self.cantidad == 1:
                self.primero = None
                self.ultimo = None
            elif actual == self.primero:
                self.primero = self.primero.siguiente
                self.primero.anterior = self.ultimo
                self.ultimo.siguiente = self.primero
            elif actual == self.ultimo:
                self.ultimo = self.ultimo.anterior
                self.ultimo.siguiente = self.primero
                self.primero.anterior = self.ultimo
            else:
                actual.anterior.siguiente = actual.siguiente
                actual.siguiente.anterior = actual.anterior

            self.cantidad -= 1
            self.actualizar_grupos_edad(actual.edad, -1)
            return True
        else:
            return False
        
    def buscar_paciente(self, identificacion):
        actual = self.primero
        for _ in range(self.cantidad):
            if actual.identificacion == identificacion:
                return actual
            actual = actual.siguiente
        return None
    
    def mostrar_pacientes(self):
        actual = self.primero
        for _ in range(self.cantidad):
            print(actual)
            actual = actual.siguiente
            
    def mostrar_pacientes_edades(self):
        print(f"Bebes: {self.bebes}")
        print(f"Primera Infancia: {self.primera_infancia}")
        print(f"Niños: {self.ninos}")
        print(f"Adolescentes: {self.adolescentes}")
        print(f"Adultos: {self.adultos}")
        print(f"Adultos Mayores: {self.adultos_mayores}")
        
    def mostrar_pacientes_diagnosticados(self, diagnostico):
        actual = self.primero
        for _ in range(self.cantidad):
            if actual.diagnostico == diagnostico:
                print(actual)
            actual = actual.siguiente
            
    def mostrar_pacientes_nodiagnosticados(self):
        if len(self.ultimos_nodiagnosticados) == 0:
            print("No hay pacientes sin diagnosticar")
        else:
            count = min(len(self.ultimos_nodiagnosticados), 5)
            last_nodiagnosticados = self.ultimos_nodiagnosticados[-count:]
        for paciente in last_nodiagnosticados:
            print(paciente)


    def actualizar_grupos_edad(self, edad, incremento):
        if edad >= 0 and edad <= 2:
            self.bebes += incremento
        elif edad >= 3 and edad <= 5:
            self.primera_infancia += incremento
        elif edad >= 6 and edad <= 11:
            self.ninos += incremento
        elif edad >= 12 and edad <= 17:
            self.adolescentes += incremento
        elif edad >= 18 and edad <= 50:
            self.adultos += incremento
        else:
            self.adultos_mayores += incremento
        
centro = CentroSalud()

while True:
    print("1. Registrar paciente")
    print("2. Eliminar paciente")
    print("3. Buscar paciente")
    print("4. Mostrar todos los pacientes")
    print("5. Mostrar pacientes por grupos de edad")
    print("6. Mostrar pacientes por diagnóstico")
    print("7. Mostrar últimos pacientes no diagnosticados")
    print("0. Salir")
    
    opcion = int(input("Ingrese la opción deseada: "))
    
    if opcion == 1:
        identificacion = input("Ingrese el número de identificación del paciente: ")
        nombre = input("Ingrese el nombre completo del paciente: ")
        edad = int(input("Ingrese la edad del paciente: "))
        diagnostico = input("Ingrese el diagnóstico médico del paciente, para no diagnosticado, de enter: ")
        centro.registrar_paciente(identificacion, nombre, edad, diagnostico)
        
    elif opcion == 2:
        identificacion = input("Ingrese el número de identificación del paciente a eliminar: ")
        if centro.eliminar_paciente(identificacion):
            print("Paciente eliminado exitosamente.")
        else:
            print("El paciente no existe.")
            
    elif opcion == 3:
        identificacion = input("Ingrese el número de identificación del paciente a buscar: ")
        paciente_encontrado = centro.buscar_paciente(identificacion)
        if paciente_encontrado:
            print("Paciente encontrado:")
            print(f"Identificación: {paciente_encontrado.identificacion}")
            print(f"Nombre: {paciente_encontrado.nombre}")
            print(f"Edad: {paciente_encontrado.edad}")
            print(f"Diagnóstico: {paciente_encontrado.diagnostico}")
        else:
            print("Paciente no encontrado.")
            
    elif opcion == 4:
        centro.mostrar_pacientes()
        
    elif opcion == 5:
        centro.mostrar_pacientes_edades()
        
    elif opcion == 6:
        diagnostico = input("Ingrese el diagnóstico médico a buscar: ")
        centro.mostrar_pacientes_diagnosticados(diagnostico)
        
    elif opcion == 7:
        centro.mostrar_pacientes_nodiagnosticados()
        
    elif opcion == 0:
        break
        
    else:
        print("Opción inválida. Intente nuevamente.")
        
        centro = CentroSalud()
