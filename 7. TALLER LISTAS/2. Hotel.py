#"El director de un hotel desea implementar una sistema de administración para saber la disponibilidad y asignación de habitaciones. 
# Para asignar, registra el número de cédula y el nombre de cada cliente a medida que llega al hotel, junto con el número de habitación que ocupa (el antiguo libro de entradas).
# Igualmente cuando un huésped se retira del hotel se actualiza la disponibilidad de las habitaciones, el libro de entradas y el libro de salida. 
# El director desea en un momento dado contar con la siguiente información:
# - Consultas vigentes por huésped: (1) Individual y (2) total. Las consultas (2) totales pueden ser: (1) Por cédula y (2) por orden de llegada. Para cualquiera de las consultas entregar toda la información asociada al huésped.
# - Consulta de habitaciones: (1) Lista de habitaciones disponibles y (2) Lista de habitaciones ocupadas."

class Hotel:
    # 1. Añadir cliente: Te pide el nombre, la cédula y la habitación (debe estar disponible).
    def anadirCliente(lista):
        nombre = input("Ingrese el nombre del cliente: ")
        cedula = int(input("Ingrese la cedula del cliente: "))
        habitacion = int(input("Ingrese el numero de la habitacion: "))
        if lista.count(habitacion) == 0:
            lista.append(nombre)
            lista.append(cedula)
            lista.append(habitacion)
            print("Se ha añadido el cliente " + nombre + " con cedula " + str(cedula) + " a la habitacion " + str(habitacion))
        else:
            print("La habitacion " + str(habitacion) + " ya esta ocupada")
        return lista

    # 2. Eliminar cliente: Te pide la cédula y te elimina el cliente de la lista.
    def eliminarCliente(lista):
        cedula = int(input("Ingrese la cedula del cliente: "))
        if lista.count(cedula) == 1:
            posicion = lista.index(cedula)
            lista.pop(posicion)
            lista.pop(posicion)
            lista.pop(posicion)
            print("Se ha eliminado el cliente con cedula " + str(cedula))
        else:
            print("La cedula " + str(cedula) + " no esta registrada")
        return lista

    # 3. Consultas vigentes por huésped: (opcion 1) Individual y (opcion 2) total. Las consultas (opcion 2) totales pueden ser: (opcion 1) Por cédula y (opcion 2) por orden de llegada. Para cualquiera de las consultas entregar toda la información asociada al huésped.
    def consultarVigentes(lista):
        opcion = int(input("Ingrese la opcion (1 Individual y 2 Total): "))
        if opcion == 1:
            cedula = int(input("Ingrese la cedula del cliente: "))
            if lista.count(cedula) == 1:
                posicion = lista.index(cedula)
                print("Nombre: " + lista[posicion - 1])
                print("Cedula: " + str(lista[posicion]))
                print("Habitacion: " + str(lista[posicion + 1]))
            else:
                print("La cedula " + str(cedula) + " no esta registrada")
        elif opcion == 2:
            opcion = int(input("Ingrese la opcion: "))
            if opcion == 1:
                cedula = int(input("Ingrese la cedula del cliente: "))
                if lista.count(cedula) == 1:
                    posicion = lista.index(cedula)
                    print("Nombre: " + lista[posicion - 1])
                    print("Cedula: " + str(lista[posicion]))
                    print("Habitacion: " + str(lista[posicion + 1]))
                else:
                    print("La cedula " + str(cedula) + " no esta registrada")
            elif opcion == 2:
                for i in range(0, len(lista), 3):
                    print("Nombre: " + lista[i])
                    print("Cedula: " + str(lista[i + 1]))
                    print("Habitacion: " + str(lista[i + 2]))
            else:
                print("La opcion ingresada no es valida")
        else:
            print("La opcion ingresada no es valida")
        return lista
    
    # 4. Consulta de habitaciones: (opcion 1) Lista de habitaciones disponibles y (opcion 2) Lista de habitaciones ocupadas.
    def consultarHabitaciones(lista):
        opcion = int(input("Ingrese la opcion: "))
        if opcion == 1:
            for i in range(1, 11):
                if lista.count(i) == 0:
                    print("Habitacion " + str(i) + " disponible")
        elif opcion == 2:
            for i in range(1, 11):
                if lista.count(i) == 1:
                    print("Habitacion " + str(i) + " ocupada")
        else:
            print("La opcion ingresada no es valida")
        return lista
    
    # 5. Salir: Termina el programa.
    def salir():
        print("Gracias por usar el programa")
        return False
    
    # 6. Menú: Muestra las opciones y llama a las funciones.
    def menu(lista):
        opcion = 0
        while opcion != 5:
            print("1. Añadir cliente")
            print("2. Eliminar cliente")
            print("3. Consultas vigentes por huésped")
            print("4. Consulta de habitaciones")
            print("5. Salir")
            opcion = int(input("Ingrese la opcion: "))
            if opcion == 1:
                lista = Hotel.anadirCliente(lista)
            elif opcion == 2:
                lista = Hotel.eliminarCliente(lista)
            elif opcion == 3:
                lista = Hotel.consultarVigentes(lista)
            elif opcion == 4:
                lista = Hotel.consultarHabitaciones(lista)
            elif opcion == 5:
                lista = Hotel.salir()
            else:
                print("La opcion ingresada no es valida")
    
#programa principal
lista = []
lista = Hotel.menu(lista)

    
