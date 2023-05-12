#crear clase lista e insertar nuevo nodo en sus distintas posiciones

class Lista:
    def __init__(self, cabeza=None):
        self.cabeza = cabeza
    
    #Asigne los valores de la lista
    valores = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    
    #Construya la lista
    lista = list()
    print ("Lista inicial:" + str(valores))
    
    def insertar(self, nodo, posicion):
        if posicion == 0:
            nodo.asignar_sig(self.cabeza)
            self.cabeza = nodo
        else:
            nodo_anterior = self.cabeza
            nodo_actual = self.cabeza.siguiente
            for i in range(1, posicion):
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.siguiente
            nodo_anterior.asignar_sig(nodo)
            nodo.asignar_sig(nodo_actual)
    
    def imprimir(self):
        nodo_actual = self.cabeza
        while nodo_actual != None:
            print(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
    
    def eliminar(self, posicion):
        if posicion == 0:
            self.cabeza = self.cabeza.siguiente
        else:
            nodo_anterior = self.cabeza
            nodo_actual = self.cabeza.siguiente
            for i in range(1, posicion):
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.siguiente
            nodo_anterior.asignar_sig(nodo_actual.siguiente)
    
    def buscar(self, valor):
        nodo_actual = self.cabeza
        posicion = 0
        while nodo_actual != None:
            if nodo_actual.valor == valor:
                return posicion
            else:
                nodo_actual = nodo_actual.siguiente
                posicion += 1
        return -1
    
    def longitud(self):
        nodo_actual = self.cabeza
        longitud = 0
        while nodo_actual != None:
            longitud += 1
            nodo_actual = nodo_actual.siguiente
        return longitud
    
    def devolver_nodo(self, posicion):
        nodo_actual = self.cabeza
        for i in range(0, posicion):
            nodo_actual = nodo_actual.siguiente
        return nodo_actual
    
    def devolver_valor(self, posicion):
        nodo_actual = self.cabeza
        for i in range(0, posicion):
            nodo_actual = nodo_actual.siguiente
        return nodo_actual.valor
    
    def devolver_posicion(self, valor):
        nodo_actual = self.cabeza
        posicion = 0
        while nodo_actual != None:
            if nodo_actual.valor == valor:
                return posicion
            else:
                nodo_actual = nodo_actual.siguiente
                posicion += 1
        return -1
    
    def cambiar_valor(self, posicion, nuevo_valor):
        nodo_actual = self.cabeza
        for i in range(0, posicion):
            nodo_actual = nodo_actual.siguiente
        nodo_actual.cambiar_valor(nuevo_valor)
        
    def cambiar_siguiente(self, posicion, nuevo_siguiente):
        nodo_actual = self.cabeza
        for i in range(0, posicion):
            nodo_actual = nodo_actual.siguiente
        nodo_actual.asignar_sig(nuevo_siguiente)
        
    def cambiar_cabeza(self, nueva_cabeza):
        self.cabeza = nueva_cabeza
    
    def devolver_cabeza(self):
        return self.cabeza