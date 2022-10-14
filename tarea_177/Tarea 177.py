# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:08:00 2022

@author: igori
"""

import pandas as pd
import missingno as msno
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_excel('ejercicio_Missing_Values.xlsx')

print(df.dtypes)
df.info()
print(df.isna().sum())

perc_nulls = (df.isna().sum()/len(df))*100
print(perc_nulls)

msno.matrix(df, figsize=(8, 5), fontsize=12)
msno.bar(df, figsize=(8, 5), fontsize=12)


# Eliminar filas 17 y 35, que son nulas en todas sus columnas.
df = df.drop([6, 17, 35])

# Eliminamos la columna NIF, que contiene bastantes nulos y no aporta.
del df['NIF']
# Rellenamos las referencias de estudio nulas con el código de todo el dataset.
df["REFERENCIA ESTUDIO"] = df["REFERENCIA ESTUDIO"][0]

# Todos los nulos en la columna de consumidores de alcohol serán 'NO'.
# Está especificado en el enunciado.
df.loc[pd.isnull(df['Consumidorx Alcohol Esporádico']),
       'Consumidorx Alcohol Esporádico'] = 'NO'

# Columna "CARNÉ CONDUCIR"
# Si la persona es <18, no tiene carné. Si >=18, si tiene.
df.loc[(pd.isnull(df['CARNÉ CONDUCIR']) & (df['Edad'] < 18)),
       'CARNÉ CONDUCIR'] = 'NO'
df.loc[pd.isnull(df['CARNÉ CONDUCIR']), 'CARNÉ CONDUCIR'] = 'NO'

# Columna " Vacunadx"
# Las vacunas no pueden administrarse a personas menores de 5 años.
df.loc[(pd.isnull(df['Vacunadx']) & (df['Edad'] < 5)),
       'Vacunadx'] = 'No'

# Columna "Estado Civil"
# Todos los nulos son menores de 18, se asigna estado "Solter/x".
df.loc[(pd.isnull(df['Estado Civil']) & (df['Edad'] < 18)),
       'Estado Civil'] = 'Solter/x'

# Columna "Ingresos"
# Para personas menores de 16 años los ingresos serán de 0€.
df.loc[(pd.isnull(df['Ingresos']) & (df['Edad'] < 16)),
       'Ingresos'] = 0
# Seguimos teniendo un valor nulo en la columna "Ingresos".
sns.stripplot(data=df, x="Ingresos")
plt.title('Stripplot de los Ingresos', fontsize=14)
plt.show()
# Al ser un único valor, se decide sustituirlo por la media de los ingresos.
# Para el cálculo de la media se han eliminado todas los filas que sean 0€.
df["Ingresos"] = df["Ingresos"].fillna(df.loc[df['Ingresos'] > 0,
                                              'Ingresos'].mean())

# Columna "Hijos"
# Consideramos que una persona menor de 16 no tiene hijos.
df.loc[(pd.isnull(df['Hijos']) & (df['Edad'] < 16)),
       'Hijos'] = 'NO'

# Columna "Estatura" y "Masa"
sns.scatterplot(data=df, x=df.Estatura, y=df.Masa)
plt.title('Estatura-Masa scatterplot', fontsize=14)
plt.show()
# Como se ve hay una correlación (exponencial) entre estatura y masa.
# Se podría hacer una regresión a una función e^x.
# Si se aplica un ajuste logarítmico se convierte en lineal.
sns.scatterplot(data=df, x=df.Estatura, y=np.log(df.Masa))
plt.title('Estatura-Masa scatterplot (ajuste logarítmico)', fontsize=14)
plt.ylabel('log(Masa)')
plt.show()

'''
No hay correlación entre consumidor de alcohol y masa (solo en niños)
En la relación masa-edad, en la juventud la relación es lineal, pero luego
a partir de los 20 años la distribución es normal. Por lo tanto, como en este
caso todos los valores faltantes son para mayores de 20 años se cojera le media
de altura o masa de adultos y se introducirá en la recta de la regresión para
sacar el valor faltante.
'''

sns.scatterplot(data=df, y=df['Masa'], x=df['Consumidorx Alcohol Esporádico'])
plt.title('Masa-Consumidor Alcohol scatterplot)', fontsize=14)
plt.show()

sns.scatterplot(data=df, y=df['Estatura'], x=df['Edad'])
plt.title('Masa-Edad scatterplot)', fontsize=14)
plt.show()


# Realizamos la regresión entre estatura y masa.

# Eliminamos las filas nulas para poder hacer la regresión.
df_estmasa = df[['Estatura', 'Masa']].dropna()
# Eliminamos la fila 28 como valor atípico.
df_estmasa = df_estmasa.drop([28])
# Realizamos la regresión lineal usando un ajuste logarítmico.
regr = linear_model.LinearRegression()
x = np.array(df_estmasa.Estatura).reshape(-1, 1)
lny = np.array(np.log(df_estmasa.Masa))
regr.fit(x, lny)
y_pred = regr.predict(x)
print('Coefficients: \n', regr.coef_)
print('Independent term: \n', regr.intercept_)
# y = mx + b // y = regr.coef_*x+regr.intercept_
print("Mean squared error: %.2f" % mean_squared_error(lny, y_pred))
print('Variance score: %.2f' % r2_score(lny, y_pred))
# Graficamos la regresión lineal construida junto con los valores reales.
plt.plot(x, lny, 'ro', label='data')
plt.plot(x, y_pred, linewidth=3.0, label='fit')
plt.legend(loc='best')
plt.ylabel('log(Masa)')
plt.xlabel('Estatura')
plt.title('Regresión lineal (con ajuste logarítmico) de Estatura-Masa')
plt.show()

# Calculamos la estatura media para los adultos y quitamos el valor atipico.
est_mean = df.loc[((df['Edad'] >= 18) & (df['Estatura'] > 100)),
                  'Estatura'].mean()
# Introducimos la estatura media en las columnas con valores nulos.
df.loc[(pd.isnull(df['Estatura'])) & (pd.isnull(df['Masa'])),
       'Estatura'] = est_mean
# Se calcula la masa de las filas nulas con la función de regresión lineal...
# ...calculada anteriormente.
# y=mx+b donde m=regr.coef_, x=estatura y b=regr.intercept_.
df.loc[pd.isnull(df['Masa']),
       'Masa'] = np.exp((df['Estatura']*regr.coef_)+regr.intercept_)

# Sustituimos la estatura del valor atípico identificado antes usando los...
# ...parámetros de la regresión lineal.
# x=(y-b)/m
df = df.reset_index()
df.iloc[26, 8] = (np.log(df.iloc[26, 9])-regr.intercept_)/regr.coef_

# Por último, para los 2 filas nulas en Municipio y Provincia asignamos...
# ...Madrid por probabilidad.
df.loc[pd.isnull(df['Provincia']), 'Provincia'] = 'Madrid'
df.loc[pd.isnull(df['Municipio']), 'Municipio'] = 'Madrid'

# Comprobamos que no nos quede ninguna fila o columna nula.
print(df.isna().sum())


# BIBLIOGRAFÍA
# https://github.com/ResidentMario/missingno
# https://www.iartificial.net/regresion-lineal-con-ejemplos-en-python/
# https://www.aprendemachinelearning.com/regresion-lineal-en-espanol-con-python/
# https://www.zweigmedia.com/MundoReal/calctopic1/regression.html
