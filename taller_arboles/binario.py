"""
1. Realice la implementación en Python de un montículo usando árboles binarios. Debe tener las siguientes funciones: Crear el montículo, insertar un elemento, eliminar elemento, recorrido en preorden y por niveles.
2. Realice la implementación en Python de un árbol binario de búsqueda. Debe tener las siguientes funciones: Crear el árbol, insertar un elemento, eliminar elemento, recorrido en preorden y por niveles.
"""

# Importar librerias
import matplotlib.pyplot as plt

# Clase Nodo
def crearNodo(dato):
    return [dato, None, None]

# Clase Arbol
def crearArbol():
    return None

# Funcion para insertar un elemento 
def insertar(arbol, dato):
    if arbol == None:
        return crearNodo(dato)
    else:
        datoRaiz = arbol[0]
        if dato < datoRaiz:
            hijoIzquierdo = arbol[1]
            arbol[1] = insertar(hijoIzquierdo, dato)
        else:
            hijoDerecho = arbol[2]
            arbol[2] = insertar(hijoDerecho, dato)
        return arbol

# Funcion para buscar el minimo
def minimo(arbol):
    if arbol == None:
        return None
    elif arbol[1] == None:
        return arbol[0]
    else:
        return minimo(arbol[1])
    
# Funcion para eliminar elemento
def eliminar(arbol, dato):
    if arbol == None:
        return None
    else:
        datoRaiz = arbol[0]
        if dato < datoRaiz:
            hijoIzquierdo = arbol[1]
            arbol[1] = eliminar(hijoIzquierdo, dato)
        elif dato > datoRaiz:
            hijoDerecho = arbol[2]
            arbol[2] = eliminar(hijoDerecho, dato)
        else:
            hijoIzquierdo = arbol[1]
            hijoDerecho = arbol[2]
            if hijoIzquierdo == None:
                return hijoDerecho
            elif hijoDerecho == None:
                return hijoIzquierdo
            else:
                datoSucesor = minimo(hijoDerecho)
                arbol[0] = datoSucesor
                arbol[2] = eliminar(hijoDerecho, datoSucesor)
        return arbol
    
# Funcion para el recorrido en preorden
def preorden(arbol):
    if arbol != None:
        print(arbol[0], end=", ")
        preorden(arbol[1])
        preorden(arbol[2])  
        
# Funcion para el recorrido por niveles
def porNiveles(arbol):
    if arbol == None:
        return None
    else:
        cola = []
        cola.append(arbol)
        while len(cola) > 0:
            nodo = cola.pop(0)
            print(nodo[0], end=", ")
            if nodo[1] != None:
                cola.append(nodo[1])
            if nodo[2] != None:
                cola.append(nodo[2])
                
# graficar el arbol
def graficar(arbol):
    if arbol == None:
        return None
    else:
        cola = []
        cola.append(arbol)
        while len(cola) > 0:
            nodo = cola.pop(0)
            print(nodo[0], end=", ")
            if nodo[1] != None:
                cola.append(nodo[1])
            if nodo[2] != None:
                cola.append(nodo[2])
                
                