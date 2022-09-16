# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:46:11 2022

@author: igori
"""

import pandas as pd

df = pd.read_csv('dataset/00_iris.csv')

df.head(1)  # Muestra la cabecera y la primera fila
df.columns
df.shape  # Número de filas y columnas
df_slicing = df[10:25]
df_specific = df[['sepal_length', 'petal_length']]
df.loc[df['species'] == 'setosa']  # Muestra las filas con 'species'=='setosa'
# Cuenta el número de veces que se repite una especie.
df["species"].value_counts()

sum_data = df["sepal_length"].sum()  # suma
mean_data = df["sepal_length"].mean()  # media
median_data = df["sepal_length"].median()  # mediana
print("Suma:", sum_data, "\nMedia:", mean_data, "\nMediana:", median_data)

min_data = df["sepal_length"].min()  # mínimo
max_data = df["sepal_length"].max()  # máximo
print("Mínimo:", min_data, "\nMáxim0:", max_data)

df.isnull().value_counts()  # Para contar valores nulos.
df.isnull().sum()  # Para contar valores nulos.

# Cambiar de nombre las columnas.
newcols = {"sepal_length": "sepallength", "sepal_width": "sepalwidth"}
# Pasamos un diccionario en columns y inplace=True para no crear un nuevo df.
df.rename(columns=newcols, inplace=True)

# Cambiar valores en "species" por números.
df['species'] = df['species'].replace(['setosa',
                                       'versicolor', 'virginica'], [0, 1, 2])
# Guardar resultado en un nuevo csv.
df.to_csv(r'dataset\00_iris_manipulado.csv', index=False)
