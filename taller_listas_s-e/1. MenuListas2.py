#"Vamos a crear un programa que tenga el siguiente menú:
# 1. Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
# 2. Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
# 3. Longitud de la lista: te muestra el número de elementos de la lista.
# 4. Eliminar el último número: Muestra el último número de la lista y lo borra.
# 5. Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
# 6. Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
# 7. Posiciones de un número: Te pide un número y te dice en qué posiciones está (contando desde 1).
# 8. Mostrar números: Muestra los números de la lista
# 9. Salir "

#use listas simplemente enlazadas
class MenuLista:
        # 1. Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
        def anadirNumero(lista):
            numero = int(input("Ingrese un numero: "))
            lista.append(numero)
            print("El número agregado a la lista es " + str(numero) + ""+ "\n")
            return lista
    
        # 2. Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
        def anadirNumeroPosicion(lista):
            numero = int(input("Ingrese un numero: "))
            posicion = int(input("Ingrese la posicion: "))
            if posicion > len(lista):
                print("La posicion no existe en la lista")
            else:
                lista.insert(posicion-1, numero)
            print("El número agregado a la lista"+ "\n" + "en la posicion " + str(posicion) + " es: " + str(numero)+ "\n")
            return lista
            
            
    
        # 3. Longitud de la lista: te muestra el número de elementos de la lista.
        def longitudLista(lista):
            print("La longitud de la lista es: " + str(len(lista))+ "\n")
            return lista
    
        # 4. Eliminar el último número: Muestra el último número de la lista y lo borra.
        def eliminarUltimoNumero(lista):
            print("El ultimo numero de la lista es: " + str(lista.pop())+ "\n")
            return lista
    
        # 5. Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
        def eliminarNumero(lista):
            posicion = int(input("Ingrese la posicion: "))
            if posicion > len(lista):
                print("La posicion no existe en la lista")
            else:
                print("El numero eliminado es: " + str(lista.pop(posicion-1))+ "\n")
            return lista
    
        # 6. Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
        def contarNumeros(lista):
            numero = int(input("Ingrese el numero a contar: "))
            if lista.count(numero) == 0:
                print("El numero no esta en la lista")
            else:
                print("El numero " + str(numero) + " aparece " + str(lista.count(numero)) + " veces en la lista"+ "\n")
            return lista
        
        # 7. Posiciones de un número: Te pide un número y te dice en qué posiciones está (contando desde 1).
        def posicionesNumero(lista):
            numero = int(input("Ingrese el numero a buscar: "))
            if lista.count(numero) == 0:
                print("El numero no esta en la lista")
            else:
                print("El numero " + str(numero) + " esta en las posiciones: ")
                for i in range(len(lista)):
                    if lista[i] == numero:
                        print(i+1)
            return lista
        
        # 8. Mostrar números: Muestra los números de la lista
        def mostrarNumeros(lista):
            print("Los numeros de la lista son: ")
            for i in range(len(lista)):
                print(lista[i])
            return lista
        
        # 9. Salir
        def salir():
            print("Saliendo del programa")
            return 0
        
        def menu():
            lista = []
            while True:
                print("1. Añadir número a la lista")
                print("2. Añadir número de la lista en una posición")
                print("3. Longitud de la lista")
                print("4. Eliminar el último número")
                print("5. Eliminar un número")
                print("6. Contar números")
                print("7. Posiciones de un número")
                print("8. Mostrar números")
                print("9. Salir")
                opcion = int(input("Ingrese una opcion: "))
                if opcion == 1:
                    lista = MenuLista.anadirNumero(lista)
                elif opcion == 2:
                    lista = MenuLista.anadirNumeroPosicion(lista)
                elif opcion == 3:
                    lista = MenuLista.longitudLista(lista)
                elif opcion == 4:
                    lista = MenuLista.eliminarUltimoNumero(lista)
                elif opcion == 5:
                    lista = MenuLista.eliminarNumero(lista)
                elif opcion == 6:
                    lista = MenuLista.contarNumeros(lista)
                elif opcion == 7:
                    lista = MenuLista.posicionesNumero(lista)
                elif opcion == 8:
                    lista = MenuLista.mostrarNumeros(lista)
                elif opcion == 9:
                    MenuLista.salir()
                    break
                else:
                    print("Opcion invalida")
            return 0
        
        menu()
        