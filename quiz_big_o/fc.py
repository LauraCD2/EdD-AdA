#Descripción del problema
#genere codigo
#En este ejercicio deberás identificar la letra más común (o moda) en una cadena recibida por parámetro. Crea una función que reciba una cadena (str) que será analizada, y que retorne otra cadena (str) que contenga la letra más común en la cadena inicial.
#Para tu facilidad, las cadenas que recibirás solo contendrán letras mayúsculas y no tendrán tildes o acentos. No obstante, estas pueden tener espacios, puntos y comas.
#En caso de que haya 2 letras con la misma cantidad de apariciones, debes retornar la que sea alfabéticamente posterior.
#Función requerida
#Tu solución debe tener una función de acuerdo con la siguiente especificación. 
#Nombre de la funcion: letra_mas_comun
#Nombre del parámetro: cadena
#Tipo del parámetro: str
#Descripción del parámetro: Cadena de caracteres en la que se quiere saber cual es la letra mas comun
#Tipo de retorno: str
#Descripción del retorno: Letra mas comun en la cadena que ingresa como parametro. Si son dos o mas, es la letra alfabeticamente posterior.
#eliminar espacios en blanco

def letra_mas_comun(cadena):
    # Eliminar espacios en blanco, puntos y comas de la cadena
    cadena = cadena.replace(" ", "").replace(",", "").replace(".", "")
    # Convertir la cadena a mayúsculas para asegurarse de que todas las letras sean mayúsculas
    cadena = cadena.upper()
    # Contar la frecuencia de cada letra en la cadena
    contador = {}
    for letra in cadena:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    # Encontrar la letra más común
    max_frecuencia = 0
    letra_max_frecuencia = ''
    for letra, frecuencia in contador.items():
        if frecuencia > max_frecuencia:
            max_frecuencia = frecuencia
            letra_max_frecuencia = letra
        elif frecuencia == max_frecuencia:
            if letra > letra_max_frecuencia:
                letra_max_frecuencia = letra
    return letra_max_frecuencia
cadena="A VER SI ESTO ES DE TU TALLA, AMIGA ENORME"
letra_comun = letra_mas_comun(cadena)
print(letra_comun) # Output: 'e"