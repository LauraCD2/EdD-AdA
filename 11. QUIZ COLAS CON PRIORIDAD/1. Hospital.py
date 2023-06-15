#Una variación común que encontramos en diferentes situaciones del mundo real de las colas, son las llamadas Colas de Prioridad.
#Una cola de prioridad es aquella en donde los elementos ingresan con una determinada prioridad, y según esa prioridad salen de la cola.
#Un ejemplo muy común es el sistema de asignación de prioridad de atención en una unidad de urgencias en un hospital.
#Los pacientes llegan en un orden solicitando ser atendidos pero son clasificados y priorizados para su atención.

#En una unidad de urgencias del hospital X, se debe elaborar un programa que organice una cola de prioridad para quienes van a ser atendidos. Cada paciente que ingrese debe registrar:
#- Nombre Completo
#- Edad
#- Síntomas o motivo de consulta
#- Gravedad (Escala numérica de 1 a 5 siendo 1 la mayor gravedad)

#Al ingresar al sistema, si la gravedad es igual que otro paciente, debe asignar prioridad según la edad del paciente así:
#- Prioridad 1: niños menores de 12 años
#- Prioridad 2: adultos mayores de 65 años
#- Prioridad 4: demás pacientes

#Elabore un programa en python, en donde organice la cola de prioridad para la atención en urgencias. 

#Debe tener el siguiente menú:
#Ingresar Paciente (Ingresa datos del paciente que llega y muestra la posición en que será atendido)
#Pasar siguiente paciente (Muestra los datos del siguiente paciente en ser atendido y lo saca de la cola)
#Mostrar la cola (Muestra la cola de atención en ese momento)


#import os

# clase Nodo
class Nodo:
    def __init__(self, value, siguiente=None):
        self.data = value
        self.siguiente = siguiente

# clase Cola        
class Cola:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    # método para saber si la cola está vacía  
    def is_empty(self):
        return self.__head is None
    
    # método para agregar un elemento a la cola
    def enqueue(self, value):
        nuevo = Nodo(value)
        if self.is_empty():
            self.__head = nuevo
            self.__tail = nuevo
        else:
            self.__tail.siguiente = nuevo
            self.__tail = nuevo
        self.__size += 1
    
    # método para eliminar un elemento de la cola    
    def dequeue(self):
        if self.is_empty():
            print("Cola vacía")
        else:
            aux = self.__head.data
            self.__head = self.__head.siguiente
            self.__size -= 1
            return aux
    
    # método para saber el tamaño de la cola     
    def length(self):
        return self.__size
    
    # método para saber cuál es el primer elemento de la cola
    def first(self):
        if self.is_empty():
            return None
        else:
            return self.__head.data
    
    # método para saber cuál es el último elemento de la cola 
    def last(self):
        if self.is_empty():
            return None
        else:
            return self.__tail.data
    
    # método para organizar la cola de prioridad
    def organice(self, value):
        if self.is_empty():
            self.enqueue(value)
        else:
            aux = self.__head
            while aux is not None:
                if aux.data[3] > value[3]:
                    self.enqueue(value)
                    break
                elif aux.data[3] == value[3]:
                    if aux.data[1] > value[1]:
                        self.enqueue(value)
                        break
                    elif aux.data[1] == value[1]:
                        if aux.data[2] > value[2]:
                            self.enqueue(value)
                            break
                aux = aux.siguiente

    # método para mostrar la cola de atención en ese momento
    def mostrar_cola(self):
        aux = self.__head
        while aux is not None:
            print(f"Nombre: {aux.data[0]}, Edad: {aux.data[1]}, Síntomas: {aux.data[2]}, Gravedad: {aux.data[3]}")
            aux = aux.siguiente


# Función principal para ejecutar el programa
def main():
    # Crear una instancia de la cola
    cola_urgencias = Cola()

    while True:
        print("--- Menú ---")
        print("1. Ingresar Paciente")
        print("2. Pasar siguiente paciente")
        print("3. Mostrar la cola")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Ingresar Paciente
            nombre = input("Ingrese el nombre completo del paciente: ")
            edad = int(input("Ingrese la edad del paciente: "))
            sintomas = input("Ingrese los síntomas o motivo de consulta: ")
            gravedad = int(input("Ingrese la gravedad del paciente (1-5): "))

            # Agregar el paciente a la cola de prioridad
            cola_urgencias.organice((nombre, edad, sintomas, gravedad))

            # Mostrar la posición en que será atendido el paciente
            print(f"\nEl paciente {nombre} será atendido en la posición {cola_urgencias.length() + 1}")

        elif opcion == "2":
            # Pasar siguiente paciente
            if cola_urgencias.is_empty():
                print("No hay pacientes en espera.")
            else:
                paciente = cola_urgencias.dequeue()
                print("--- Siguiente Paciente ---")
                print(f"Nombre: {paciente[0]}, Edad: {paciente[1]}, Síntomas: {paciente[2]}, Gravedad: {paciente[3]}")

        elif opcion == "3":
            # Mostrar la cola
            if cola_urgencias.is_empty():
                print("No hay pacientes en espera.")
            else:
                print("--- Cola de Atención ---")
                cola_urgencias.mostrar_cola()

        elif opcion == "4":
            # Salir del programa
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
