#Teniendo en cuenta la teoría de las pilas y colas, desarrolle:
#Implementación para una pila básica en python
#debe:
#Utilizarse listas enlazadas
#Métodos para insertar y eliminar
#Método para validar si está vacía
#Método para contar los elementos en la pila o cola
#Método para devolver el valor del siguiente en salir

class Nodo:
    def __init__(self, value, siguiente=None):
        self.data = value
        self.next = siguiente   

class Pila:
    def __init__(self):
        self.__head = None
        self.__contador = 0
        
    # Método para validar si está vacía
    def is_empty(self):
        return self.__head == None
    
    # Método para insertar
    def push(self, value):
        self.__head = Nodo(value, self.__head)
        self.__contador += 1
        
    # Método para eliminar
    def pop(self):
        if self.is_empty():
            print("La pila está vacía")
        else:
            self.__head = self.__head.next
            self.__contador -= 1    
            
    # Método para contar los elementos en la pila
    def contar_elementos(self):
        return self.__contador
    
    # Método para devolver el valor del siguiente en salir, es decir, el último ingresado
    def siguiente_salir(self):
        if self.is_empty():
            print("La pila está vacía")
        else:
            return self.__head.data
    

#pila = Pila()
#print(f"¿La pila está vacía?: {pila.is_empty()}")
#pila.push(10)
#pila.push(20)
#pila.push(30)
#pila.push(40)
#print(pila.contar_elementos())  # 4
#print(pila.siguiente_salir())  # ultimo ingresado 40
#pila.pop()
