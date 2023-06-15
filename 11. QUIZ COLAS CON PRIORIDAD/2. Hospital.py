class Nodo:
    def __init__(self, value, siguiente=None):
        self.data = value
        self.siguiente = siguiente

class Cola:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def is_empty(self):
        return self.__head is None

    def enqueue(self, value):
        nuevo = Nodo(value)
        if self.is_empty():
            self.__head = nuevo
            self.__tail = nuevo
        else:
            self.__tail.siguiente = nuevo
            self.__tail = nuevo
        self.__size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        aux = self.__head.data
        self.__head = self.__head.siguiente
        self.__size -= 1
        if self.is_empty():
            self.__tail = None
        return aux

    def length(self):
        return self.__size

    def first(self):
        if self.is_empty():
            return None
        return self.__head.data

    def last(self):
        if self.is_empty():
            return None
        return self.__tail.data

    def organize(self, value):
        nuevo = Nodo(value)
        if self.is_empty():
            self.enqueue(value)
        elif value[3] < self.__head.data[3]:
            nuevo.siguiente = self.__head
            self.__head = nuevo
            self.__size += 1
        else:
            actual = self.__head
            while actual.siguiente is not None and value[3] >= actual.siguiente.data[3]:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
            self.__size += 1

    def show_queue(self):
        if self.is_empty():
            print("No hay pacientes en espera.")
        else:
            aux = self.__head
            while aux is not None:
                print(f"Nombre: {aux.data[0]}, Edad: {aux.data[1]}, Síntomas: {aux.data[2]}, Gravedad: {aux.data[3]}")
                aux = aux.siguiente


def main():
    cola_urgencias = Cola()

    while True:
        print("--- Menú ---")
        print("1. Ingresar Paciente")
        print("2. Pasar siguiente paciente")
        print("3. Mostrar la cola")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nIngrese los datos del paciente:")
            nombre = input("Nombre completo: ")
            edad = int(input("Edad: "))
            sintomas = input("Síntomas o motivo de consulta: ")
            gravedad = int(input("Gravedad (1-5): "))

            cola_urgencias.organize((nombre, edad, sintomas, gravedad))
            print(f"\nEl paciente {nombre} será atendido en la posición {cola_urgencias.length()}")

        elif opcion == "2":
            paciente = cola_urgencias.dequeue()
            if paciente:
                print("--- Siguiente Paciente ---")
                print(f"Nombre: {paciente[0]}, Edad: {paciente[1]}, Síntomas: {paciente[2]}, Gravedad: {paciente[3]}")
            else:
                print("No hay pacientes en espera.")

        elif opcion == "3":
            print("--- Cola de Atención ---")
            cola_urgencias.show_queue()

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
