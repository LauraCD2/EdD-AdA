#Description: Clase Nodo
# Se crea la clase Nodo, que tiene como atributos el valor del nodo y el nodo siguiente
# Se crean los metodos para devolver el valor del nodo, asignar el nodo siguiente y cambiar el valor del nodo

class Nodo:
    #constructor de la clase Nodo
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

    #metodo devolver valor del nodo
    def devolver_valor(self):
        print(self.valor)
    
    #metodo asignar nodo siguiente
    def asignar_sig(self, nodo):
        self.siguiente = nodo
    
    #metodo cambiar valor del nodo
    def cambiar_valor(self, nuevo_valor):
        self.valor = nuevo_valor

#construir elementos de la clase Nodo
nodo1 = Nodo("A")
nodo2 = Nodo("B")
nodo3 = Nodo("C")

#imprimir valor del nodo 1, las dos formas son equivalentes
print("Valor del nodo 1: "+ nodo1.valor)
nodo1.devolver_valor()

#asignar nodo siguiente al nodo 1 e imprimirlo
nodo1.asignar_sig(nodo2)
print("Valor del nodo siguiente al nodo 1: "+ nodo1.siguiente.valor)

#cambiar valor del nodo 1 e imprimirlo
nodo1.cambiar_valor("D")
print("Valor del nodo 1: "+ nodo1.valor)
