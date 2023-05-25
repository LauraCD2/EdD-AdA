#crear:
#Una lista CIRCULAR DOBLEMENTE ENLAZADA
#Método para insertar en:
    #a. Inicio
    #b. Final
#Método para eliminar nodo
#Método para mostrar la lista en cualquiera de los 2 sentidos (Adelante hacia atrás o viceversa) 
#Método agregar en cualquier lugar de la lista

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaCDE:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        if self.primero == None:
            return True
        else:
            return False

    #Método para agregar nodos al inicio
    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.__unir_nodos()

    #Método para agregar nodos al final
    def agregar_final(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.__unir_nodos()

    #Método para eliminar nodos al inicio
    def eliminar_inicio(self):
        if self.vacia():
            print("No hay elementos para eliminar")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
        self.__unir_nodos()

    #Método para eliminar nodos al final
    def eliminar_final(self):
        if self.vacia():
            print("No hay elementos para eliminar")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
        self.__unir_nodos()
    
    #Método para agregar nodos en cualquier lugar de la lista
    def agregar(self, dato, referencia):
        if self.vacia():
            print("No hay elementos para agregar")
        else:
            aux = self.primero
            while aux:
                if aux.dato == referencia:
                    nuevo = Nodo(dato)
                    anterior = aux.anterior
                    anterior.siguiente = nuevo
                    nuevo.siguiente = aux
                    aux.anterior = nuevo
                    nuevo.anterior = anterior
                aux = aux.siguiente
                if aux == self.primero:
                    break
    
    #Método para eliminar nodos en cualquier lugar de la lista
    def eliminar(self, referencia):
        if self.vacia():
            print("No hay elementos para eliminar")
        else:
            aux = self.primero
            while aux:
                if aux.dato == referencia:
                    anterior = aux.anterior
                    siguiente = aux.siguiente
                    anterior.siguiente = siguiente
                    siguiente.anterior = anterior
                aux = aux.siguiente
                if aux == self.primero:
                    break
    
    #Método para mostrar los elementos de la lista 
    def recorrer_inicio(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break

    #Método para mostrar los elementos de la lista en sentido inverso
    def recorrer_final(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior
            if aux == self.ultimo:
                break