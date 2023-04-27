#funcion lambda que imprima los numeros pares del 1-100

import numpy as np

#funcion lambda que imprima los numeros pares del 1-100
zy = lambda x: x%2==0

#imprimir solo los numeros pares del 1-100
for i in range(1,101):
    if zy(i):
        print(i)
