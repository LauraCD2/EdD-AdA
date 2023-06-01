# cree un menu que permita:
# 1. crear una lista simplemente enlazada con 10 numeros aleatorios entre 1 y 100
# 2. crear una lista doblemente enlazada con 10 numeros ingresados por el usuario
# 3. crear una lista circular simplemente enlazada con 10 numeros aleatorios entre 1 y 100
# 4. crear una lista circular doblemente enlazada con 10 numeros ingresados por el usuario
# para cada opcion del menu, cree un submenu que permita:
# 1. mostrar la lista
# 2. mostrar la lista en orden inverso
# 3. mostrar la longitud de la lista
# 4. mostrar el primer elemento de la lista}
# 5. mostrar el ultimo elemento de la lista
# 6. mostrar el elemento de la lista en una posicion
# 7. eliminar el primer elemento de la lista e imprimir la lista resultante
# 8. eliminar el ultimo elemento de la lista e imprimir la lista resultante
# 9. eliminar un elemento de la lista en una posicion e imprimir la lista resultante
# 10. insertar un elemento en la lista en una posicion e imprimir la lista resultante
# 11. insertar un elemento al inicio de la lista e imprimir la lista resultante
# 12. insertar un elemento al final de la lista e imprimir la lista resultante
# 13. salir

import random

class Nodo:
    def __init__(self, valor):
        self.siguiente = None
        self.anterior = None
        self.valor = valor

