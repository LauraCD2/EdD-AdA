# crear clase lista con los atributos tamaño y PrimerNodo,  
# crear los métodos Agregar_Nodo_Inicio, Agregar_Nodo_Final, Calcular_Tamanio, Retornar_Lista, Buscar, Eliminar
# probar los métodos de la clase Lista

class Lista:
    def __init__(self, cabeza=None):
        self.cabeza = cabeza
        self.tamaño = 0
    
    def Agregar_Nodo_Inicio(self, nodo):
        nodo.asignar_sig(self.cabeza)
        self.cabeza = nodo
        self.tamaño += 1
    
    def Agregar_Nodo_Final(self, nodo):
        if self.cabeza == None:
            self.cabeza = nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente != None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.asignar_sig(nodo)
        self.tamaño += 1
    
    def Calcular_Tamanio(self):
        return self.tamaño
    
    def Retornar_Lista(self):
        lista = list()
        nodo_actual = self.cabeza
        while nodo_actual != None:
            lista.append(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
        return lista
    
    def Buscar(self, valor):
        nodo_actual = self.cabeza
        posicion = 0
        while nodo_actual != None:
            if nodo_actual.valor == valor:
                return posicion
            else:
                nodo_actual = nodo_actual.siguiente
                posicion += 1
        return -1
    
    def Eliminar(self, posicion):
        if posicion == 0:
            self.cabeza = self.cabeza.siguiente
        else:
            nodo_anterior = self.cabeza
            nodo_actual = self.cabeza.siguiente
            for i in range(1, posicion):
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.siguiente
            nodo_anterior.asignar_sig(nodo_actual.siguiente)
        self.tamaño -= 1
        
    #probar los métodos de la clase Lista
    lista = list("abcde")
    print ("Lista inicial:" + str(lista))
    
    #agregar nodo al inicio
    lista.insert(0, "z")
    print ("Lista con nodo al inicio:" + str(lista))
    
    #agregar nodo al final
    lista.append("w")
    print ("Lista con nodo al final:" + str(lista))
    
    #calcular tamaño
    print ("Tamaño de la lista:" + str(len(lista)))
    
    #retornar lista
    print ("Lista:" + str(lista))
    
    #buscar
    print ("Posición del nodo con valor 'c':" + str(lista.index("c")))
    
    #eliminar
    lista.remove("c")
    print ("Lista con nodo eliminado:" + str(lista))
    
    