def collatz_conjecture(n):
    """Función que genera la secuencia de Collatz para el promedio de 0+3 números dados. 
    Mi código es 222100 por consiguiente N=0+3"""
    if n == 1:  # Caso base: si n es 1, retorna una lista con solo el valor 1 / Base Case: if n=1, return list with just value 1
        return [1]
    elif n % 2 == 0:  # Si n es par / if n is even
        return [n] + collatz_conjecture(n // 2)  # Agrega n a la lista y llama la funcion con n dividido por 2 / add n to the list and call the function with n divided by 2
    else:  # Si n es impar / if n is odd
        return [n] + collatz_conjecture(3 * n + 1)  # Agrega n a la lista y llama la función con 3n+1 / add n to the list and call the function with 3n+1

# Pedir al usuario que ingrese N=0+3 números / Ask user to input N=0+3 numbers
num1 = int(input("Ingresa el  primer  número: "))
num2 = int(input("Ingresa el  segundo número: "))
num3 = int(input("Ingresa el  tercer  número: "))

# Calcular el promedio de los N=0+3 números / Calculate the average of the N=0+3 numbers
promedio = (num1 + num2 + num3) / 3

# Calcular la secuencia de Collatz para el promedio / Calculate the Collatz Conjecture for the average
output = collatz_conjecture(int(promedio))

# Imprimir la secuencia / Print the sequence
print("La secuencia de Collatz para el promedio de los 3 números ingresados es: ", output)