# clase lista simplemente enlazada
class ListaSE:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.longitud = 0

    def insertar(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza == None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            self.cola = nuevo
        self.longitud += 1

    def mostrar(self):
        aux = self.cabeza
        while aux != None:
            print(aux.valor)
            aux = aux.siguiente

    def mostrarInverso(self): # mostrar la lista en orden inverso
        aux = self.cola
        while aux != None:
            print(aux.valor)
            aux = aux.anterior

    def mostrarLongitud(self):
        print(self.longitud)

    def mostrarPrimero(self):
        print(self.cabeza.valor)

    def mostrarUltimo(self):
        print(self.cola.valor)

    def mostrarPosicion(self, pos):
        aux = self.cabeza
        for i in range(pos):
            aux = aux.siguiente
        print(aux.valor)

    def eliminarPrimero(self):
        self.cabeza = self.cabeza.siguiente
        self.longitud -= 1

    def eliminarUltimo(self):
        aux = self.cabeza
        while aux.siguiente != self.cola:
            aux = aux.siguiente
        aux.siguiente = None
        self.cola = aux
        self.longitud -= 1

    def eliminarPosicion(self, pos):
        aux = self.cabeza
        for i in range(pos-1):
            aux = aux.siguiente
        aux.siguiente = aux.siguiente.siguiente
        self.longitud -= 1

    def insertarPosicion(self, pos, valor):
        nuevo = Nodo(valor)
        aux = self.cabeza
        for i in range(pos-1):
            aux = aux.siguiente
        nuevo.siguiente = aux.siguiente
        aux.siguiente = nuevo
        self.longitud += 1

    def insertarInicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.longitud += 1

    def insertarFinal(self, valor):
        nuevo = Nodo(valor)
        self.cola.siguiente
        self.cola = nuevo
        self.longitud += 1
    
    def menu(self):
        print("1. mostrar la lista")
        print("2. mostrar la lista en orden inverso")
        print("3. mostrar la longitud de la lista")
        print("4. mostrar el primer elemento de la lista")
        print("5. mostrar el ultimo elemento de la lista")
        print("6. mostrar el elemento de la lista en una posicion")
        print("7. eliminar el primer elemento de la lista e imprimir la lista resultante")
        print("8. eliminar el ultimo elemento de la lista e imprimir la lista resultante")
        print("9. eliminar un elemento de la lista en una posicion e imprimir la lista resultante")
        print("10. insertar un elemento en la lista en una posicion e imprimir la lista resultante")
        print("11. insertar un elemento al inicio de la lista e imprimir la lista resultante")
        print("12. insertar un elemento al final de la lista e imprimir la lista resultante")
        print("13. salir")
        opcion = int(input("ingrese una opcion: "))
        return opcion
    
    def submenu(self):
        print("1. crear una lista simplemente enlazada con 10 numeros aleatorios entre 1 y 100")
        print("2. crear una lista doblemente enlazada con 10 numeros ingresados por el usuario")
        print("3. crear una lista circular simplemente enlazada con 10 numeros aleatorios entre 1 y 100")
        print("4. crear una lista circular doblemente enlazada con 10 numeros ingresados por el usuario")
        opcion = int(input("ingrese una opcion: "))
        return opcion
    
    def menuPrincipal(self):
        opcion = self.submenu()
        if opcion == 1:
            for i in range(10):
                self.insertar(random.randint(1,100))
        elif opcion == 2:
            for i in range(10):
                self.insertar(int(input("ingrese un numero: ")))
        elif opcion == 3:
            for i in range(10):
                self.insertar(random.randint(1,100))
            self.cola.siguiente = self.cabeza
        elif opcion == 4:
            for i in range(10):
                self.insertar(int(input("ingrese un numero: ")))
            self.cola.siguiente = self.cabeza
        else:
            print("opcion invalida")
            self.menuPrincipal()
        opcion = self.menu()
        while opcion != 13:
            if opcion == 1:
                self.mostrar()
            elif opcion == 2:
                self.mostrarInverso()
            elif opcion == 3:
                self.mostrarLongitud()
            elif opcion == 4:
                self.mostrarPrimero()
            elif opcion == 5:
                self.mostrarUltimo()
            elif opcion == 6:
                self.mostrarPosicion(int(input("ingrese una posicion: ")))
            elif opcion == 7:
                self.eliminarPrimero()
                self.mostrar()
            elif opcion == 8:
                self.eliminarUltimo()
                self.mostrar()
            elif opcion == 9:
                self.eliminarPosicion(int(input("ingrese una posicion: ")))
                self.mostrar()
            elif opcion == 10:
                self.insertarPosicion(int(input("ingrese una posicion: ")), int(input("ingrese un numero: ")))
                self.mostrar()
            elif opcion == 11:
                self.insertarInicio(int(input("ingrese un numero: ")))
                self.mostrar()
            elif opcion == 12:
                self.insertarFinal(int(input("ingrese un numero: ")))
                self.mostrar()
            else:
                print("opcion invalida")
            opcion = self.menu()
        print("fin del programa")
        
lista = ListaSE()
lista.menuPrincipal()

class ListaDE:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.longitud = 0
    
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza == None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo
        self.longitud += 1
    
    def mostrar(self):
        aux = self.cabeza
        while aux != None:
            print(aux.valor)
            aux = aux.siguiente
        
    def mostrarInverso(self):
        aux = self.cola
        while aux != None:
            print(aux.valor)
            aux = aux.anterior
    
    def mostrarLongitud(self):
        print(self.longitud)
        
    def mostrarPrimero(self):
        print(self.cabeza.valor)
        
    def mostrarUltimo(self):
        print(self.cola.valor)
    
    def mostrarPosicion(self, pos):
        aux = self.cabeza
        for i in range(pos):
            aux = aux.siguiente
        print(aux.valor)
    
    def eliminarPrimero(self):
        self.cabeza = self.cabeza.siguiente
        self.cabeza.anterior = None
        self.longitud -= 1
    
    def eliminarUltimo(self):
        self.cola = self.cola.anterior
        self.cola.siguiente = None
        self.longitud -= 1
    
    def eliminarPosicion(self, pos):
        aux = self.cabeza
        for i in range(pos):
            aux = aux.siguiente
        aux.anterior.siguiente = aux.siguiente
        aux.siguiente.anterior = aux.anterior
        self.longitud -= 1
    
    def insertarPosicion(self, pos, valor):
        nuevo = Nodo(valor)
        aux = self.cabeza
        for i in range(pos):
            aux = aux.siguiente
        aux.anterior.siguiente = nuevo
        nuevo.anterior = aux.anterior
        nuevo.siguiente = aux
        aux.anterior = nuevo
        self.longitud += 1
    
    def insertarInicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza.anterior = nuevo
        self.cabeza = nuevo
        self.longitud += 1
    
    def insertarFinal(self, valor):
        self.insertar(valor)
    
    def menu(self):
        print("1. mostrar la lista")
        print("2. mostrar la lista en orden inverso")
        print("3. mostrar la longitud de la lista")
        print("4. mostrar el primer elemento de la lista")
        print("5. mostrar el ultimo elemento de la lista")
        print("6. mostrar el elemento de la lista en una posicion")
        print("7. eliminar el primer elemento de la lista e imprimir la lista resultante")
        print("8. eliminar el ultimo elemento de la lista e imprimir la lista resultante")
        print("9. eliminar un elemento de la lista en una posicion e imprimir la lista resultante")
        print("10. insertar un elemento en la lista en una posicion e imprimir la lista resultante")
        print("11. insertar un elemento al inicio de la lista e imprimir la lista resultante")
        print("12. insertar un elemento al final de la lista e imprimir la lista resultante")
        print("13. salir")
        opcion = int(input("ingrese una opcion: "))
        return opcion
    
    def submenu(self):
        print("1. crear una lista doblemente enlazada con 10 numeros aleatorios entre 1 y 100")
        print("2. crear una lista doblemente enlazada con 10 numeros ingresados por el usuario")
        print("3. crear una lista doblemente enlazada circular con 10 numeros aleatorios entre 1 y 100")
        print("4. crear una lista doblemente enlazada circular con 10 numeros ingresados por el usuario")
        opcion = int(input("ingrese una opcion: "))
        return opcion
    
Lista = ListaDE()
Lista.menuPrincipal()

class ListaC:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.longitud = 0
        
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza == None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo
        self.longitud += 1
        
    def mostrar(self):
        aux = self.cabeza
        for i in range(self.longitud):
            print(aux.valor)
            aux = aux.siguiente
    
    def mostrarInverso(self):
        aux = self.cola
        for i in range(self.longitud):
            print(aux.valor)
            aux = aux.anterior
            
    def mostrarLongitud(self):
        print(self.longitud)
        
    def mostrarPrimero(self):
        print(self.cabeza.valor)
        
    def mostrarUltimo(self):
        print(self.cola.valor)
    
    def mostrarPosicion(self, pos):
        aux = self.cabeza
        for i in range(pos):
            aux = aux.siguiente
        print(aux.valor)
        
    def eliminarPrimero(self):
        self.cabeza = self.cabeza.siguiente
        self.cabeza.anterior = None
        self.cola.siguiente = self.cabeza
        self.cabeza.anterior = self.cola
        self.longitud -= 1
        
    def eliminarUltimo(self):
        self.cola = self.cola.anterior
        self.cola.siguiente = self.cabeza
        self.cabeza.anterior = self.cola
        self.longitud -= 1
    
    def eliminarPosicion(self, pos):
        aux = self.cabeza
        for i in range(pos):
            aux = aux.siguiente
        aux.anterior.siguiente = aux.siguiente
        aux.siguiente.anterior = aux.anterior
        self.longitud -= 1
        
    def insertarPosicion(self, pos, valor):
        nuevo = Nodo(valor)
        aux = self.cabeza
        for i in range(pos):
            aux = aux.siguiente
        aux.anterior.siguiente = nuevo
        nuevo.anterior = aux.anterior
        nuevo.siguiente = aux
        aux.anterior = nuevo
        self.longitud += 1
    
    def insertarInicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza.anterior = nuevo
        self.cabeza = nuevo
        self.longitud += 1
        
    def insertarFinal(self, valor):
        self.insertar(valor)
        
    def menu(self):
        print("1. mostrar la lista")
        print("2. mostrar la lista en orden inverso")
        print("3. mostrar la longitud de la lista")
        print("4. mostrar el primer elemento de la lista")
        print("5. mostrar el ultimo elemento de la lista")
        print("6. mostrar el elemento de la lista en una posicion")
        print("7. eliminar el primer elemento de la lista e imprimir la lista resultante")
        print("8. eliminar el ultimo elemento de la lista e imprimir la lista resultante")
        print("9. eliminar un elemento de la lista en una posicion e imprimir la lista resultante")
        print("10. insertar un elemento en la lista en una posicion e imprimir la lista resultante")
        print("11. insertar un elemento al inicio de la lista e imprimir la lista resultante")
        print("12. insertar un elemento al final de la lista e imprimir la lista resultante")
        print("13. salir")
        opcion = int(input("ingrese una opcion: "))
        return opcion
    
    def submenu(self):
        print("1. crear una lista doblemente enlazada con 10 numeros aleatorios entre 1 y 100")
        print("2. crear una lista doblemente enlazada con 10 numeros ingresados por el usuario")
        print("3. crear una lista doblemente enlazada circular con 10 numeros aleatorios entre 1 y 100")
        print("4. crear una lista doblemente enlazada circular con 10 numeros ingresados por el usuario")
        opcion = int(input("ingrese una opcion: "))
        return opcion
    
Lista = ListaC()
Lista.menuPrincipal()

class ListaCD:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.longitud = 0
        
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza == None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo
        self.cola.siguiente = self.cabeza
        self.cabeza.anterior = self.cola
        self.longitud += 1
        
    def mostrar(self):
        aux = self.cabeza
        for i in range(self.longitud):
            print(aux.valor)
            aux = aux.siguiente
            
    def mostrarInverso(self):
        aux = self.cola
        for i in range(self.longitud):
            print(aux.valor)
            aux = aux.anterior
            
    def mostrarLongitud(self):
        print(self.longitud)
        
    def mostrarPrimero(self):
        print(self.cabeza.valor)
        
    def mostrarUltimo(self):
        print(self.cola.valor)
        
    def mostrarPosicion(self, pos):
        aux = self.cabeza
        for i in range(pos):
            aux = aux.siguiente
        print(aux.valor)
        
    def eliminarPrimero(self):
        self.cabeza = self.cabeza.siguiente
        self.cabeza.anterior = None
        self.cola.siguiente = self.cabeza
        self.cabeza.anterior = self.cola
        self.longitud -= 1
        
    def eliminarUltimo(self):
        self.cola = self.cola.anterior
        self.cola.siguiente = self.cabeza
        self.cabeza.anterior = self.cola
        self.longitud -= 1
        
    def eliminarPosicion(self, pos):
        aux = self.cabeza
        for i in range(pos):
            aux = aux.siguiente
        aux.anterior.siguiente = aux.siguiente
        aux.siguiente.anterior = aux.anterior
        self.longitud -= 1
        
    def insertarPosicion(self, pos, valor):
        nuevo = Nodo(valor)
        aux = self.cabeza
        for i in range(pos):
            aux = aux.siguiente
        aux.anterior.siguiente = nuevo
        nuevo.anterior = aux.anterior
        nuevo.siguiente = aux
        aux.anterior = nuevo
        self.longitud += 1
        
    def insertarInicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza.anterior = nuevo
        self.cabeza = nuevo
        self.longitud += 1
        
    def insertarFinal(self, valor):
        self.insertar(valor)
        
    def menu(self):
        print("1. mostrar la lista")
        print("2. mostrar la lista en orden inverso")
        print("3. mostrar la longitud de la lista")
        print("4. mostrar el primer elemento de la lista")
        print("5. mostrar el ultimo elemento de la lista")
        print("6. mostrar el elemento de la lista en una posicion")
        print("7. eliminar el primer elemento de la lista e imprimir la lista resultante")
        print("8. eliminar el ultimo elemento de la lista e imprimir la lista resultante")
        print("9. eliminar un elemento de la lista en una posicion e imprimir la lista resultante")
        print("10. insertar un elemento en la lista en una posicion e imprimir la lista resultante")
        print("11. insertar un elemento al inicio de la lista e imprimir la lista resultante")
        print("12. insertar un elemento al final de la lista e imprimir la lista resultante")
        print("13. salir")
        opcion = int(input("ingrese una opcion: "))
        return opcion
    
    def submenu(self):
        print("1. crear una lista doblemente enlazada con 10 numeros aleatorios entre 1 y 100")
        print("2. crear una lista doblemente enlazada con 10 numeros ingresados por el usuario")
        print("3. crear una lista doblemente enlazada circular con 10 numeros aleatorios entre 1 y 100")
        print("4. crear una lista doblemente enlazada circular con 10 numeros ingresados por el usuario")
        opcion = int(input("ingrese una opcion: "))
        return opcion
    
Lista = ListaCD()
Lista.menuPrincipal()


    