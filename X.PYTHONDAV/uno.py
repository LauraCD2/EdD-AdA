#El objetivo final del proyecto es predecir la edad de un 
#abalón, utilizando información de las variables disponibles 
#en la base de datos. En este primer avance, el objetivo es 
#realizar el análisis exploratorio de los datos. En particular, 
#debes realizar lo siguiente:
#i. ¿Cuántos datos tenemos para nuestro análisis?
#ii. Encontrar estadísticas descriptivas de todas las variables de 
#la base de datos. Entre ellas, deben estar: media, desviación 
#estándar, mínimo, máximo, percentiles 25, 50 y 75.
#iii. Hacer un análisis exploratorio para ver qué variables pueden 
#ser las mejores al momento de predecir si una persona tiene 
#diabetes. Para esto, debes generar: 
#i. Gráficos de dispersión de las variables 2.-8. contra la variable 
#edad. ¿Cuáles variables parecieran ser buenas para explicar 
#la edad de un abalón? Nota: Si se intenta hacer el gráfico de 
#dispersión de la librería Seaborn para la variable sexo agregándole 
#la línea de regresión como hicimos en clase, va a arrojar error por 
#ser una variable categórica. Por eso debemos excluirla de este 
#análisis si queremos agregar línea de regresión.
#ii. Gráfico de calor para ver las correlaciones existentes entre 
#variables. ¿Lo que se observa en el gráfico de calor concuerda 
#con lo encontrado en los gráficos de dispersión? ¿Cuáles variables 
#tienen correlaciones positivas o negativas más fuertes con 
#respecto a la variable edad?
#iii. Gráficos de cajas y bigotes para todas las variables categóricas 
#o discretas. ¿Cuáles variables son categóricas? ¿Qué categorías 
#tienen mayor edad en promedio?

#Importar librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#traer base de datos abalon_train.csv
abalon_train = pd.read_csv('abalon_train.csv')

#i. ¿Cuántos datos tenemos para nuestro análisis?
abalon_train.shape

#ii. Encontrar estadísticas descriptivas de todas las variables de
#la base de datos. Entre ellas, deben estar: media, desviación
#estándar, mínimo, máximo, percentiles 25, 50 y 75.
abalon_train.describe()

#media, desviación estándar, mínimo, máximo, percentiles 25, 50 y 75.
abalon_train.describe(include = 'all')

#iii. Hacer un análisis exploratorio para ver qué variables pueden
#ser las mejores al momento de predecir si una persona tiene
#diabetes. Para esto, debes generar:
#i. Gráficos de dispersión de las variables 2.-8. contra la variable
#edad. ¿Cuáles variables parecieran ser buenas para explicar
#la edad de un abalón? Nota: Si se intenta hacer el gráfico de
#dispersión de la librería Seaborn para la variable sexo agregándole
#la línea de regresión como hicimos en clase, va a arrojar error por
#ser una variable categórica. Por eso debemos excluirla de este
#análisis si queremos agregar línea de regresión.
abalon_train.columns
abalon_train.columns[1:8]
abalon_train.columns[1:8].tolist()

#Gráficos de dispersión de las variables 2.-8. contra la variable
#edad. ¿Cuáles variables parecieran ser buenas para explicar
#la edad de un abalón? Nota: Si se intenta hacer el gráfico de
#dispersión de la librería Seaborn para la variable sexo agregándole
#la línea de regresión como hicimos en clase, va a arrojar error por
#ser una variable categórica. Por eso debemos excluirla de este
#análisis si queremos agregar línea de regresión.
abalon_train.columns[1:8].tolist()
for i in abalon_train.columns[1:8].tolist():
    sns.lmplot(x = i, y = 'edad', data = abalon_train)
    plt.show()
    
#ii. Gráfico de calor para ver las correlaciones existentes entre
#variables. ¿Lo que se observa en el gráfico de calor concuerda
#con lo encontrado en los gráficos de dispersión? ¿Cuáles variables
#tienen correlaciones positivas o negativas más fuertes con
#respecto a la variable edad?
sns.heatmap(abalon_train.corr(), annot = True)
plt.show()

#iii. Gráficos de cajas y bigotes para todas las variables categóricas
#o discretas. ¿Cuáles variables son categóricas? ¿Qué categorías
#tienen mayor edad en promedio?
sns.boxplot(x = 'sexo', y = 'edad', data = abalon_train)
plt.show()

