#En la universidad se efectuó la elección del representante de los estudiantes ante el Consejo Superior. Se presentaron 30 candidatos y cada uno se identificó con un número del 1 al 30. Asumiendo que los 5000 estudiantes de la universidad votaron, elabore un programa donde:
#Imprima un listado de mayor a menor, según el número de votos obtenidos por cada candidato
#total votos = 5000

import numpy as np

#vector con los votos de cada candidato, cantidad max de votos = 5000
votos = np.random.randint(1, 5000, 30)

#suma de votos
total_votos = sum(votos) 

#normalizar los votos // formula matematica: votos_normalizados = votos / suma_votos * valor_objetivo

votos_normalizados = votos / total_votos * 5000 #normalizar los votos con la formula matematica
votos_normalizados = np.round(votos_normalizados).astype(int) #redondear los votos normalizados

#vector con los candidatos
candidatos = {}
for i in range(30):
    candidatos[i] = i + 1

#ordenar los votos de mayor a menor numero de votos
for i in range(30):
    for j in range(30):
        if votos_normalizados[i] > votos_normalizados[j]:
            votos_normalizados[i], votos_normalizados[j] = votos_normalizados[j], votos_normalizados[i]
            candidatos[i], candidatos[j] = candidatos[j], candidatos[i]

#imprimir de mayor a menor numero de votos
print("El listado de mayor a menor, según el número de votos obtenidos por cada candidato es:")
for i in range(30):
    print("El candidato", candidatos[i], "obtuvo", votos_normalizados[i], "votos")

#comprobar que la suma de votos es igual a 5000
#print("La suma total de votos es:", sum(votos_normalizados))
print ("Hecho por: Laura Camila Diaz Delgado - 2220100")

