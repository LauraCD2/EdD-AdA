#En la universidad se efectuó la elección del representante de los estudiantes ante el Consejo Superior. Se presentaron 30 candidatos y cada uno se identificó con un número del 1 al 30. Asumiendo que los 5000 estudiantes de la universidad votaron, elabore un programa donde:
#Imprima un listado de mayor a menor, según el número de votos obtenidos por cada candidato

import numpy as np

#vector con los votos de cada candidato
votos= np.random.randint(0,5000,30)

#vector con los candidatos
candidatos={}
for i in range(30):
    candidatos[i]=i+1
    
#ordenar los votos de mayor a menor cantidad de votos
