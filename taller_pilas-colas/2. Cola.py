#Teniendo en cuenta la teoría de las colas, desarrolle:
#Implementación para una cola básica en python
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
        
class Cola:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__contador = 0
        
    # Método para validar si está vacía
    def is_empty(self):
        return self.__head == None
    
    # Método para insertar
    def push(self, value):
        nuevo = Nodo(value)
        if self.is_empty():
            self.__head = nuevo
            self.__tail = nuevo
        else:
            self.__tail.next = nuevo
            self.__tail = nuevo
        self.__contador += 1
        
    # Método para eliminar
    def pop(self):
        if self.is_empty():
            print("La cola está vacía")
        else:
            self.__head = self.__head.next
            self.__contador -= 1
            
    # Método para contar los elementos en la cola
    def contar_elementos(self):
        return self.__contador
    
    # Método para devolver el valor del siguiente en salir, es decir, el primero ingresado
    def siguiente_salir(self):
        if self.is_empty():
            print("La cola está vacía")
        else:
            return self.__head.data
        
#cola = Cola()
#print(f"¿La cola está vacía?: {cola.is_empty()}")
#cola.push(10)
#cola.push(20)
#cola.push(30)
#cola.push(40)
#print(cola.contar_elementos())  # 4
#print(cola.siguiente_salir())  # primero ingresado 10
#cola.pop()